import json
from django.core.management.base import BaseCommand
from django.apps import apps
from django.db.models import NOT_PROVIDED
import pandas as pd  # Ensure you have pandas installed

class Command(BaseCommand):
    help = 'Genera un JSON y un XLSX con las tablas (modelos) y todos sus campos'

    def handle(self, *args, **kwargs):
        # Se asume que los modelos se encuentran en el app "infrastructure".
        app_config = apps.get_app_config('infrastructure')
        models_list = app_config.get_models()
        
        output = {}
        rows = []  # Para crear la tabla del Excel

        for model in models_list:
            model_fields = []
            for field in model._meta.fields:
                # Para cada campo se determina si es obligatorio
                is_required = not field.null and not field.blank and field.default == NOT_PROVIDED
                
                # Get field type
                field_type = field.get_internal_type()
                
                # Get choices if available
                choices = None
                if hasattr(field, 'choices') and field.choices:
                    choices = [choice[0] for choice in field.choices]
                
                field_data = {
                    "name": field.name,
                    "required": is_required,
                    "type": field_type,
                    "choices": choices
                }
                model_fields.append(field_data)
                
                # Se agrega una fila para el Excel
                rows.append({
                    "Model": model.__name__,
                    "Field": field.name,
                    "Type": field_type,
                    "Choices": str(choices) if choices else None,
                    "Required": is_required
                })
                output[model.__name__] = model_fields

        # Guardar la salida en un archivo JSON
        json_output = json.dumps(output, indent=4, ensure_ascii=False)
        self.stdout.write(json_output)
        with open('all_fields.json', 'w', encoding='utf-8') as f:
            f.write(json_output)
        
        # Guardar la salida en un archivo Excel (única hoja)
        df = pd.DataFrame(rows)
        df.to_excel('all_fields.xlsx', index=False)
