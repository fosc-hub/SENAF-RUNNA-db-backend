from django.db.models import Q, CharField
from django.db.models.functions import Cast
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Importa los modelos necesarios (asegúrate de que las rutas sean correctas según tu proyecto)
from infrastructure.models import (
    TPersona,
    TCodigoDemanda,
    TLocalizacion,
    TDemanda,
    TDemandaPersona,
)

class DemandaBusquedaVinculacionView(APIView):
    """
    Endpoint para buscar coincidencias en:
      - TPersona (por nombre, apellido y dni)
      - TCodigoDemanda (por codigo)
      - TLocalizacion (por calle y localidad)
    Y luego retornar:
      - Una lista de IDs de las demandas vinculadas
      - Una descripción detallada de cada match encontrado.
    """

    def post(self, request, *args, **kwargs):
        data = request.data

        # Extrae los parámetros del body
        nombre_y_apellido = data.get('nombre_y_apellido')
        dni = data.get('dni')
        codigo = data.get('codigo')
        localizacion_data = data.get('localizacion')

        # Usaremos un set para ir acumulando los IDs (para evitar duplicados)
        demanda_ids = set()
        # Lista para acumular las descripciones de los matchs
        match_descriptions = []

        # --- BÚSQUEDA EN TPersona ---
        if nombre_y_apellido or dni:
            persona_qs = TPersona.objects.all()
            terms = []
            if nombre_y_apellido:
                nombre_y_apellido = nombre_y_apellido.strip()  # elimina solo espacios al inicio/final
                terms = nombre_y_apellido.split()  # separa en palabras, ej. ["cell", "before"]
                query = Q()
                for term in terms:
                    query |= Q(nombre__icontains=term) | Q(apellido__icontains=term)
                persona_qs = persona_qs.filter(query)
            if dni is not None:
                # Como 'dni' es un IntegerField, para hacer búsqueda parcial convertimos a cadena
                persona_qs = persona_qs.annotate(dni_str=Cast('dni', CharField())).filter(dni_str__icontains=str(dni))
            
            # Para cada persona encontrada, determinamos qué campos hicieron match
            for person in persona_qs:
                matched_fields = []
                if terms:
                    for term in terms:
                        if term.lower() in person.nombre.lower():
                            if "nombre" not in matched_fields:
                                matched_fields.append("nombre")
                        if term.lower() in person.apellido.lower():
                            if "apellido" not in matched_fields:
                                matched_fields.append("apellido")
                if dni is not None and person.dni is not None:
                    if str(dni) in str(person.dni):
                        matched_fields.append("dni")
                # Buscamos las demandas vinculadas a esta persona a través de TDemandaPersona
                demanda_persona_qs = TDemandaPersona.objects.filter(persona=person)
                for dp in demanda_persona_qs:
                    demanda_ids.add(dp.demanda.id)
                    description = (
                        f"Se encontró coincidencia con persona '{person.nombre} {person.apellido}' (dni {person.dni}) por match en los campos "
                        f"{', '.join(matched_fields)}; vinculado a la demanda {dp.demanda.id}"
                    )
                    match_descriptions.append(description)

        # --- BÚSQUEDA EN TCodigoDemanda ---
        if codigo:
            codigo_qs = TCodigoDemanda.objects.filter(codigo__icontains=codigo)
            for cd in codigo_qs:
                demanda_ids.add(cd.demanda.id)
                description = (
                    f"Se encontró coincidencia en el código '{cd.codigo}' ({cd.tipo_codigo.nombre}); "
                    f"vinculado a la demanda {cd.demanda.id}"
                )
                match_descriptions.append(description)

        # --- BÚSQUEDA EN TLocalizacion ---
        if localizacion_data:
            calle = localizacion_data.get('calle')
            localidad = localizacion_data.get('localidad')
            # Se verifica que ambos campos existan para la búsqueda
            if calle and localidad:
                loc_qs = TLocalizacion.objects.filter(
                    calle__icontains=calle,
                    localidad=localidad  # Suponemos que 'localidad' es un campo numérico o identificador exacto
                )
                for loc in loc_qs:
                    # Se buscan demandas que tengan como localización alguno de los resultados encontrados
                    demanda_qs = TDemanda.objects.filter(localizacion=loc)
                    for demanda in demanda_qs:
                        demanda_ids.add(demanda.id)
                        description = (
                            f"Se encontró coincidencia en la localización por match en el campo 'calle' ({loc.calle}) y "
                            f"'localidad' ({loc.localidad}); vinculado a la demanda {demanda.id}"
                        )
                        match_descriptions.append(description)

        # Se devuelve la lista de IDs (sin duplicados) en la respuesta
        return Response({
            "demanda_ids": list(demanda_ids),
            "match_descriptions": match_descriptions
        }, status=status.HTTP_200_OK)
