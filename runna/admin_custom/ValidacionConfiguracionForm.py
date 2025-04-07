from django import forms
from django.contrib import admin
from infrastructure.models import TDemanda, TActividadTipo, TRespuestaEtiqueta
from infrastructure.models import ValidacionConfiguracion

class ValidacionConfiguracionForm(forms.ModelForm):
    # Se generan dinámicamente las opciones para los campos de TDemanda.
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Excluimos campos que no queremos mostrar (por ejemplo, 'id', u otros)
        available_fields = [
            (field.name, field.verbose_name.title()) 
            for field in TDemanda._meta.fields 
            if field.name not in ['id', 'ultima_actualizacion', 'fecha_creacion']
        ]
        print(f"available fields: {available_fields}")
        self.fields['required_fields'] = forms.MultipleChoiceField(
            choices=available_fields,
            widget=forms.CheckboxSelectMultiple,
            required=False,
            label="Campos obligatorios"
        )
        # Para los tipos de actividad
        self.fields['required_activity_types'] = forms.ModelMultipleChoiceField(
            queryset=TActividadTipo.objects.all(),
            widget=forms.CheckboxSelectMultiple,
            required=False,
            label="Tipos de actividad requeridos"
        )
        # Para los tipos de respuesta
        self.fields['required_response_types'] = forms.ModelMultipleChoiceField(
            queryset=TRespuestaEtiqueta.objects.all(),
            widget=forms.CheckboxSelectMultiple,
            required=False,
            label="Tipos de respuesta requeridos"
        )
        # Si ya existe una instancia, se cargan los valores almacenados en formato JSON
        if self.instance and self.instance.pk:
            self.initial['required_fields'] = self.instance.required_fields
            self.initial['required_activity_types'] = TActividadTipo.objects.filter(
                pk__in=self.instance.required_activity_types
            )
            self.initial['required_response_types'] = TRespuestaEtiqueta.objects.filter(
                pk__in=self.instance.required_response_types
            )

    class Meta:
        model = ValidacionConfiguracion
        fields = []  # Los campos se agregan dinámicamente

    def clean(self):
        # Al limpiar, si se reciben los valores de actividades y respuestas, extraemos los pks para almacenarlos en JSON
        cleaned_data = super().clean()
        activity_objs = cleaned_data.get('required_activity_types')
        response_objs = cleaned_data.get('required_response_types')
        if activity_objs:
            cleaned_data['required_activity_types'] = [obj.pk for obj in activity_objs]
        else:
            cleaned_data['required_activity_types'] = []
        if response_objs:
            cleaned_data['required_response_types'] = [obj.pk for obj in response_objs]
        else:
            cleaned_data['required_response_types'] = []
        return cleaned_data
