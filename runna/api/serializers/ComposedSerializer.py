from rest_framework import serializers

from infrastructure.models import (
    TDemanda,
    TDemandaScore,
    TOrigenDemanda,
    TDemandaPersona,
    TPersona,
    TPrecalificacionDemanda,
    TLocalizacion,
    TNNyAEducacion,
    TInformante,
    TVinculoPersonaPersona,
    TCondicionesVulnerabilidad,
    TLocalizacionPersona,
    TPersonaCondicionesVulnerabilidad,
    TNNyAEducacion,
    TNNyASalud,
    TVulneracion
)
from api.serializers import (
    TDemandaSerializer,
    TDemandaScoreSerializer,
    TOrigenDemandaSerializer,
    TDemandaPersonaSerializer,
    TPersonaSerializer,
    TPrecalificacionDemandaSerializer,
    TSubOrigenDemandaSerializer,
    TCategoriaMotivoSerializer,
    TCategoriaSubmotivoSerializer,
    TBarrioSerializer,
    TLocalidadSerializer,
    TCPCSerializer,
    TVinculoPersonaSerializer,
    TCondicionesVulnerabilidadSerializer,
    TInstitucionEducativaSerializer,
    TInstitucionSanitariaSerializer,
    TUrgenciaVulneracionSerializer,
    TGravedadVulneracionSerializer,
    TLocalizacionSerializer,
    TInformanteSerializer,
    TVinculoPersonaPersonaSerializer,
    TNNyAEducacionSerializer,
    TNNyASaludSerializer,
    TVulneracionSerializer
)

class MesaDeEntradaSerializer(serializers.ModelSerializer):
    demanda_score = serializers.SerializerMethodField()
    origen_demanda = serializers.SerializerMethodField()
    nnya_principal = serializers.SerializerMethodField()
    precalificacion = serializers.SerializerMethodField()

    def get_demanda_score(self, obj):
        try:
            score = TDemandaScore.objects.get(demanda=obj)
            return TDemandaScoreSerializer(score).data
        except TDemandaScore.DoesNotExist:
            return None

    def get_origen_demanda(self, obj):
        return TOrigenDemandaSerializer(obj.origen).data if obj.origen else None

    def get_nnya_principal(self, obj):
        try:
            demandaPersona = TDemandaPersona.objects.get(demanda=obj, nnya_principal=True)
            return TPersonaSerializer(demandaPersona.persona).data
        except TDemandaPersona.DoesNotExist:
            return None

    def get_precalificacion(self, obj):
        try:
            precalificacion = TPrecalificacionDemanda.objects.get(demanda=obj)
            return TPrecalificacionDemandaSerializer(precalificacion).data
        except TPrecalificacionDemanda.DoesNotExist:
            return None
        
    class Meta:
        model = TDemanda
        fields = '__all__'


# Custom ChoiceField Serializer to avoid redundant code
class ChoiceFieldSerializer(serializers.Serializer):
    key = serializers.CharField()
    value = serializers.CharField()

    @staticmethod
    def from_model(choices):
        """Converts model choices into a serializable format"""
        return [{"key": key, "value": value} for key, value in choices]

class NuevoRegistroFormDropdownsSerializer(serializers.Serializer):
    """Main serializer to group all dropdown data"""
    
    estado_demanda_choices = serializers.SerializerMethodField()
    ambito_vulneracion_choices = serializers.SerializerMethodField()
    tipo_calle_choices = serializers.SerializerMethodField()
    situacion_dni_choices = serializers.SerializerMethodField()
    genero_choices = serializers.SerializerMethodField()
    supuesto_autordv_choices = serializers.SerializerMethodField()
    nivel_choices = serializers.SerializerMethodField()
    turno_choices = serializers.SerializerMethodField()

    informantes = TInformanteSerializer(many=True)
    origenes = TOrigenDemandaSerializer(many=True)
    sub_origenes = TSubOrigenDemandaSerializer(many=True)
    categoria_motivos = TCategoriaMotivoSerializer(many=True)
    categoria_submotivos = TCategoriaSubmotivoSerializer(many=True)
    barrios = TBarrioSerializer(many=True)
    localidades = TLocalidadSerializer(many=True)
    cpcs = TCPCSerializer(many=True)
    vinculos = TVinculoPersonaSerializer(many=True)
    condiciones_vulnerabilidad = TCondicionesVulnerabilidadSerializer(many=True)
    instituciones_educativas = TInstitucionEducativaSerializer(many=True)
    instituciones_sanitarias = TInstitucionSanitariaSerializer(many=True)
    gravedades_vulneracion = TGravedadVulneracionSerializer(many=True)
    urgencias_vulneracion = TUrgenciaVulneracionSerializer(many=True)

    class Meta:
        fields = '__all__'

    # 🔥 Optimized Choice Fields using SerializerMethodField
    def get_estado_demanda_choices(self, obj):
        return ChoiceFieldSerializer.from_model(TDemanda.estado_demanda_choices)

    def get_ambito_vulneracion_choices(self, obj):
        return ChoiceFieldSerializer.from_model(TDemanda.ambito_vulneracion_choices)

    def get_tipo_calle_choices(self, obj):
        return ChoiceFieldSerializer.from_model(TLocalizacion.tipo_calle_choices)

    def get_situacion_dni_choices(self, obj):
        return ChoiceFieldSerializer.from_model(TPersona.situacion_dni_choices)

    def get_genero_choices(self, obj):
        return ChoiceFieldSerializer.from_model(TPersona.genero_choices)

    def get_supuesto_autordv_choices(self, obj):
        return ChoiceFieldSerializer.from_model(TDemandaPersona.supuesto_autordv_choices)

    def get_nivel_choices(self, obj):
        return ChoiceFieldSerializer.from_model(TNNyAEducacion.nivel_choices)

    def get_turno_choices(self, obj):
        return ChoiceFieldSerializer.from_model(TNNyAEducacion.turno_choices)


class AdultoSerializer(serializers.Serializer):
    persona = TPersonaSerializer()
    demanda_persona = TDemandaPersonaSerializer(required=False, allow_null=True)
    localizacion = TLocalizacionSerializer(required=False, allow_null=True)  # Can be same as Demanda, new, or null
    use_demanda_localizacion = serializers.BooleanField(required=False, default=False)  # Flag to indicate reuse
    vinculo_nnya_principal = TVinculoPersonaPersonaSerializer(required=False, allow_null=True)
    condiciones_vulnerabilidad = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=TCondicionesVulnerabilidad.objects.all(),  # Ensure only valid IDs are accepted
        required=False
    )
class TVulneracionNuevoRegistroSerializer(serializers.ModelSerializer):
    autordv_index = serializers.IntegerField(write_only=True, allow_null=False)
    
    class Meta:
        model = TVulneracion
        fields = '__all__'
        read_only_fields = ['sumatoria_de_pesos', 'nnya', 'deleted']

class NNyAPrincipalSerializer(serializers.Serializer):
    persona = TPersonaSerializer()
    demanda_persona = TDemandaPersonaSerializer(required=False, allow_null=True)
    localizacion = TLocalizacionSerializer(required=False, allow_null=True)  # Can be same as Demanda, new, or null
    use_demanda_localizacion = serializers.BooleanField(required=False, default=False)  # Flag to indicate reuse
    condiciones_vulnerabilidad = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=TCondicionesVulnerabilidad.objects.all(),  # Ensure only valid IDs are accepted
        required=False
    )
    nnya_educacion = TNNyAEducacionSerializer(required=False, allow_null=True)
    nnya_salud = TNNyASaludSerializer(required=False, allow_null=True)
    vulneraciones = TVulneracionNuevoRegistroSerializer(many=True, required=False)

class NNyASecundariosSerializer(NNyAPrincipalSerializer):
    vinculo_nnya_principal = TVinculoPersonaPersonaSerializer(required=False, allow_null=True)


class RegistroCasoFormSerializer(serializers.ModelSerializer):
    localizacion = TLocalizacionSerializer()
    informante = TInformanteSerializer(required=False, allow_null=True)
    adultos = AdultoSerializer(many=True, required=False)
    nnya_principal = NNyAPrincipalSerializer(required=False, allow_null=True)
    nnyas_secundarios = NNyASecundariosSerializer(many=True, required=False)

    class Meta:
        model = TDemanda
        fields = '__all__'
        
    def to_representation(self, instance):
        """Modify representation to include nested relationships for retrieval."""
        data = super().to_representation(instance)

        # Serialize Localizacion and Informante
        data['localizacion'] = TLocalizacionSerializer(instance.localizacion).data
        if instance.informante:
            data['informante'] = TInformanteSerializer(instance.informante).data

        # Fetch primary NNyA (Main Child)
        nnya_principal_instance = instance.tdemandapersona_set.filter(nnya_principal=True).first()
        if nnya_principal_instance:
            localizacion_nnya_principal = TLocalizacionPersona.objects.filter(persona=nnya_principal_instance.persona).last()
            condiciones_vulnerabilidad = TPersonaCondicionesVulnerabilidad.objects.filter(persona=nnya_principal_instance.persona, demanda=instance)
            data['nnya_principal'] = NNyAPrincipalSerializer({
                'persona': nnya_principal_instance.persona,
                'demanda_persona': nnya_principal_instance,
                'localizacion': localizacion_nnya_principal.localizacion if localizacion_nnya_principal else None,
                'condiciones_vulnerabilidad': [cv.condicion_vulnerabilidad for cv in condiciones_vulnerabilidad],
                'nnya_educacion': TNNyAEducacion.objects.filter(nnya=nnya_principal_instance.persona).first(),
                'nnya_salud': TNNyASalud.objects.filter(nnya=nnya_principal_instance.persona).first(),
                'vulneraciones': TVulneracion.objects.filter(nnya=nnya_principal_instance.persona, demanda=instance)
            }).data
        print(f"OK NNyA: {data['nnya_principal']}")

        # Fetch secondary NNyAs
        nnyas_secundarios_instances = instance.tdemandapersona_set.filter(nnya_principal=False, persona__nnya=True)
        nnyas_secundarios_data = []
        for nnya in nnyas_secundarios_instances:
            localizacion_nnya_secundario = TLocalizacionPersona.objects.filter(persona=nnya.persona).last()
            condiciones_vulnerabilidad = TPersonaCondicionesVulnerabilidad.objects.filter(persona=nnya.persona, demanda=instance)
            print(f"nnya secundario: {nnya.persona}")
            nnyas_secundarios_data.append(NNyASecundariosSerializer({
                'persona': nnya.persona,
                'demanda_persona': nnya,
                'localizacion': localizacion_nnya_secundario.localizacion if localizacion_nnya_secundario else None,
                'condiciones_vulnerabilidad': [cv.condicion_vulnerabilidad for cv in condiciones_vulnerabilidad],
                'nnya_educacion': TNNyAEducacion.objects.filter(nnya=nnya.persona).first(),
                'nnya_salud': TNNyASalud.objects.filter(nnya=nnya.persona).first(),
                'vinculo_nnya_principal': TVinculoPersonaPersona.objects.filter(persona_1=nnya_principal_instance.persona, persona_2=nnya.persona).first(),
                'vulneraciones': TVulneracion.objects.filter(nnya=nnya.persona, demanda=instance)
            }).data)
        data['nnyas_secundarios'] = nnyas_secundarios_data

        # Fetch Adultos
        adultos_instances = instance.tdemandapersona_set.filter(persona__adulto=True)
        adultos_data = []
        for adulto in adultos_instances:
            localizacion_adulto = TLocalizacionPersona.objects.filter(persona=adulto.persona).last()
            condiciones_vulnerabilidad = TPersonaCondicionesVulnerabilidad.objects.filter(persona=adulto.persona, demanda=instance)
            adultos_data.append(AdultoSerializer({
                'persona': adulto.persona,
                'demanda_persona': adulto,
                'localizacion': localizacion_adulto.localizacion if localizacion_adulto else None,
                'condiciones_vulnerabilidad': [cv.condicion_vulnerabilidad for cv in condiciones_vulnerabilidad],
                'vinculo_nnya_principal': TVinculoPersonaPersona.objects.filter(persona_1=nnya_principal_instance.persona, persona_2=adulto.persona).first()
            }).data)
        data['adultos'] = adultos_data

        return data


    def create(self, validated_data):
        localizacion_data = validated_data.pop('localizacion')
        informante_data = validated_data.pop('informante', None)
        adultos_data = validated_data.pop('adultos', [])
        nnya_principal_data = validated_data.pop('nnya_principal', None)
        nnyas_secundarios_data = validated_data.pop('nnyas_secundarios', [])

        # Handle Localizacion (always create one for Demanda)
        localizacion = TLocalizacion.objects.create(**localizacion_data)

        informante = None
        if informante_data:
            informante = TInformante.objects.create(**informante_data)

        # Create TDemanda instance
        demanda = TDemanda.objects.create(localizacion=localizacion, informante=informante, **validated_data)


        nnya_principal_db = None
        # Handle NNyA Principal Data
        if nnya_principal_data:
            persona_data = nnya_principal_data.pop('persona')
            demanda_persona_data = nnya_principal_data.pop('demanda_persona', None)
            localizacion_data = nnya_principal_data.pop('localizacion', None)
            use_demanda_localizacion = nnya_principal_data.pop('use_demanda_localizacion', False)
            condiciones_vulnerabilidad = nnya_principal_data.pop('condiciones_vulnerabilidad', [])
            nnya_educacion_data = nnya_principal_data.pop('nnya_educacion', None)
            nnya_salud_data = nnya_principal_data.pop('nnya_salud', None)

            # Create or get Persona
            nnya_principal_db, _ = TPersona.objects.get_or_create(**persona_data)

            # Determine Localizacion for Persona
            if use_demanda_localizacion:
                # Assign same localizacion as Demanda
                localizacion_persona = TLocalizacionPersona.objects.create(persona=nnya_principal_db, localizacion=demanda.localizacion)
            elif localizacion_data:
                new_localizacion, _ = TLocalizacion.objects.get_or_create(**localizacion_data)
                localizacion_persona = TLocalizacionPersona.objects.create(persona=nnya_principal_db, localizacion=new_localizacion)
            else:
                pass
        
            if demanda_persona_data:
                TDemandaPersona.objects.create(persona=nnya_principal_db, demanda=demanda, **demanda_persona_data)
            
            for condicion in condiciones_vulnerabilidad:
                TPersonaCondicionesVulnerabilidad.objects.create(persona=nnya_principal_db, condicion_vulnerabilidad=condicion, demanda=demanda, si_no=True)
                
            if nnya_educacion_data:
                TNNyAEducacion.objects.create(nnya=nnya_principal_db, **nnya_educacion_data)
            
            if nnya_salud_data:
                TNNyASalud.objects.create(nnya=nnya_principal_db, **nnya_salud_data)


        # Handle Adultos Data
        adultos_db = {} # Store created personas as {adulto_index_request: persona_instance}
        count = 0
        for adulto_data in adultos_data:
            persona_data = adulto_data.pop('persona')
            demanda_persona_data = adulto_data.pop('demanda_persona', None)
            localizacion_data = adulto_data.pop('localizacion', None)
            use_demanda_localizacion = adulto_data.pop('use_demanda_localizacion', False)
            vinculo_nnya_principal_data = adulto_data.pop('vinculo_nnya_principal', None)
            condiciones_vulnerabilidad = adulto_data.pop('condiciones_vulnerabilidad', [])

            # Create or get Persona
            adulto_db, _ = TPersona.objects.get_or_create(**persona_data)

            # Determine Localizacion for Persona
            if use_demanda_localizacion:
                # Assign same localizacion as Demanda
                localizacion_persona = TLocalizacionPersona.objects.create(persona=adulto_db, localizacion=demanda.localizacion)
            elif localizacion_data:
                new_localizacion, _ = TLocalizacion.objects.get_or_create(**localizacion_data)
                localizacion_persona = TLocalizacionPersona.objects.create(persona=adulto_db, localizacion=new_localizacion)
            else:
                pass  # No localizacion provided

            # Create DemandaPersona if provided
            if demanda_persona_data:
                TDemandaPersona.objects.create(persona=adulto_db, demanda=demanda, **demanda_persona_data)

            # Create Vinculo if provided
            print(vinculo_nnya_principal_data)
            if vinculo_nnya_principal_data:
                print('Creating vinculo')
                TVinculoPersonaPersona.objects.create(persona_1=nnya_principal_db, persona_2=adulto_db, **vinculo_nnya_principal_data)

            # Assign Condiciones de Vulnerabilidad (only using existing IDs)
            for condicion in condiciones_vulnerabilidad:
                TPersonaCondicionesVulnerabilidad.objects.create(persona=adulto_db, condicion_vulnerabilidad=condicion, demanda=demanda, si_no=True)
            
            adultos_db[count] = adulto_db
            print(adultos_db)
            count += 1

 
        # Handle NNyA Principal Vulneraciones
        if nnya_principal_data:
            vulneraciones_data = nnya_principal_data.pop('vulneraciones', [])
            print(vulneraciones_data)
            for vulneracion_data in vulneraciones_data:
                autordv_index = vulneracion_data.pop('autordv_index', None)
                print(f'Autordv Index: {autordv_index}')
                print(f'Adultos DB: {adultos_db[autordv_index]}')
                TVulneracion.objects.create(nnya=nnya_principal_db, autor_dv=adultos_db[autordv_index], demanda=demanda, **vulneracion_data)

        # Handle NNyA Secundarios
        for nnya_secundario_data in nnyas_secundarios_data:
            persona_data = nnya_secundario_data.pop('persona')
            demanda_persona_data = nnya_secundario_data.pop('demanda_persona', None)
            localizacion_data = nnya_secundario_data.pop('localizacion', None)
            use_demanda_localizacion = nnya_secundario_data.pop('use_demanda_localizacion', False)
            vinculo_nnya_principal_data = nnya_secundario_data.pop('vinculo_nnya_principal', None)
            condiciones_vulnerabilidad = nnya_secundario_data.pop('condiciones_vulnerabilidad', [])
            nnya_educacion_data = nnya_secundario_data.pop('nnya_educacion', None)
            nnya_salud_data = nnya_secundario_data.pop('nnya_salud', None)

            # Create or get Persona
            nnya_secundario_db, _ = TPersona.objects.get_or_create(**persona_data)

            # Determine Localizacion for Persona
            if use_demanda_localizacion:
                # Assign same localizacion as Demanda
                localizacion_persona = TLocalizacionPersona.objects.create(persona=nnya_secundario_db, localizacion=demanda.localizacion)
            elif localizacion_data:
                new_localizacion, _ = TLocalizacion.objects.get_or_create(**localizacion_data)
                localizacion_persona = TLocalizacionPersona.objects.create(persona=nnya_secundario_db, localizacion=new_localizacion)
            else:
                pass
            
            # Create DemandaPersona if provided
            if demanda_persona_data:
                TDemandaPersona.objects.create(persona=nnya_secundario_db, demanda=demanda, **demanda_persona_data)
            
            # Create Vinculo if provided
            if vinculo_nnya_principal_data:
                TVinculoPersonaPersona.objects.create(persona_1=nnya_principal_db, persona_2=nnya_secundario_db, **vinculo_nnya_principal_data)
            
            # Assign Condiciones de Vulnerabilidad (only using existing IDs)
            for condicion in condiciones_vulnerabilidad:
                TPersonaCondicionesVulnerabilidad.objects.create(persona=nnya_secundario_db, condicion_vulnerabilidad=condicion, demanda=demanda, si_no=True)
            
            if nnya_educacion_data:
                TNNyAEducacion.objects.create(nnya=nnya_secundario_db, **nnya_educacion_data)
            
            if nnya_salud_data:
                TNNyASalud.objects.create(nnya=nnya_secundario_db, **nnya_salud_data)
 
            for vulneracion_data in nnya_secundario_data.pop('vulneraciones', []):
                autordv_index = vulneracion_data.pop('autordv_index', None)
                TVulneracion.objects.create(nnya=nnya_secundario_db, autor_dv=adultos_db[autordv_index], demanda=demanda, **vulneracion_data)

        return demanda

    def update(self, instance, validated_data):
        localizacion_data = validated_data.pop('localizacion', None)
        informante = validated_data.pop('informante', None)

        if localizacion_data:
            for attr, value in localizacion_data.items():
                setattr(instance.localizacion, attr, value)
            instance.localizacion.save()

        if informante is not None:
            if instance.informante is not None:
                instance.informante = informante
            else:
                informante = TInformante.objects.create(**informante)
                instance.informante = informante

        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        
        instance.save()
        return instance
