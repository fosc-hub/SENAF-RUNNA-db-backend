import json
from django.core.management.base import BaseCommand
from django.apps import apps
from django.db.models import NOT_PROVIDED

class Command(BaseCommand):
    help = 'Genera un JSON con las tablas (modelos) y sus campos obligatorios'

    def handle(self, *args, **kwargs):
        # Se asume que los modelos se encuentran en el app "infrastructure".
        # Esto depende de cómo se haya organizado el __init__.py.
        app_config = apps.get_app_config('infrastructure')
        models_list = app_config.get_models()
        
        output = {}

        for model in models_list:
            required_fields = []
            for field in model._meta.fields:
                # Se omiten los campos autogenerados (por ejemplo, 'id')
                if field.auto_created:
                    continue
                # Se considera obligatorio si:
                #  - No permite nulos (null=False)
                #  - No permite valor en blanco (blank=False)
                #  - No tiene valor por defecto (por lo que se espera que se provea)
                if not field.null and not field.blank and field.default == NOT_PROVIDED:
                    required_fields.append(field.name)
            output[model.__name__] = required_fields

        json_output = json.dumps(output, indent=4, ensure_ascii=False)
        self.stdout.write(json_output)
        with open('required_fields.json', 'w') as f:
            f.write(json_output)
