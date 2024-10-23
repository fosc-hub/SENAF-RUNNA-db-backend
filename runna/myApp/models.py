from django.db import models

# Modelos base relacionados con Localización
class Provincia(models.Model):
    nombre = models.CharField(max_length=255)

    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name = "Provincia"
        verbose_name_plural = "Provincias"

class Localidad(models.Model):
    nombre = models.CharField(max_length=255)
    provincia = models.ForeignKey(Provincia, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nombre} ({self.provincia})"
    class Meta:
        verbose_name = "Localidad"
        verbose_name_plural = "Localidades"

class Barrio(models.Model):
    nombre = models.CharField(max_length=255)
    localidad = models.ForeignKey(Localidad, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nombre} - {self.localidad}"
    
    class Meta:
        verbose_name = "Barrio"
        verbose_name_plural = "Barrios"

class LocalizacionDemanda(models.Model):
    calle = models.CharField(max_length=255)
    numero = models.CharField(max_length=10)
    barrio = models.ForeignKey(Barrio, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.calle} {self.numero}, {self.barrio}"
    
    class Meta:
        verbose_name = "Localización de Demanda"
        verbose_name_plural = "Localizaciones de Demanda"

# Instituciones y vinculación
class InstitucionEducativa(models.Model):
    nombre = models.CharField(max_length=255)

    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name = "Institución Educativa"
        verbose_name_plural = "Instituciones Educativas"

class InstitucionSanitaria(models.Model):
    nombre = models.CharField(max_length=255)

    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name = "Institución Sanitaria"
        verbose_name_plural = "Instituciones Sanitarias"


class Vinculo(models.Model):
    descripcion = models.CharField(max_length=255)

    def __str__(self):
        return self.descripcion
    
    class Meta:
        verbose_name = "Vínculo"
        verbose_name_plural = "Vínculos"

class Responsable(models.Model):
    nombre = models.CharField(max_length=255)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = "Responsable"
        verbose_name_plural = "Responsables"

# Modelos de Usuarios y Roles
class UsuarioL(models.Model):
    nombre_y_apellido = models.CharField(max_length=255)
    institucion = models.ForeignKey(InstitucionEducativa, on_delete=models.CASCADE)
    responsable = models.ForeignKey(Responsable, on_delete=models.CASCADE)
    vinculo = models.ForeignKey(Vinculo, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre_y_apellido

    class Meta:
        verbose_name = "Usuario Linea"
        verbose_name_plural = "Usuarios Linea"

# Demanda y Entidades Relacionadas
class EstadoDemanda(models.Model):
    estado = models.CharField(max_length=255)

    def __str__(self):
        return self.estado

    class Meta:
        verbose_name = "Estado de Demanda"
        verbose_name_plural = "Estados de Demanda"

class PrioridadIntervencion(models.Model):
    descripcion = models.CharField(max_length=255)

    def __str__(self):
        return self.descripcion
    
    class Meta:
        verbose_name = "Prioridad de Intervención"
        verbose_name_plural = "Prioridades de Intervención"


class Problematica(models.Model):
    descripcion = models.CharField(max_length=255)

    def __str__(self):
        return self.descripcion

    class Meta:
        verbose_name = "Problemática"
        verbose_name_plural = "Problemáticas"

class Ambito(models.Model):
    descripcion = models.CharField(max_length=255)

    def __str__(self):
        return self.descripcion
    
    class Meta:
        verbose_name = "Ámbito"
        verbose_name_plural = "Ámbitos"


class Operador(models.Model):
    nombre_y_apellido = models.CharField(max_length=255)

    def __str__(self):
        return self.nombre_y_apellido
    
    class Meta:
        verbose_name = "Operador"
        verbose_name_plural = "Operadores"

class DDV(models.Model):
    descripcion = models.CharField(max_length=255)

    def __str__(self):
        return self.descripcion
    
    class Meta:
        verbose_name = "Derecho Vulnerado"
        verbose_name_plural = "Derechos Vulnerados"


class NNyA(models.Model):
    nombre = models.CharField(max_length=255)
    institucion_sanitaria = models.ForeignKey(InstitucionSanitaria, on_delete=models.SET_NULL, null=True)
    institucion_educativa = models.ForeignKey(InstitucionEducativa, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name = "Niño, Niña o Adolescente"
        verbose_name_plural = "Niños, Niñas y Adolescentes"

class Demanda(models.Model):
    descripcion = models.TextField()
    estado = models.ForeignKey(EstadoDemanda, on_delete=models.CASCADE)
    localizacion = models.ForeignKey(LocalizacionDemanda, on_delete=models.CASCADE)
    usuario = models.ForeignKey(UsuarioL, on_delete=models.CASCADE)

    def __str__(self):
        return f"Demanda ({self.estado}): {self.descripcion[:50]}"
    
    class Meta:
        verbose_name = "Demanda"
        verbose_name_plural = "Demandas"

class DemandaNNyA(models.Model):
    demanda = models.ForeignKey(Demanda, on_delete=models.CASCADE)
    nnya = models.ForeignKey(NNyA, on_delete=models.CASCADE)

    def __str__(self):
        return f"Demanda {self.demanda.id} - NNyA {self.nnya}"
    
    class Meta:
        verbose_name = "Demanda y NNyA"
        verbose_name_plural = "Demandas y NNyA"

# Actividades y Evaluaciones
class ActividadTipo(models.Model):
    descripcion = models.CharField(max_length=255)

    def __str__(self):
        return self.descripcion
    
    class Meta:
        verbose_name = "Tipo de Actividad"
        verbose_name_plural = "Tipos de Actividad"

class Actividad(models.Model):
    descripcion = models.TextField()
    tipo = models.ForeignKey(ActividadTipo, on_delete=models.CASCADE)
    demanda = models.ForeignKey(Demanda, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.tipo}: {self.descripcion[:50]}"
    
    class Meta:
        verbose_name = "Actividad"
        verbose_name_plural = "Actividades"

class Evaluacion(models.Model):
    demanda = models.ForeignKey(Demanda, on_delete=models.CASCADE)
    comentarios = models.TextField()

    def __str__(self):
        return f"Evaluación de Demanda {self.demanda.id}"
    
    class Meta:
        verbose_name = "Evaluación"
        verbose_name_plural = "Evaluaciones"

class GravedadTipo(models.Model):
    descripcion = models.CharField(max_length=255)

    def __str__(self):
        return self.descripcion
    
    class Meta:
        verbose_name = "Gravedad de Evaluación"
        verbose_name_plural = "Gravedades de Evaluación"

class UrgenciaTipo(models.Model):
    descripcion = models.CharField(max_length=255)

    def __str__(self):
        return self.descripcion
    
    class Meta:
        verbose_name = "Urgencia de Evaluación"
        verbose_name_plural = "Urgencias de Evaluación"

class EvaluacionAccion(models.Model):
    evaluacion = models.ForeignKey(Evaluacion, on_delete=models.CASCADE)
    descripcion = models.CharField(max_length=255)

    def __str__(self):
        return self.descripcion
    
    class Meta:
        verbose_name = "Acción de Evaluación"
        verbose_name_plural = "Acciones de Evaluación"

class Legajo(models.Model):
    nnya = models.ForeignKey(NNyA, on_delete=models.CASCADE)

    def __str__(self):
        return f"Legajo de NNyA {self.nnya}"
    
    class Meta:
        verbose_name = "Legajo"
        verbose_name_plural = "Legajos"

# Respuestas y Vinculación de Demandas
class Respuesta(models.Model):
    demanda = models.ForeignKey(Demanda, on_delete=models.CASCADE)
    mensaje = models.TextField()

    def __str__(self):
        return f"Respuesta a Demanda {self.demanda.id}"
    
    class Meta:
        verbose_name = "Respuesta"
        verbose_name_plural = "Respuestas"

class DemandaVinculada(models.Model):
    demanda_principal = models.ForeignKey(Demanda, related_name='demanda_principal', on_delete=models.CASCADE)
    demanda_relacionada = models.ForeignKey(Demanda, related_name='demanda_relacionada', on_delete=models.CASCADE)

    def __str__(self):
        return f"Demanda {self.demanda_principal.id} vinculada con Demanda {self.demanda_relacionada.id}"
    
    class Meta:
        verbose_name = "Demanda Vinculada"
        verbose_name_plural = "Demandas Vinculadas"
