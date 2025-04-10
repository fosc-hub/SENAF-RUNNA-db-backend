from datetime import datetime, date
from django.db import models
from simple_history.models import HistoricalRecords
from django.utils.translation import gettext_lazy as _
from .BaseClass import BaseHistory, BaseAdjunto

class TBloqueDatosRemitente(models.Model):
    nombre = models.CharField(max_length=255, null=False, blank=False)

    class Meta:
        app_label = 'infrastructure'
        verbose_name = _('Bloque de Datos Remitente, Origen de Demanda')
        verbose_name_plural = _('Bloques de Datos Remitentes, Origenes de Demandas')
        
    def __str__(self):
        return f"{self.nombre}"


class TTipoInstitucionDemanda(models.Model):
    nombre = models.CharField(max_length=255, null=False, blank=False)
    bloque_datos_remitente = models.ForeignKey('TBloqueDatosRemitente', on_delete=models.CASCADE, null=False)

    class Meta:
        app_label = 'infrastructure'
        verbose_name = _('Tipos de instituciones de demanda, Sub-Origen de Demanda')
        verbose_name_plural = _('Tipos de instituciones de demanda, Sub-Origenes de Demandas')
        
    def __str__(self):
        return f"{self.nombre} - {self.bloque_datos_remitente}"

class TAmbitoVulneracion(models.Model):
    nombre = models.CharField(max_length=255, null=False, blank=False)

    class Meta:
        app_label = 'infrastructure'
        verbose_name = _('Ambito de Vulneracion')
        verbose_name_plural = _('Ambitos de Vulneracion')

    def __str__(self):
        return f"{self.nombre}"


class TInstitucionDemanda(models.Model):
    nombre = models.CharField(max_length=255, null=False, blank=False)
    tipo_institucion = models.ForeignKey('TTipoInstitucionDemanda', on_delete=models.CASCADE, null=False)

    class Meta:
        app_label = 'infrastructure'
        verbose_name = _('Institucion de Demanda')
        verbose_name_plural = _('Instituciones de Demanda')

    def __str__(self):
        return f"{self.nombre} - {self.tipo_institucion}"


class TDemandaBase(models.Model):
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    ultima_actualizacion = models.DateTimeField(auto_now=True)
    fecha_ingreso_senaf = models.DateField(null=False)
    fecha_oficio_documento = models.DateField(null=False)
    descripcion = models.TextField(null=True, blank=True)
    
    OBJETIVO_DE_DEMANDA_CHOICES = [
        ('PROTECCION', 'Protección'),
        ('PETICION_DE_INFORME', 'Petición de Informe'),
    ]
    objetivo_de_demanda = models.CharField(max_length=30, choices=OBJETIVO_DE_DEMANDA_CHOICES, default='PROTECCION', null=False, blank=False)

    ESTADO_DEMANDA_CHOICES = [
        ('SIN_ASIGNAR', 'Sin Asignar'),
        ('CONSTATACION', 'Constatacion'),
        ('EVALUACION', 'Evaluacion'),
        ('PENDIENTE_AUTORIZACION', 'Pendiente Autorizacion'),
        ('ARCHIVADA', 'Archivada'),
        ('ADMITIDA', 'Admitida'),
        ('INFORME_SIN_ENVIAR', 'Informe Sin Enviar'),
        ('INFORME_ENVIADO', 'Informe Enviado'),
    ]
    estado_demanda = models.CharField(max_length=30, choices=ESTADO_DEMANDA_CHOICES, null=False, blank=False, default='SIN_ASIGNAR')
    
    observaciones = models.TextField(null=True, blank=True, help_text="Observaciones sobre los niños, adultos, cantidad de personas, etc.")
    
    ENVIO_DE_RESPUESTA_CHOICES = [
        ('NO_NECESARIO', 'No Necesario'),
        ('PENDIENTE', 'Pendiente'),
        ('ENVIADO', 'Enviado')
    ]
    envio_de_respuesta = models.CharField(max_length=20, choices=ENVIO_DE_RESPUESTA_CHOICES, null=False, blank=False, default='NO_NECESARIO')

    etiqueta = models.ForeignKey('TRespuestaEtiqueta', on_delete=models.SET_NULL, null=True, blank=True)

    localizacion = models.ForeignKey('TLocalizacion', on_delete=models.PROTECT, null=False)

    ambito_vulneracion = models.ForeignKey('TAmbitoVulneracion', on_delete=models.PROTECT, null=True, blank=True)

    bloque_datos_remitente = models.ForeignKey('TBloqueDatosRemitente', on_delete=models.PROTECT, null=False)
    tipo_institucion = models.ForeignKey('TTipoInstitucionDemanda', on_delete=models.PROTECT, null=True, blank=True)
    institucion = models.ForeignKey('TInstitucionDemanda', on_delete=models.PROTECT, null=True, blank=True)

    motivo_ingreso = models.ForeignKey('TCategoriaMotivo', on_delete=models.PROTECT, null=True, blank=True)
    submotivo_ingreso = models.ForeignKey('TCategoriaSubmotivo', on_delete=models.PROTECT, null=True, blank=True)

    registrado_por_user = models.ForeignKey('customAuth.CustomUser', related_name="%(class)sregistrado_por_user", on_delete=models.PROTECT, null=True, blank=True)
    registrado_por_user_zona = models.ForeignKey('customAuth.TZona', related_name="%(class)sregistrado_por_user_zona", on_delete=models.PROTECT, null=True, blank=True)

    class Meta:
        abstract = True


class TDemanda(TDemandaBase):

    def delete(self, *args, **kwargs):
        """Override delete to implement soft delete."""
        self.archivado = True
        self.save()

    def hard_delete(self, *args, **kwargs):
        """Permanently delete the object."""
        super().delete(*args, **kwargs)

    class Meta:
        app_label = 'infrastructure'
        verbose_name = _('Demanda')
        verbose_name_plural = _('Demandas')

    def __str__(self):
        return f"{self.id} {self.bloque_datos_remitente} - {self.descripcion} - {self.fecha_creacion}"
    
    # def save(self, *args, **kwargs):
    #     if not self.pk:  # onCreate
            
    #         if self.tipo_demanda == 'DE_PROTECCION':
    #             if not self.ambito_vulneracion:
    #                 raise ValueError("El ambito de vulneracion es obligatorio para una demanda de proteccion")
    #             if self.tipos_presuntos_delitos:
    #                 raise ValueError("El tipo de presunto delito debe ser None para una demanda de proteccion")

    #         if self.tipo_demanda == 'PENAL_JUVENIL':
    #             if not self.tipos_presuntos_delitos:
    #                 raise ValueError("El tipo de presunto delito es obligatorio para una demanda penal juvenil")
            
    #         if self.tipo_institucion:
    #             if self.bloque_datos_remitente != self.tipo_institucion.bloque_datos_remitente:
    #                 raise ValueError("El bloque de datos del remitente debe ser el mismo que el del tipo de institucion")
            
    #         if self.submotivo_ingreso:
    #             if self.motivo_ingreso != self.submotivo_ingreso.motivo:
    #                 raise ValueError("El motivo de ingreso debe ser el mismo que el del submotivo de ingreso")
        
    #     else:  # onUpdate
    #         if self.user_responsable.zona != self.zona_asignada:
    #             if self.user != self.user_responsable:
    #                 raise ValueError("El usuario asignado debe ser de la misma zona que la demanda")
        
    #     super().save(*args, **kwargs)


class TDemandaHistory(TDemandaBase, BaseHistory):
    parent = models.ForeignKey(
        'infrastructure.TDemanda',
        on_delete=models.CASCADE,
        related_name='history'
    )

    class Meta:
        app_label = 'infrastructure'
        verbose_name = _('Historial de Demanda')
        verbose_name_plural = _('Historial de Demandas')

class TDemandaAdjunto(BaseAdjunto):
    demanda = models.ForeignKey(
        'TDemanda', 
        on_delete=models.CASCADE, 
        null=False,
        related_name='adjuntos'
    )

    class Meta:
        app_label = 'infrastructure'
        verbose_name = _('Adjunto de Demanda')
        verbose_name_plural = _('Adjuntos de Demandas')

    def __str__(self):
        return f"{self.demanda} - {self.archivo}"

class TTipoCodigoDemanda(models.Model):
    nombre = models.CharField(max_length=255, null=False, blank=False)
    datatype_choices = [
        ('INT', 'Integer'),
        ('STRING', 'String')
    ]
    datatype = models.CharField(max_length=10, choices=datatype_choices, null=False, blank=False)
    
    bloque_datos_remitente = models.ForeignKey('TBloqueDatosRemitente', on_delete=models.CASCADE, null=True)

    class Meta:
        app_label = 'infrastructure'
        verbose_name = _('Tipo de Codigo de Demanda')
        verbose_name_plural = _('Tipos de Codigos de Demanda')

    def __str__(self):
        return f"{self.nombre} - {self.datatype} - {self.bloque_datos_remitente}"


class TCodigoDemanda(models.Model):
    codigo = models.CharField(max_length=255, null=False, blank=False)
    tipo_codigo = models.ForeignKey('TTipoCodigoDemanda', on_delete=models.PROTECT, null=False)
    demanda = models.ForeignKey('TDemanda', on_delete=models.CASCADE, null=False)

    class Meta:
        app_label = 'infrastructure'
        verbose_name = _('Codigo de Demanda')
        verbose_name_plural = _('Codigos de Demanda')

    # def save(self, *args, **kwargs):
    #     if self.tipo_codigo.datatype == 'INT':
    #         if not self.codigo.isdigit():
    #             raise ValueError("El código debe ser un número")
    #     elif self.tipo_codigo.datatype == 'STRING':
    #         if not self.codigo.isalpha():
    #             raise ValueError("El código debe ser una cadena de texto")
    #     super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.codigo} - {self.tipo_codigo} - {self.demanda}"


class TCalificacionDemandaBase(models.Model):
    fecha_y_hora_creacion = models.DateTimeField(auto_now_add=True)
    justificacion = models.TextField(null=False, blank=False)

    ESTADO_CALIFICACION_CHOICES = [
        ('PERTINENTE_CONSTATACION_URGENTE', 'Pertinente de Constatación Urgente'),
        ('PERTINENTE_CONSTATACION_NO_URGENTE', 'Pertinente de Constatación No Urgente'),
        ('NO_PERTINENTE_NO_CORRESPONDE', 'No Pertinente - No corresponde al 2do o 3er nivel del sistema de protección'),
        ('NO_PERTINENTE_INCOMPETENCIA', 'No Pertinente - Incompetencia material o territorial'),
        ('NO_PERTINENTE_OFICIOS_INCOMPLETOS', 'No Pertinente - Oficios incompletos o con error'),
        ('NO_PERTINENTE_NO_CORRESPONDE_LEY', 'No Pertinente - No corresponde a la Ley 9944'),
        ('PASA_A_LEGAJO', 'Pasa Directo al Legajo Sin Proceso de Admisión (demandas DE MPJ O MPI/MPE ABIERTAS/VIGENTES)'),
        ('NO_PERTINENTE_NO_VERACIDAD', 'No Pertinente - No se constata la veracidad de la demanda'),
    ]
    estado_calificacion = models.CharField(max_length=50, choices=ESTADO_CALIFICACION_CHOICES, null=False, blank=False)
    ultima_actualizacion = models.DateTimeField(auto_now=True)
    
    demanda = models.OneToOneField('TDemanda', on_delete=models.CASCADE, null=False, blank=False)


    class Meta:
        abstract = True

    # def save(self, *args, **kwargs):
    #     if not self.pk:  # onCreate
    #         if self.estado_calificacion == 'PASA_A_LEGAJO':
    #             self.crear_legajo(self.demanda.nnya)
    #             self.demanda.estado_demanda = 'ADMITIDA'
    #         if self.estado_calificacion != 'NO_PERTINENTE':
    #             self.demanda.estado_demanda = 'ARCHIVADA'
    #     else:  # onUpdate
    #         if self.estado_calificacion == 'PASA_A_LEGAJO':
    #             self.crear_legajo(self.demanda.nnya)
    #             self.demanda.estado_demanda = 'ADMITIDA'
    #         if self.estado_calificacion != 'NO_PERTINENTE':
    #             self.demanda.estado_demanda = 'ARCHIVADA'
        
    #     self.demanda.save()
    #     super().save(*args, **kwargs)

    def crear_legajo(self, nnya):
        # Implement the logic to create a legajo
        pass
    
    def __str__(self):
        return f"{self.estado_calificacion} - {self.demanda}"


class TCalificacionDemanda(TCalificacionDemandaBase):

    class Meta:
        app_label = 'infrastructure'
        verbose_name = _('Calificación de Demanda')
        verbose_name_plural = _('Calificaciones de Demandas')


class TCalificacionDemandaHistory(TCalificacionDemandaBase, BaseHistory):
    demanda = models.ForeignKey('TDemanda', on_delete=models.CASCADE, null=False, blank=False)
    parent = models.ForeignKey(
        'infrastructure.TCalificacionDemanda',
        on_delete=models.CASCADE,
        related_name='history'
    )

    class Meta:
        app_label = 'infrastructure'
        verbose_name = _('Historial de Calificacion de Demanda')
        verbose_name_plural = _('Historial de Calificaciones de Demandas')


class TDemandaScoreBase(models.Model):
    ultima_actualizacion = models.DateTimeField(auto_now=True)
    score = models.FloatField(default=0)
    score_condiciones_vulnerabilidad = models.FloatField(default=0)
    score_vulneracion = models.FloatField(default=0)
    score_motivos_intervencion = models.FloatField(default=0)
    score_indicadores_valoracion = models.FloatField(default=0)

    demanda = models.OneToOneField('TDemanda', on_delete=models.CASCADE, unique=True, null=False, blank=False)

    class Meta:
        abstract = True  # This model is abstract and won't create a table.
        
    def __str__(self):
        return f"{self.score} - {self.demanda}"


class TDemandaScore(TDemandaScoreBase):

    class Meta:
        app_label = 'infrastructure'
        verbose_name = _('Score de Demanda')
        verbose_name_plural = _('Scores de Demandas')


class TDemandaScoreHistory(TDemandaScoreBase, BaseHistory):
    demanda = models.ForeignKey('TDemanda', on_delete=models.CASCADE, unique=False, null=False, blank=False)
    parent = models.ForeignKey(
        'infrastructure.TDemandaScore',
        on_delete=models.CASCADE,
        related_name='history'
    )

    class Meta:
        app_label = 'infrastructure'
        verbose_name = _('Historial de Score de Demanda')
        verbose_name_plural = _('Historial de Scores de Demandas')
