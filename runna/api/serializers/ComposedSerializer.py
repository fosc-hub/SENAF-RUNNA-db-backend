from rest_framework import serializers

from customAuth.models import (
    CustomUser,
    TZona,
    TCustomUserZona,
)
from customAuth.serializers import (
    CustomUserSerializer,
    TZonaSerializer,
    TCustomUserZonaSerializer,
)

from infrastructure.models import (
    TBloqueDatosRemitente,
    TTipoInstitucionDemanda,
    TAmbitoVulneracion,
    TTipoPresuntoDelito,
    TInstitucionDemanda,
    TDemanda,
    TDemandaAdjunto,
    TTipoCodigoDemanda,
    TCodigoDemanda,
    TCalificacionDemanda,
    TDemandaScore,
    
    TLocalidad,
    TBarrio,
    TCPC,
    TLocalizacion,
    
    TPersona,
    TInstitucionEducativa,
    TEducacion,
    TInstitucionSanitaria,
    TSituacionSalud,
    TEnfermedad,
    TMedico,
    TCoberturaMedica,
    TPersonaEnfermedades,
    TPersonaOficioAdjunto,
    TPersonaCertificadoAdjunto,
    TNNyAScore,

    TCategoriaMotivo,
    TCategoriaSubmotivo,
    TGravedadVulneracion,
    TUrgenciaVulneracion,
    TCondicionesVulnerabilidad,
    TVulneracion,

    TLocalizacionPersona,
    TDemandaPersona,
    TDemandaZona,
    TDemandaVinculada,
    TPersonaCondicionesVulnerabilidad,
    TVinculoDePersonas,
)
from api.serializers import (
    TBloqueDatosRemitenteSerializer,
    TTipoInstitucionDemandaSerializer,
    TAmbitoVulneracionSerializer,
    TTipoPresuntoDelitoSerializer,
    TInstitucionDemandaSerializer,
    TDemandaSerializer,
    TDemandaAdjuntoSerializer,
    TTipoCodigoDemandaSerializer,
    TCodigoDemandaSerializer,
    TCalificacionDemandaSerializer,
    TDemandaScoreSerializer,
    
    TLocalidadSerializer,
    TBarrioSerializer,
    TCPCSerializer,
    TLocalizacionSerializer,
    
    TVinculoDePersonasSerializer,
    TPersonaSerializer,
    TInstitucionEducativaSerializer,
    TEducacionSerializer,
    TInstitucionSanitariaSerializer,
    TSituacionSaludSerializer,
    TEnfermedadSerializer,
    TMedicoSerializer,
    TCoberturaMedicaSerializer,
    TPersonaOficioAdjuntoSerializer,
    TPersonaCertificadoAdjuntoSerializer,
    TPersonaEnfermedadesSerializer,
    TNNyAScoreSerializer,

    TCategoriaMotivoSerializer,
    TCategoriaSubmotivoSerializer,
    TGravedadVulneracionSerializer,
    TUrgenciaVulneracionSerializer,
    TCondicionesVulnerabilidadSerializer,
    TVulneracionSerializer,

    TLocalizacionPersonaSerializer,
    TDemandaPersonaSerializer,
    TDemandaZonaSerializer,
    TDemandaVinculadaSerializer,
    TPersonaCondicionesVulnerabilidadSerializer,
    
    TActividadTipoSerializer,
    TInstitucionActividadSerializer,
)


class TActividadDropdownSerializer(serializers.Serializer):
    tipos_actividad = TActividadTipoSerializer(many=True)
    instituciones_actividad = TInstitucionActividadSerializer(many=True)
    

class TDemandaZonaRegistroSerializer(serializers.ModelSerializer):
    enviado_por = CustomUserSerializer()
    recibido_por = CustomUserSerializer()
    zona = TZonaSerializer()
    user_responsable = CustomUserSerializer()

    class Meta:
        model = TDemandaZona
        fields = '__all__'
        read_only_fields = ['demanda']


class GestionDemandaZonaSerializer(serializers.Serializer):
    demanda_zonas = TDemandaZonaRegistroSerializer(many=True)
    zonas = TZonaSerializer(many=True)
    users = CustomUserSerializer(many=True)


class MesaDeEntradaSerializer(serializers.ModelSerializer):
    demanda_score = serializers.SerializerMethodField()
    bloque_datos_remitente = TBloqueDatosRemitenteSerializer()
    nnya_principal = serializers.SerializerMethodField()
    calificacion = serializers.SerializerMethodField()
    codigos_demanda = serializers.SerializerMethodField()
    localidad = serializers.SerializerMethodField()
    barrio = serializers.SerializerMethodField()
    cpc = serializers.SerializerMethodField()
    registrado_por_user = CustomUserSerializer()
    registrado_por_user_zona = TZonaSerializer()
    demanda_zona  = serializers.SerializerMethodField()
    calificacion_choices = serializers.SerializerMethodField()

    def get_demanda_score(self, obj):
        try:
            score = TDemandaScore.objects.get(demanda=obj)
            return TDemandaScoreSerializer(score).data
        except TDemandaScore.DoesNotExist:
            return None

    def get_nnya_principal(self, obj):
        try:
            demandaPersona = TDemandaPersona.objects.filter(demanda=obj, vinculo_demanda="NNYA_PRINCIPAL").first()
            return TPersonaSerializer(demandaPersona.persona).data
        except TDemandaPersona.DoesNotExist:
            return None
        except AttributeError:
            return None

    def get_calificacion(self, obj):
        try:
            calificacion = TCalificacionDemanda.objects.get(demanda=obj)
            return TCalificacionDemandaSerializer(calificacion).data
        except TCalificacionDemanda.DoesNotExist:
            return None
        except AttributeError:
            return None
    
    def get_codigos_demanda(self, obj):
        codigos_demanda = TCodigoDemanda.objects.filter(demanda=obj)
        serialized_codigos = TCodigoDemandaSerializer(codigos_demanda.all(), many=True).data
        
        for codigo in serialized_codigos:
            tipo_codigo = TTipoCodigoDemanda.objects.get(id=codigo['tipo_codigo'])
            codigo['tipo_codigo_nombre'] = tipo_codigo.nombre
            codigo['tipo_codigo_datatype'] = tipo_codigo.datatype
        
        return serialized_codigos
    
    def get_localidad(self, obj):
        return TLocalidadSerializer(obj.localizacion.localidad).data if obj.localizacion else None
    
    def get_barrio(self, obj):
        return TBarrioSerializer(obj.localizacion.barrio).data if obj.localizacion else None
    
    def get_cpc(self, obj):
        return TCPCSerializer(obj.localizacion.cpc).data if obj.localizacion else None
    
    def get_demanda_zona(self, obj):
        demanda_zona = TDemandaZona.objects.filter(demanda=obj, esta_activo=True).last()
        return TDemandaZonaRegistroSerializer(demanda_zona).data if demanda_zona else None
    
    def get_calificacion_choices(self, obj):
        return TCalificacionDemanda.ESTADO_CALIFICACION_CHOICES

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


class RegistroDemandaFormDropdownsSerializer(serializers.Serializer):
    """Main serializer to group all dropdown data"""
    
    estado_demanda_choices = serializers.SerializerMethodField()
    envio_de_respuesta_choices = serializers.SerializerMethodField()
    tipo_demanda_choices = serializers.SerializerMethodField()
    tipo_calle_choices = serializers.SerializerMethodField()
    nacionalidad_choices = serializers.SerializerMethodField()
    situacion_dni_choices = serializers.SerializerMethodField()
    genero_choices = serializers.SerializerMethodField()
    nivel_alcanzado_choices = serializers.SerializerMethodField()
    ultimo_cursado_choices = serializers.SerializerMethodField()
    tipo_escuela_choices = serializers.SerializerMethodField()
    obra_social_choices = serializers.SerializerMethodField()
    intervencion_choices = serializers.SerializerMethodField()
    certificacion_choices = serializers.SerializerMethodField()
    beneficios_choices = serializers.SerializerMethodField()
    vinculo_demanda_choices = serializers.SerializerMethodField()

    bloques_datos_remitente = TBloqueDatosRemitenteSerializer(many=True)
    tipo_institucion_demanda = TTipoInstitucionDemandaSerializer(many=True)
    ambito_vulneracion = TAmbitoVulneracionSerializer(many=True)
    tipo_presunto_delito = TTipoPresuntoDelitoSerializer(many=True)
    institucion_demanda = TInstitucionDemandaSerializer(many=True)
    tipo_codigo_demanda = TTipoCodigoDemandaSerializer(many=True)
    
    localidad = TLocalidadSerializer(many=True)
    barrio = TBarrioSerializer(many=True)
    cpc = TCPCSerializer(many=True)
    
    vinculo_con_nnya_principal_choices = TVinculoDePersonasSerializer(many=True)
    institucion_educativa = TInstitucionEducativaSerializer(many=True)
    institucion_sanitaria = TInstitucionSanitariaSerializer(many=True)
    situacion_salud = TSituacionSaludSerializer(many=True)
    enfermedad = TEnfermedadSerializer(many=True)

    categoria_motivo = TCategoriaMotivoSerializer(many=True)
    categoria_submotivo = TCategoriaSubmotivoSerializer(many=True)
    gravedad_vulneracion = TGravedadVulneracionSerializer(many=True)
    urgencia_vulneracion = TUrgenciaVulneracionSerializer(many=True)
    condiciones_vulnerabilidad = TCondicionesVulnerabilidadSerializer(many=True)
    
    zonas = TZonaSerializer(many=True)

    class Meta:
        fields = '__all__'

    # 🔥 Optimized Choice Fields using SerializerMethodField
    def get_estado_demanda_choices(self, obj):
        return ChoiceFieldSerializer.from_model(TDemanda.ESTADO_DEMANDA_CHOICES)

    def get_envio_de_respuesta_choices(self, obj):
        return ChoiceFieldSerializer.from_model(TDemanda.ENVIO_DE_RESPUESTA_CHOICES)

    def get_tipo_demanda_choices(self, obj):
        return ChoiceFieldSerializer.from_model(TDemanda.TIPO_DEMANDA_CHOICES)

    def get_tipo_calle_choices(self, obj):
        return ChoiceFieldSerializer.from_model(TLocalizacion.TIPO_CALLE_CHOICES)

    def get_nacionalidad_choices(self, obj):
        return ChoiceFieldSerializer.from_model(TPersona.NACIONALIDAD_CHOICES)

    def get_situacion_dni_choices(self, obj):
        return ChoiceFieldSerializer.from_model(TPersona.SITUACION_DNI_CHOICES)

    def get_genero_choices(self, obj):
        return ChoiceFieldSerializer.from_model(TPersona.GENERO_CHOICES)

    def get_nivel_alcanzado_choices(self, obj):
        return ChoiceFieldSerializer.from_model(TEducacion.NIVEL_ALCANZADO_CHOICES)

    def get_ultimo_cursado_choices(self, obj):
        return ChoiceFieldSerializer.from_model(TEducacion.ULTIMO_CURSADO_CHOICES)

    def get_tipo_escuela_choices(self, obj):
        return ChoiceFieldSerializer.from_model(TEducacion.TIPO_ESCUELA_CHOICES)

    def get_obra_social_choices(self, obj):
        return ChoiceFieldSerializer.from_model(TCoberturaMedica.OBRA_SOCIAL_CHOICES)

    def get_intervencion_choices(self, obj):
        return ChoiceFieldSerializer.from_model(TCoberturaMedica.INTERVENCION_CHOICES)

    def get_certificacion_choices(self, obj):
        return ChoiceFieldSerializer.from_model(TPersonaEnfermedades.CERTIFICACION_CHOICES)

    def get_beneficios_choices(self, obj):
        return ChoiceFieldSerializer.from_model(TPersonaEnfermedades.BENEFICIOS_CHOICES)

    def get_vinculo_demanda_choices(self, obj):
        return ChoiceFieldSerializer.from_model(TDemandaPersona.VINCULO_DEMANDA_CHOICES)


class TVulneracionRegistroSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
    autordv_index = serializers.IntegerField(write_only=True, allow_null=True, required=False)
    
    class Meta:
        model = TVulneracion
        fields = '__all__'
        read_only_fields = ['sumatoria_de_pesos', 'nnya', 'deleted']


class TEducacionRegistroSerializer(serializers.ModelSerializer):
    institucion_educativa = TInstitucionEducativaSerializer()  # Nested Serializer
    id = serializers.IntegerField(required=False)

    class Meta:
        model = TEducacion
        read_only_fields = ['persona']
        fields = '__all__'

    def create(self, validated_data):
        """Handles creation of both TEducacion and new TInstitucionEducativa if provided"""
        institucion_data = validated_data.pop('institucion_educativa', None)
        validated_data['persona'] = self.context.get('persona')  # Get persona from context

        if institucion_data:
            institucion_educativa, created = TInstitucionEducativa.objects.get_or_create(**institucion_data)
            validated_data['institucion_educativa'] = institucion_educativa

        return TEducacion.objects.create(**validated_data)


class TCoberturaMedicaRegistroSerializer(serializers.ModelSerializer):
    institucion_sanitaria = TInstitucionSanitariaSerializer(required=False, allow_null=True)  # Nested Serializer
    medico_cabecera = TMedicoSerializer(required=False, allow_null=True)
    id = serializers.IntegerField(required=False)

    class Meta:
        model = TCoberturaMedica
        read_only_fields = ['persona']
        fields = '__all__'
    
    def create(self, validated_data):
        """Handles creation of both TCoberturaMedica and new TInstitucionSanitaria if provided"""
        institucion_data = validated_data.pop('institucion_sanitaria', None)
        medico_data = validated_data.pop('medico_cabecera', None)
        validated_data['persona'] = self.context.get('persona')  # Get persona from context

        if institucion_data:
            institucion_sanitaria, created = TInstitucionSanitaria.objects.get_or_create(**institucion_data)
            validated_data['institucion_sanitaria'] = institucion_sanitaria
        
        if medico_data:
            medico_cabecera, created = TMedico.objects.get_or_create(**medico_data)
            validated_data['medico_cabecera'] = medico_cabecera
        
        return TCoberturaMedica.objects.create(**validated_data)
    

class TPersonaEnfermedadesRegistroSerializer(serializers.ModelSerializer):
    oficio_adjunto = TPersonaOficioAdjuntoSerializer(many=True, required=False)
    certificado_adjunto = TPersonaCertificadoAdjuntoSerializer(many=True, required=False)

    enfermedad = TEnfermedadSerializer()
    institucion_sanitaria_interviniente = TInstitucionSanitariaSerializer(required=False, allow_null=True)
    medico_tratamiento = TMedicoSerializer(required=False, allow_null=True)
    id = serializers.IntegerField(required=False)

    class Meta:
        model = TPersonaEnfermedades
        read_only_fields = ['persona']
        fields = '__all__'

    def create(self, validated_data):
        """Handles creation of both TPersonaEnfermedades and new TEnfermedad if provided"""
        enfermedad_data = validated_data.pop('enfermedad', None)
        institucion_data = validated_data.pop('institucion_sanitaria_interviniente', None)
        medico_data = validated_data.pop('medico_tratamiento', None)
        validated_data['persona'] = self.context.get('persona')  # Get persona from context

        if enfermedad_data:
            enfermedad, created = TEnfermedad.objects.get_or_create(**enfermedad_data)
            validated_data['enfermedad'] = enfermedad
        
        if institucion_data:
            institucion_sanitaria, created = TInstitucionSanitaria.objects.get_or_create(**institucion_data)
            validated_data['institucion_sanitaria_interviniente'] = institucion_sanitaria
        
        if medico_data:
            medico_tratamiento, created = TMedico.objects.get_or_create(**medico_data)
            validated_data['medico_tratamiento'] = medico_tratamiento
        
        return TPersonaEnfermedades.objects.create(**validated_data)


class TDemandaPersonaRegistroSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
    class Meta:
        model = TDemandaPersona
        read_only_fields = ['demanda', 'persona']
        fields = '__all__'

    def create(self, validated_data):
        """Create and return a TDemandaPersona object"""
        validated_data['demanda'] = self.context.get('demanda')  # Get demanda from context
        validated_data['persona'] = self.context.get('persona')  # Get persona from context

        return TDemandaPersona.objects.create(**validated_data)


class PersonaRegistroSerializer(serializers.Serializer):
    localizacion = TLocalizacionSerializer(required=False, allow_null=True)
    educacion = TEducacionRegistroSerializer(required=False, allow_null=True)
    cobertura_medica = TCoberturaMedicaRegistroSerializer(required=False, allow_null=True)
    persona_enfermedades = TPersonaEnfermedadesRegistroSerializer(many=True, required=False)

    demanda_persona = TDemandaPersonaRegistroSerializer()
    use_demanda_localizacion = serializers.BooleanField(required=False, default=False)
    condiciones_vulnerabilidad = TPersonaCondicionesVulnerabilidadSerializer(many=True, required=False)
    persona = TPersonaSerializer()
    vulneraciones = TVulneracionRegistroSerializer(many=True, required=False)
    persona_id = serializers.IntegerField(required=False)
    
    def create(self, validated_data):
        """Create and return a Persona object"""
        condiciones_vulnerabilidad = validated_data.pop('condiciones_vulnerabilidad', [])
        localizacion_data = validated_data.pop('localizacion', None)
        educacion_data = validated_data.pop('educacion', None)
        cobertura_medica_data = validated_data.pop('cobertura_medica', None)
        persona_enfermedades_data = validated_data.pop('persona_enfermedades', [])
        demanda_persona_data = validated_data.pop('demanda_persona', None)
        vulneraciones_data = validated_data.pop('vulneraciones', [])
        
        # Get demanda from context
        demanda = self.context.get('demanda')

        # Create Persona
        persona_db = TPersona.objects.create(**validated_data)
        self.context['persona'] = persona_db
        self.context['personas_db'].append(persona_db)  # Store created personas to link them to demanda
        
        # Handle CondicionesVulnerabilidad
        for condicion in condiciones_vulnerabilidad:
            TPersonaCondicionesVulnerabilidad.objects.create(
                persona=persona_db,
                condicion_vulnerabilidad=condicion,
                demanda=demanda,
                si_no=True
            )

        # Handle Localizacion for Persona
        if self.validated_data.get('use_demanda_localizacion'):
            localizacion_persona = TLocalizacionPersona.objects.create(persona=persona_db, localizacion=demanda.localizacion)
        elif localizacion_data:
            new_localizacion, _ = TLocalizacion.objects.get_or_create(**localizacion_data)
            localizacion_persona = TLocalizacionPersona.objects.create(persona=persona_db, localizacion=new_localizacion)

        # Handle Educacion
        if educacion_data:
            educacion_serializer = TEducacionRegistroSerializer(data=educacion_data, context=self.context)
            print(f"Educacion data: {educacion_data}")
            educacion_serializer.is_valid(raise_exception=True)
            educacion_serializer.save(persona=persona_db)

        # Handle CoberturaMedica
        if cobertura_medica_data:
            cobertura_medica_serializer = TCoberturaMedicaRegistroSerializer(data=cobertura_medica_data, context=self.context)
            cobertura_medica_serializer.is_valid(raise_exception=True)
            cobertura_medica_serializer.save(persona=persona_db)

        # Handle Enfermedades
        for enfermedad_data in persona_enfermedades_data:
            print(f"Enfermedad data: {enfermedad_data}")
            enfermedad_serializer = TPersonaEnfermedadesRegistroSerializer(data=enfermedad_data, context=self.context)
            print(f"Enfermedad serializer: {enfermedad_serializer}")
            enfermedad_serializer.is_valid(raise_exception=True)
            print("Enfermedad serializer is valid")
            enfermedad_serializer.save(persona=persona_db)
        
        # Handle DemandaPersona
        if demanda_persona_data:
            demanda_persona_serializer = TDemandaPersonaRegistroSerializer(data=demanda_persona_data, context=self.context)
            demanda_persona_serializer.is_valid(raise_exception=True)
            demanda_persona_serializer.save()

        return persona_db


class TCodigoDemandaRegistroSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)

    class Meta:
        model = TCodigoDemanda
        read_only_fields = ['demanda']
        fields = '__all__'

    def create(self, validated_data):
        # Ensure 'demanda' is retrieved from the context
        demanda = self.context.get('demanda')
        if not demanda:
            raise serializers.ValidationError({"error": "Demanda must be provided in context but was missing."})

        # Assign demanda and create the object
        return TCodigoDemanda.objects.create(demanda=demanda, **validated_data)


class TDemandaZonaRegistroPOSTSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
    class Meta:
        model = TDemandaZona
        fields = '__all__'
        read_only_fields = ['demanda']

class RelacionDemandaSerializer(serializers.Serializer):
    codigos_demanda = TCodigoDemandaRegistroSerializer(many=True)
    demanda_zona = TDemandaZonaRegistroPOSTSerializer()



class RegistroDemandaFormSerializer(serializers.ModelSerializer):
    adjuntos=TDemandaAdjuntoSerializer(many=True, required=False)
    institucion = TInstitucionDemandaSerializer()
    relacion_demanda = RelacionDemandaSerializer(write_only=True)
    localizacion = TLocalizacionSerializer()
    personas = PersonaRegistroSerializer(many=True, required=False)

    class Meta:
        model = TDemanda
        fields = '__all__'

    def to_representation(self, instance):
        """Modify representation to include nested relationships for retrieval."""
        data = super().to_representation(instance)

        # Now "inject" your nested structure:
        data['relacion_demanda'] = {
            'codigos_demanda': TCodigoDemandaSerializer(
                TCodigoDemanda.objects.filter(demanda=instance), 
                many=True
            ).data,
            'demanda_zona': TDemandaZonaRegistroPOSTSerializer(
                TDemandaZona.objects.filter(
                    demanda=instance, 
                    esta_activo=True
                ).last()
            ).data
        }

        # You can also override your other fields if needed
        data['localizacion'] = TLocalizacionSerializer(instance.localizacion).data
        data['institucion'] = TInstitucionDemandaSerializer(instance.institucion).data if instance.institucion else None
        
        data['personas'] = []
        for demanda_persona in TDemandaPersona.objects.filter(demanda=instance, deleted=False):
            localizacion_persona = TLocalizacionPersona.objects.filter(persona=demanda_persona.persona).last()
            educacion = TEducacion.objects.filter(persona=demanda_persona.persona).last()
            cobertura_medica = TCoberturaMedica.objects.filter(persona=demanda_persona.persona).last()
            persona_enfermedades = TPersonaEnfermedades.objects.filter(persona=demanda_persona.persona)
            persona_condiciones_vulnerabilidad = TPersonaCondicionesVulnerabilidad.objects.filter(persona=demanda_persona.persona)
            persona_vulneraciones = TVulneracion.objects.filter(nnya=demanda_persona.persona)
            data['personas'].append(
                PersonaRegistroSerializer(
                    {
                        'persona': demanda_persona.persona,
                        'localizacion': localizacion_persona.localizacion if localizacion_persona else None,
                        'educacion': educacion if educacion else None,
                        'cobertura_medica': cobertura_medica if cobertura_medica else None,
                        'persona_enfermedades': persona_enfermedades if persona_enfermedades else [],
                        'demanda_persona': demanda_persona,
                        'condiciones_vulnerabilidad': persona_condiciones_vulnerabilidad if persona_condiciones_vulnerabilidad else [],
                        'vulneraciones': persona_vulneraciones if persona_vulneraciones else []
                    }
                ).data
            )

        print(f"Modified representation: {data}")

        return data


    def create(self, validated_data):
        """Create and return a TDemanda instance along with its related objects."""
        adjuntos_data = validated_data.pop('adjuntos', [])
        institucion_data = validated_data.pop('institucion')
        relacion_demanda_data = validated_data.pop('relacion_demanda')
        localizacion_data = validated_data.pop('localizacion')
        personas_data = validated_data.pop('personas', [])

        # Create or get InstitucionDemanda
        institucion, _ = TInstitucionDemanda.objects.get_or_create(**institucion_data)

        # Handle Localizacion (always create one for Demanda)
        localizacion = TLocalizacion.objects.create(**localizacion_data)

        # Create TDemanda instance
        demanda = TDemanda.objects.create(localizacion=localizacion, institucion=institucion, **validated_data)
        print(f"Created demanda: {demanda}")
        # Pass demanda as context to nested serializers
        self.context['demanda'] = demanda

        # Handle Adjuntos
        for adjunto_data in adjuntos_data:
            adjunto = TDemandaAdjunto.objects.create(demanda=demanda, **adjunto_data)
            print(f"Adjunto created: {adjunto}")

        self.context['personas_db'] = []  # Store created personas to link them to demanda
        self.context['vulneraciones_temp'] = []  # Store temporary vulneraciones to link them to a after created autordv
        # Handle Personas
        for persona_data in personas_data:
            print()
            persona = persona_data.pop('persona')
            localizacion = persona_data.pop('localizacion', None)
            educacion = persona_data.pop('educacion', None)
            cobertura_medica = persona_data.pop('cobertura_medica', None)
            persona_enfermedades = persona_data.pop('persona_enfermedades', [])
            
            use_demanda_localizacion = persona_data.pop('use_demanda_localizacion', False)
            demanda_persona = persona_data.pop('demanda_persona', None)
            vulneraciones = persona_data.pop('vulneraciones', [])
            condiciones_vulnerabilidad = persona_data.pop('condiciones_vulnerabilidad', [])
            print(f"Persona data: {persona_data}")
            
            persona_db = TPersona.objects.create(**persona)
            self.context['persona'] = persona_db
            self.context['personas_db'].append(persona_db)
            
            if use_demanda_localizacion:
                localizacion_persona = TLocalizacionPersona.objects.create(persona=persona_db, localizacion=demanda.localizacion)
                print(f"Localizacion created: {localizacion_persona}")
            elif localizacion:
                new_localizacion, _ = TLocalizacion.objects.get_or_create(**localizacion)
                localizacion_persona = TLocalizacionPersona.objects.create(persona=persona_db, localizacion=new_localizacion)
            
                print(f"Localizacion created: {localizacion_persona}")
            
            if educacion:
                institucion_educativa = educacion.get('institucion_educativa', None)
                if institucion_educativa:
                    institucion_educativa, _ = TInstitucionEducativa.objects.get_or_create(**educacion.pop('institucion_educativa'))
                    educacion['institucion_educativa'] = institucion_educativa
                educacion, _ = TEducacion.objects.get_or_create(persona=persona_db, **educacion)
            
                print(f"Educacion created: {educacion}")
            
            if cobertura_medica:

                institucion_sanitaria = cobertura_medica.get('institucion_sanitaria', None)
                if institucion_sanitaria:
                    institucion_sanitaria, _ = TInstitucionSanitaria.objects.get_or_create(**institucion_sanitaria)
                    cobertura_medica['institucion_sanitaria'] = institucion_sanitaria
                medico_cabecera = cobertura_medica.get('medico_cabecera', None)
                if medico_cabecera:
                    medico_cabecera, _ = TMedico.objects.get_or_create(**medico_cabecera)
                    cobertura_medica['medico_cabecera'] = medico_cabecera
                cobertura_medica, _ = TCoberturaMedica.objects.get_or_create(persona=persona_db, **cobertura_medica)
            
                print(f"CoberturaMedica created: {cobertura_medica}")
            
            for enfermedad_data in persona_enfermedades:

                enfermedad = enfermedad_data.get('enfermedad', None)
                oficios_adjuntos_data = enfermedad_data.pop('oficio_adjunto', [])
                certificados_adjuntos_data = enfermedad_data.pop('certificado_adjunto', [])
                if enfermedad:
                    enfermedad, _ = TEnfermedad.objects.get_or_create(**enfermedad_data.pop('enfermedad'))
                    enfermedad_data['enfermedad'] = enfermedad
                institucion_sanitaria = enfermedad_data.get('institucion_sanitaria_interviniente', None)
                if institucion_sanitaria:
                    institucion_sanitaria, _ = TInstitucionSanitaria.objects.get_or_create(**enfermedad_data.pop('institucion_sanitaria_interviniente'))
                    enfermedad_data['institucion_sanitaria_interviniente'] = institucion_sanitaria
                medico_tratamiento = enfermedad_data.get('medico_tratamiento', None)
                if medico_tratamiento:
                    medico_tratamiento, _ = TMedico.objects.get_or_create(**enfermedad_data.pop('medico_tratamiento'))
                    enfermedad_data['medico_tratamiento'] = medico_tratamiento

                persona_enfermedad, _ = TPersonaEnfermedades.objects.get_or_create(persona=persona_db, **enfermedad_data)
                print(f"Enfermedad created: {persona_enfermedad}")
                
                for oficio_adjunto_data in oficios_adjuntos_data:
                    oficio = TPersonaOficioAdjunto.objects.create(persona_enfermedades=persona_enfermedad, **oficio_adjunto_data)
                    print(f"Oficio created: {oficio}")
                for certificado_adjunto_data in certificados_adjuntos_data:
                    certificado = TPersonaCertificadoAdjunto.objects.create(persona_enfermedades=persona_enfermedad, **certificado_adjunto_data)
                    print(f"Certificado created: {certificado}")

            if demanda_persona:
                demanda_persona['demanda'] = demanda
                demanda_persona['persona'] = persona_db
                demanda_persona = TDemandaPersona.objects.create(**demanda_persona)

                print(f"DemandaPersona created: {demanda_persona}")
            
            for condicion in condiciones_vulnerabilidad:
                TPersonaCondicionesVulnerabilidad.objects.create(
                    persona=persona_db,
                    demanda=demanda,
                    **condicion
                )
            
            for vulneracion in vulneraciones:
                vulneracion['nnya'] = persona_db
                vulneracion['demanda'] = demanda
                self.context['vulneraciones_temp'].append(vulneracion)
            
        print(f"Vulneraciones Temporales: {self.context['vulneraciones_temp']}")
        for vulneracion in self.context['vulneraciones_temp']:
            autordv_index = vulneracion.pop('autordv_index', None)
            if autordv_index is not None:
                autordv = self.context['personas_db'][autordv_index]
                vulneracion['autordv'] = autordv
            vulneracion_db = TVulneracion.objects.create(**vulneracion)
            print(f"Vulneracion created: {vulneracion_db}")

        print(f"Personas created: {self.context['personas_db']}")

        demanda_zona_data = relacion_demanda_data.pop('demanda_zona', None)
        demanda_zona_data['demanda'] = demanda
        demanda_zona = TDemandaZona.objects.create(**demanda_zona_data)
        print(f"Created demanda_zona: {demanda_zona}")

        codigos_data = relacion_demanda_data.pop('codigos_demanda', [])
        # Handle CodigosDemanda (without requiring `demanda` in request)
        for codigo_data in codigos_data:
            codigo, _ = TCodigoDemanda.objects.get_or_create(demanda=demanda, **codigo_data)
            print(f"Created codigo: {codigo}")

        return demanda


    def update(self, instance, validated_data):
        adjuntos_data = validated_data.pop('adjuntos', [])
        localizacion_data = validated_data.pop('localizacion', None)
        institucion_data = validated_data.pop('institucion', None)
        relacion_demanda_data = validated_data.pop('relacion_demanda', None)
        personas_data = validated_data.pop('personas', [])

        if localizacion_data:
            for attr, value in localizacion_data.items():
                setattr(instance.localizacion, attr, value)
            instance.localizacion.save()
        
        print(f"Institucion data: {institucion_data}")
        if institucion_data:
            institucion, _ = TInstitucionDemanda.objects.get_or_create(**institucion_data)
            instance.institucion = institucion

        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        # Handle Adjuntos
        for adjunto_data in adjuntos_data:
            adjunto = TDemandaAdjunto.objects.get_or_create(demanda=instance, **adjunto_data)
            print(f"Adjunto created: {adjunto}")

        if relacion_demanda_data:
            codigos_data = relacion_demanda_data.pop('codigos_demanda', [])
            for codigo_data in codigos_data:
                codigo_id = codigo_data.get('id', None)
                if 'id' in codigo_data:
                    # Update existing
                    codigo = TCodigoDemanda.objects.get(pk=codigo_data['id'])
                    for attr, value in codigo_data.items():
                        setattr(codigo, attr, value)
                    codigo.save()
                else:
                    # Create new
                    codigo, _ = TCodigoDemanda.objects.get_or_create(
                        demanda=instance,
                        **codigo_data
                    )
            demanda_zona_data = relacion_demanda_data.pop('demanda_zona', None)
            if demanda_zona_data:
                demanda_zona_id = demanda_zona_data.get('id', None)
                if demanda_zona_id:
                    demanda_zona = TDemandaZona.objects.get(pk=demanda_zona_id)
                    for attr, value in demanda_zona_data.items():
                        setattr(demanda_zona, attr, value)
                    demanda_zona.save()
                else:
                    demanda_zona = TDemandaZona.objects.create(demanda=instance, **demanda_zona_data)
        
        self.context['personas_db'] = []  # Store created personas to link them to demanda
        self.context['vulneraciones_temp'] = []  # Store temporary vulneraciones to link them to a after created autordv
        # Handle Personas
        print(f"Personas data: {personas_data}")
        for persona_data in personas_data:
            persona_id = persona_data.pop('persona_id', None)
            persona = persona_data.pop('persona', None)
            localizacion = persona_data.pop('localizacion', None)
            educacion = persona_data.pop('educacion', None)
            cobertura_medica = persona_data.pop('cobertura_medica', None)
            persona_enfermedades = persona_data.pop('persona_enfermedades', [])
            
            use_demanda_localizacion = persona_data.pop('use_demanda_localizacion', False)
            demanda_persona = persona_data.pop('demanda_persona', None)
            vulneraciones = persona_data.pop('vulneraciones', [])
            condiciones_vulnerabilidad = persona_data.pop('condiciones_vulnerabilidad', [])
            
            print(f"Persona data: {persona}")
            if persona_id:
                persona_db = TPersona.objects.get(pk=persona_id)
                if persona:
                    for attr, value in persona.items():
                        setattr(persona_db, attr, value)
                    persona_db.save()
            else:
                persona_db = TPersona.objects.create(**persona)
            self.context['persona'] = persona_db
            self.context['personas_db'].append(persona_db)
            
            if use_demanda_localizacion:
                localizacion_persona, _ = TLocalizacionPersona.objects.get_or_create(persona=persona_db, localizacion=instance.localizacion)
                print(f"Localizacion created: {localizacion_persona}")
            elif localizacion:
                localizacion_id = localizacion.get('id', None)
                if localizacion_id:
                    localizacion_db = TLocalizacion.objects.get(pk=localizacion_id)
                    for attr, value in localizacion.items():
                        setattr(localizacion_db, attr, value)
                    localizacion_db.save()
                else:
                    localizacion_db = TLocalizacion.objects.create(**localizacion)
                    localizacion_persona_db = TLocalizacionPersona.objects.create(persona=persona_db, localizacion=localizacion_db)

                print(f"Localizacion created: {localizacion_db}")
            
            if educacion:
                institucion_educativa = educacion.get('institucion_educativa', None)
                if institucion_educativa:
                    institucion_educativa, _ = TInstitucionEducativa.objects.get_or_create(**educacion.pop('institucion_educativa'))
                    educacion['institucion_educativa'] = institucion_educativa
    
                educacion_id = educacion.pop('id', None)
                if educacion_id:
                    educacion_db = TEducacion.objects.get(pk=educacion_id)
                    if educacion:
                        for attr, value in educacion.items():
                            setattr(educacion_db, attr, value)
                        educacion_db.save()
                        print(f"Educacion modified: {educacion_db}")
                else:
                    print(f"Educacion data: {educacion}")
                    educacion_db = TEducacion.objects.create(persona=persona_db, **educacion)
                
                    print(f"Educacion created: {educacion_db}")
                
            if cobertura_medica:
                institucion_sanitaria = cobertura_medica.get('institucion_sanitaria', None)
                if institucion_sanitaria:
                    institucion_sanitaria, _ = TInstitucionSanitaria.objects.get_or_create(**institucion_sanitaria)
                    cobertura_medica['institucion_sanitaria'] = institucion_sanitaria
                
                medico_cabecera = cobertura_medica.get('medico_cabecera', None)
                if medico_cabecera:
                    medico_cabecera, _ = TMedico.objects.get_or_create(**medico_cabecera)
                    cobertura_medica['medico_cabecera'] = medico_cabecera
                
                cobertura_medica_id = cobertura_medica.pop('id', None)    
                if cobertura_medica_id:
                    cobertura_medica_db = TCoberturaMedica.objects.get(pk=cobertura_medica_id)
                    if cobertura_medica:
                        for attr, value in cobertura_medica.items():
                            setattr(cobertura_medica_db, attr, value)
                        cobertura_medica_db.save()
                else:
                    cobertura_medica_db = TCoberturaMedica.objects.create(persona=persona_db, **cobertura_medica)
                
                print(f"CoberturaMedica created: {cobertura_medica_db}")
            
            for enfermedad_data in persona_enfermedades:
                enfermedad_id = enfermedad_data.pop('id', None)
                enfermedad = enfermedad_data.get('enfermedad', None)
                institucion_sanitaria = enfermedad_data.get('institucion_sanitaria_interviniente', None)
                medico_tratamiento = enfermedad_data.get('medico_tratamiento', None)
                oficios_adjuntos_data = enfermedad_data.pop('oficio_adjunto', [])
                certificados_adjuntos_data = enfermedad_data.pop('certificado_adjunto', [])
                if enfermedad:
                    enfermedad, _ = TEnfermedad.objects.get_or_create(**enfermedad)
                    enfermedad_data['enfermedad'] = enfermedad
                if institucion_sanitaria:
                    institucion_sanitaria, _ = TInstitucionSanitaria.objects.get_or_create(**institucion_sanitaria)
                    enfermedad_data['institucion_sanitaria_interviniente'] = institucion_sanitaria
                if medico_tratamiento:
                    medico_tratamiento, _ = TMedico.objects.get_or_create(**medico_tratamiento)
                    enfermedad_data['medico_tratamiento'] = medico_tratamiento
                
                if enfermedad_id:
                    persona_enfermedad_db = TPersonaEnfermedades.objects.get(pk=enfermedad_id)
                    if enfermedad_data:
                        for attr, value in enfermedad_data.items():
                            setattr(persona_enfermedad_db, attr, value)
                        persona_enfermedad_db.save()
                else:
                    persona_enfermedad_db= TPersonaEnfermedades.objects.create(persona=persona_db, **enfermedad_data)

                print(f"Enfermedad created: {persona_enfermedad_db}")
                
                for oficio_adjunto_data in oficios_adjuntos_data:
                    oficio = TPersonaOficioAdjunto.objects.get_or_create(persona_enfermedades=persona_enfermedad_db, **oficio_adjunto_data)
                    print(f"Oficio created: {oficio}")
                for certificado_adjunto_data in certificados_adjuntos_data:
                    certificado = TPersonaCertificadoAdjunto.objects.get_or_create(persona_enfermedades=persona_enfermedad_db, **certificado_adjunto_data)
                    print(f"Certificado created: {certificado}")
            
            if demanda_persona:
                demanda_persona_id = demanda_persona.pop('id', None)
                demanda_persona['demanda'] = instance
                demanda_persona['persona'] = persona_db
                if demanda_persona_id:
                    demanda_persona_db = TDemandaPersona.objects.get(pk=demanda_persona_id)
                    if demanda_persona:
                        for attr, value in demanda_persona.items():
                            setattr(demanda_persona_db, attr, value)
                        demanda_persona_db.save()
                else:
                    demanda_persona_db = TDemandaPersona.objects.create(**demanda_persona)
                
                print(f"DemandaPersona created: {demanda_persona_db}")
            
            for condicion in condiciones_vulnerabilidad:
                condicion_id = condicion.pop('id', None)
                condicion['persona'] = persona_db
                condicion['demanda'] = instance
                if condicion_id:
                    condicion_db = TPersonaCondicionesVulnerabilidad.objects.get(pk=condicion_id)
                    if condicion:
                        for attr, value in condicion.items():
                            setattr(condicion_db, attr, value)
                        condicion_db.save()
                else:
                    TPersonaCondicionesVulnerabilidad.objects.create(**condicion)

                print(f"Condicion created: {condicion}")
            
            for vulneracion in vulneraciones:
                vulneracion['nnya'] = persona_db
                vulneracion['demanda'] = instance
                self.context['vulneraciones_temp'].append(vulneracion)
            
        print(f"Vulneraciones Temporales: {self.context['vulneraciones_temp']}")
        for vulneracion in self.context['vulneraciones_temp']:
            autordv_index = vulneracion.pop('autordv_index', None)
            if autordv_index:
                autordv = self.context['personas_db'][autordv_index]
                vulneracion['autordv'] = autordv
            vulneracion_id = vulneracion.pop('id', None)
            if vulneracion_id:
                vulneracion_db = TVulneracion.objects.get(pk=vulneracion_id)
                if vulneracion:
                    for attr, value in vulneracion.items():
                        setattr(vulneracion_db, attr, value)
                    vulneracion_db.save()
            else:
                TVulneracion.objects.create(**vulneracion)
        
        print(f"Personas created: {self.context['personas_db']}")

        instance.save()
        return instance
