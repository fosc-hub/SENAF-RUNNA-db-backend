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
)
from api.serializers import (
    TBloqueDatosRemitenteSerializer,
    TTipoInstitucionDemandaSerializer,
    TAmbitoVulneracionSerializer,
    TTipoPresuntoDelitoSerializer,
    TInstitucionDemandaSerializer,
    TDemandaSerializer,
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
)


class MesaDeEntradaSerializer(serializers.ModelSerializer):
    demanda_score = serializers.SerializerMethodField()
    bloque_datos_remitente = serializers.SerializerMethodField()
    nnya_principal = serializers.SerializerMethodField()
    calificacion = serializers.SerializerMethodField()
    codigos_demanda = serializers.SerializerMethodField()
    localidad = serializers.SerializerMethodField()
    barrio = serializers.SerializerMethodField()
    cpc = serializers.SerializerMethodField()
    zona_asignada = serializers.SerializerMethodField()
    registrado_por_user = serializers.SerializerMethodField()
    registrado_por_user_zona = serializers.SerializerMethodField()
    user_responsable = serializers.SerializerMethodField()

    def get_demanda_score(self, obj):
        try:
            score = TDemandaScore.objects.get(demanda=obj)
            return TDemandaScoreSerializer(score).data
        except TDemandaScore.DoesNotExist:
            return None

    def get_bloque_datos_remitente(self, obj):
        return TBloqueDatosRemitenteSerializer(obj.bloque_datos_remitente).data if obj.bloque_datos_remitente else None

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
        return TCodigoDemandaSerializer(codigos_demanda.all(), many=True).data
    
    def get_localidad(self, obj):
        return TLocalidadSerializer(obj.localizacion.localidad).data if obj.localizacion else None
    
    def get_barrio(self, obj):
        return TBarrioSerializer(obj.localizacion.barrio).data if obj.localizacion else None
    
    def get_cpc(self, obj):
        return TCPCSerializer(obj.localizacion.cpc).data if obj.localizacion else None
    
    def get_zona_asignada(self, obj):
        return TZonaSerializer(obj.zona_asignada).data if obj.zona_asignada else None
    
    def get_registrado_por_user(self, obj):
        return CustomUserSerializer(obj.registrado_por_user).data if obj.registrado_por_user else None
    
    def get_registrado_por_user_zona(self, obj):
        return TZonaSerializer(obj.registrado_por_user_zona).data if obj.registrado_por_user_zona else None

    def get_user_responsable(self, obj):
        return CustomUserSerializer(obj.user_responsable).data if obj.user_responsable else None

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
    autordv_index = serializers.IntegerField(write_only=True, allow_null=False)
    
    class Meta:
        model = TVulneracion
        fields = '__all__'
        read_only_fields = ['sumatoria_de_pesos', 'nnya', 'deleted']


class TEducacionRegistroSerializer(serializers.ModelSerializer):
    institucion_educativa = TInstitucionEducativaSerializer()  # Nested Serializer

    class Meta:
        model = TEducacion
        read_only_fields = ['persona']
        fields = '__all__'
    
    def to_internal_value(self, data):
        """Remove `persona` from validation to allow deferred assignment"""
        data = data.copy()
        data.pop('persona', None)  # Prevents validation from requiring `persona`
        return super().to_internal_value(data)

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
    enfermedad = TEnfermedadSerializer()
    institucion_sanitaria_interviniente = TInstitucionSanitariaSerializer(required=False, allow_null=True)
    medico_tratamiento = TMedicoSerializer(required=False, allow_null=True)

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
    cobertura_medica = TCoberturaMedicaSerializer(required=False, allow_null=True)
    persona_enfermedades = TPersonaEnfermedadesRegistroSerializer(many=True, required=False)

    demanda_persona = TDemandaPersonaSerializer()
    use_demanda_localizacion = serializers.BooleanField(required=False, default=False)
    condiciones_vulnerabilidad = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=TCondicionesVulnerabilidad.objects.all(),  # Ensure only valid IDs are accepted
        required=False
    )
    vulneraciones = TVulneracionRegistroSerializer(many=True, required=False)
    
    class Meta:
        model = TPersona
        fields = '__all__'
    
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
            educacion_serializer.is_valid(raise_exception=True)
            educacion_serializer.save(persona=persona_db)

        # Handle CoberturaMedica
        if cobertura_medica_data:
            cobertura_medica_serializer = TCoberturaMedicaRegistroSerializer(data=cobertura_medica_data, context=self.context)
            cobertura_medica_serializer.is_valid(raise_exception=True)
            cobertura_medica_serializer.save(persona=persona_db)

        # Handle Enfermedades
        for enfermedad_data in persona_enfermedades_data:
            enfermedad_serializer = TPersonaEnfermedadesRegistroSerializer(data=enfermedad_data, context=self.context)
            enfermedad_serializer.is_valid(raise_exception=True)
            enfermedad_serializer.save(persona=persona_db)
        
        # Handle DemandaPersona
        if demanda_persona_data:
            demanda_persona_serializer = TDemandaPersonaRegistroSerializer(data=demanda_persona_data, context=self.context)
            demanda_persona_serializer.is_valid(raise_exception=True)
            demanda_persona_serializer.save()

        return persona_db

class TCodigoDemandaRegistroSerializer(serializers.ModelSerializer):
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


class RegistroDemandaFormSerializer(serializers.ModelSerializer):
    institucion_demanda = TInstitucionDemandaSerializer()
    codigos_demanda = TCodigoDemandaRegistroSerializer(many=True)
    localizacion = TLocalizacionSerializer()
    personas = PersonaRegistroSerializer(many=True, required=False)

    class Meta:
        model = TDemanda
        fields = '__all__'
        
    def to_representation(self, instance):
        """Modify representation to include nested relationships for retrieval."""
        data = super().to_representation(instance)

        # Serialize Localizacion and Informante
        data['localizacion'] = TLocalizacionSerializer(instance.localizacion).data

        return data


    def create(self, validated_data):
        """Create and return a TDemanda instance along with its related objects."""
        institucion_data = validated_data.pop('institucion_demanda')
        codigos_data = validated_data.pop('codigos_demanda')
        localizacion_data = validated_data.pop('localizacion')
        personas_data = validated_data.pop('personas', [])

        # Create or get InstitucionDemanda
        institucion_demanda, _ = TInstitucionDemanda.objects.get_or_create(**institucion_data)

        # Handle Localizacion (always create one for Demanda)
        localizacion = TLocalizacion.objects.create(**localizacion_data)

        # Create TDemanda instance
        demanda = TDemanda.objects.create(localizacion=localizacion, institucion=institucion_demanda, **validated_data)
        print(f"Created demanda: {demanda}")
        # Pass demanda as context to nested serializers
        self.context['demanda'] = demanda

        # Handle CodigosDemanda (without requiring `demanda` in request)
        for codigo_data in codigos_data:
            codigo_serializer = TCodigoDemandaRegistroSerializer(data=codigo_data, context=self.context)
            print(f"Creating codigo with data: {codigo_data}")
            print(f"Context: {self.context}")
            codigo_serializer.is_valid(raise_exception=True)
            print(f"Validated data: {codigo_serializer.validated_data}")
            codigo_serializer.save()  # demanda is assigned automatically

        self.context['personas_db'] = []  # Store created personas to link them to demanda
        # Handle Personas
        for persona_data in personas_data:
            persona_serializer = PersonaRegistroSerializer(data=persona_data, context=self.context)
            persona_serializer.is_valid(raise_exception=True)
            persona_db = persona_serializer.save()
            self.context['personas_db'].append(persona_db)  # Store created personas to link them to demanda
        
        print(f"Personas created: {self.context['personas_db']}")

        return demanda

    def update(self, instance, validated_data):
        localizacion_data = validated_data.pop('localizacion', None)
        informante = validated_data.pop('informante', None)

        if localizacion_data:
            for attr, value in localizacion_data.items():
                setattr(instance.localizacion, attr, value)
            instance.localizacion.save()

        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        
        instance.save()
        return instance
