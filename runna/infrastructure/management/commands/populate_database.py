import json
import random
from django.core.management.base import BaseCommand
from django.apps import apps
from faker import Faker

fake = Faker()

class Command(BaseCommand):
    help = 'Populate database with random data for all models in a specified order'

    def handle(self, *args, **kwargs):
        # Load the ordered model list from JSON
        try:
            with open('./infrastructure/management/fixtures/sorted_models.json', 'r') as f:
                model_order = json.load(f)['models']
        except FileNotFoundError:
            self.stderr.write(self.style.ERROR('sorted_models.json not found!'))
            return

        for model_name in model_order:
            model = apps.get_model('infrastructure', model_name)  # Adjust 'myapp' to your app name
            self.stdout.write(f'Populating model: {model_name}')

            for _ in range(10):  # Number of objects per model
                obj_data = {}
                for field in model._meta.fields:
                    if field.name == 'id':  # Skip ID field
                        continue
                    if field.choices:
                        obj_data[field.name] = random.choice([choice[0] for choice in field.choices])
                    elif field.get_internal_type() == 'CharField':
                        obj_data[field.name] = fake.word()
                    elif field.get_internal_type() == 'TextField':
                        obj_data[field.name] = fake.text()
                    elif field.get_internal_type() == 'IntegerField':
                        obj_data[field.name] = random.randint(1, 100)
                    elif field.get_internal_type() == 'BooleanField':
                        obj_data[field.name] = random.choice([True, False])
                    elif field.get_internal_type() == 'DateField':
                        obj_data[field.name] = fake.date()
                    elif field.get_internal_type() == 'TimeField':
                        obj_data[field.name] = fake.date_time()
                    elif field.get_internal_type() == 'EmailField':
                        obj_data[field.name] = fake.email()
                    elif field.get_internal_type() == 'ForeignKey':
                        related_model = field.related_model
                        related_obj = related_model.objects.order_by('?').first()
                        if related_obj:
                            obj_data[field.name] = related_obj
                        else:
                            self.stdout.write(
                                self.style.WARNING(f'Skipping {field.name} on {model_name} due to missing related object.')
                            )
                    elif field.get_internal_type() == 'OneToOneField':
                        related_model = field.related_model
                        related_obj = related_model.objects.order_by('?').first()
                        if related_obj:
                            obj_data[field.name] = related_obj
                        else:
                            related_obj = related_model.objects.create(**self.get_fake_data(related_model))
                            obj_data[field.name] = related_obj

                try:
                    model.objects.create(**obj_data)
                except Exception as e:
                    self.stderr.write(self.style.ERROR(f'Error creating {model_name} object: {e}'))

            self.stdout.write(self.style.SUCCESS(f'Finished populating {model_name}'))
