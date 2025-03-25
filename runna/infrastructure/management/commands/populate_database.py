import json
import random
import pandas as pd
from django.core.management.base import BaseCommand
from django.apps import apps
from faker import Faker
from django.db import models

fake = Faker()

def load_excel_data(self, file_path, sheet_name=None):
    try:
        data = pd.read_excel(file_path, sheet_name=sheet_name)
        return data
    except FileNotFoundError:
        self.stderr.write(self.style.ERROR(f'{file_path} not found!'))
        raise FileNotFoundError(f'{file_path} not found!')

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

        # Load data from Excel file
        # bloque_datos_remitente_data = load_excel_data(self, './runna/infrastructure/management/fixtures/origen de la demanda.xlsx')
        tipo_institucion_demanda_data = load_excel_data(self, './infrastructure/management/fixtures/CIRCUNSCRIPCIONES_TIPOS Y ORGANOS JUDICIALES.xlsx', sheet_name='TIPO Y ÓRGANOS judiciales')
        zonas = load_excel_data(self, './infrastructure/management/fixtures/equipos senaf.xlsx', sheet_name='Hoja1')
        tipo_codigo_demanda = load_excel_data(self, './infrastructure/management/fixtures/tipo_codigo_demanda.xlsx', sheet_name='Sheet1')
        motivos_submotivos = load_excel_data(self, './infrastructure/management/fixtures/motivos, submotivos y derechos.xlsx', sheet_name='categ motivo y tipos de motivos')
        tipos_presuntos_delitos = load_excel_data(self, './infrastructure/management/fixtures/tipos de presuntos delitos.xlsx', sheet_name='Hoja1')
        ambitos_vulneracion = load_excel_data(self, './infrastructure/management/fixtures/AMBITOS DE LA VULNERACION.xlsx', sheet_name='AMBITOS DE LA VULNERACION')
        vinculo_de_personas = load_excel_data(self, './infrastructure/management/fixtures/tipos de relaciones vinculares.xlsx', sheet_name='Hoja1')
        localidades = load_excel_data(self, './infrastructure/management/fixtures/localidades prov cba.xlsx', sheet_name='Hoja1')
        salud = load_excel_data(self, './infrastructure/management/fixtures/salud.xlsx', sheet_name='Sheet1')
        condiciones_vulnerabilidad = load_excel_data(self, './infrastructure/management/fixtures/condiciones_vulnerabilidad.xlsx', sheet_name='Sheet1')
        indicadores_valoracion = load_excel_data(self, './infrastructure/management/fixtures/indicadores_valoracion.xlsx', sheet_name='Sheet1')
        tipos_actividad = load_excel_data(self, './infrastructure/management/fixtures/tipos_actividad.xlsx', sheet_name='Sheet1')

        for model_name in model_order:
            model = apps.get_model(model_name)  # Adjust 'myapp' to your app name
            self.stdout.write(f'Populating model: {model_name}')
            
            if model_name == 'infrastructure.TBloqueDatosRemitente':
                pass
            elif model_name == 'infrastructure.TTipoInstitucionDemanda':
                for index, row in tipo_institucion_demanda_data.iterrows():
                    bloque_obj_data = {
                        'nombre': row['tipo de órgano judicial'],
                    }
                    try:
                        bloque_model = apps.get_model("infrastructure.TBloqueDatosRemitente")
                        bloque_db = bloque_model.objects.get_or_create(**bloque_obj_data)
                    except Exception as e:
                        self.stderr.write(self.style.ERROR(f'Error creating {model_name} object: {e}'))

                    institucion_demanda_data = {
                        'nombre': row['Organos Judiciales'],
                        'bloque_datos_remitente': bloque_db[0],
                    }
                    try:
                        model.objects.get_or_create(**institucion_demanda_data)
                    except Exception as e:
                        self.stderr.write(self.style.ERROR(f'Error creating {model_name} object: {e}'))
            elif model_name == 'customAuth.TZona':
                for index, row in zonas.iterrows():
                    obj_data = {
                        'nombre': row['UDER/Zonas'],
                    }
                    try:
                        model.objects.get_or_create(**obj_data)
                    except Exception as e:
                        self.stderr.write(self.style.ERROR(f'Error creating {model_name} object: {e}'))
            elif model_name == 'infrastructure.TCategoriaMotivo':
                pass
            elif model_name == 'infrastructure.TCategoriaSubmotivo':
                for index, row in motivos_submotivos.iterrows():
                    motivo_data = {
                        'nombre': row['MOTIVO'],
                        'peso': 2,
                    }
                    try:
                        motivo_model = apps.get_model("infrastructure.TCategoriaMotivo")
                        motivo_db = motivo_model.objects.get_or_create(**motivo_data)
                    except Exception as e:
                        self.stderr.write(self.style.ERROR(f'Error creating {model_name} object: {e}'))
                    
                    sumbotivo_data = {
                        'nombre': row['SUBMOTIVO'],
                        'peso': random.randint(1, 5),
                        'motivo': motivo_db[0],
                    }
                    try:
                        model.objects.get_or_create(**sumbotivo_data)
                    except Exception as e:
                        self.stderr.write(self.style.ERROR(f'Error creating {model_name} object: {e}'))
            elif model_name == 'infrastructure.TTipoPresuntoDelito':
                for index, row in tipos_presuntos_delitos.iterrows():
                    obj_data = {
                        'nombre': row['Tipos Delito'],
                    }
                    try:
                        model.objects.get_or_create(**obj_data)
                    except Exception as e:
                        self.stderr.write(self.style.ERROR(f'Error creating {model_name} object: {e}'))
            elif model_name == 'infrastructure.TTipoCodigoDemanda':
                for index, row in tipo_codigo_demanda.iterrows():
                    obj_data = {
                        'nombre': row['nombre'],
                        'datatype': row['datatype'],
                    }
                    try:
                        model.objects.get_or_create(**obj_data)
                    except Exception as e:
                        self.stderr.write(self.style.ERROR(f'Error creating {model_name} object: {e}'))
            elif model_name == 'infrastructure.TAmbitoVulneracion':
                for index, row in ambitos_vulneracion.iterrows():
                    obj_data = {
                        'nombre': row['AMBITOS DE LA VULNERACION'],
                    }
                    try:
                        model.objects.get_or_create(**obj_data)
                    except Exception as e:
                        self.stderr.write(self.style.ERROR(f'Error creating {model_name} object: {e}'))
            elif model_name == 'infrastructure.TLocalidad':
                cont = 0
                for index, row in localidades.iterrows():
                    if cont == 15:
                        break
                    obj_data = {
                        'nombre': row['NOMBRE LOCAL'],
                    }
                    try:
                        model.objects.get_or_create(**obj_data)
                        cont += 1
                    except Exception as e:
                        self.stderr.write(self.style.ERROR(f'Error creating {model_name} object: {e}'))
            elif model_name == 'infrastructure.TVinculoDePersonas':
                for index, row in vinculo_de_personas.iterrows():
                    obj_data = {
                        'nombre': row['TIPOS DE RELACIONES VINCULARES'],
                    }
                    try:
                        model.objects.get_or_create(**obj_data)
                    except Exception as e:
                        self.stderr.write(self.style.ERROR(f'Error creating {model_name} object: {e}'))
            elif model_name == 'infrastructure.TSituacionSalud':
                pass
            elif model_name == 'infrastructure.TEnfermedad':
                for index, row in salud.iterrows():
                    situacion_salud_data = {
                        'nombre': row['SITUACIONES DE SALUD'],
                    }
                    try:
                        situacion_salud_model = apps.get_model("infrastructure.TSituacionSalud")
                        situacion_salud_db = situacion_salud_model.objects.get_or_create(**situacion_salud_data)
                    except Exception as e:
                        self.stderr.write(self.style.ERROR(f'Error creating {model_name} object: {e}'))

                    enfermedad_data = {
                        'nombre': row['ENFERMEDADES'],
                        'situacion_salud_categoria': situacion_salud_db[0],
                    }
                    try:
                        model.objects.get_or_create(**enfermedad_data)
                    except Exception as e:
                        self.stderr.write(self.style.ERROR(f'Error creating {model_name} object: {e}'))
            elif model_name == 'customAuth.TCustomUserZona':
                for i in range(1, 10):
                    try:
                        user = apps.get_model("customAuth.CustomUser").objects.get(id=i)
                        zona = apps.get_model("customAuth.TZona").objects.get(id=1)
                        user_zona_data = {
                            'director': random.choice([False]),
                            'jefe': random.choice([False]),
                            'user': user,
                            'zona': zona,
                        }
                        model.objects.get_or_create(**user_zona_data)
                        self.stdout.write(f'User {user} added to Zona 1')
                    except Exception as e:
                        self.stderr.write(self.style.ERROR(f'Error creating {model_name} object: {e}'))
            elif model_name == 'infrastructure.TCondicionesVulnerabilidad':
                for index, row in condiciones_vulnerabilidad.iterrows():
                    obj_data = {
                        'nombre': row['condiciones_vulnerabilidad'],
                        'peso': random.randint(1, 5),
                        'nnya': 'NNA' in row['condiciones_vulnerabilidad'],
                        'adulto': 'NNA' not in row['condiciones_vulnerabilidad'],
                    }
                    try:
                        model.objects.get_or_create(**obj_data)
                    except Exception as e:
                        self.stderr.write(self.style.ERROR(f'Error creating {model_name} object: {e}'))
            elif model_name == 'infrastructure.TIndicadoresValoracion':
                for index, row in indicadores_valoracion.iterrows():
                    obj_data = {
                        'nombre': row['indicadores_valoracion'],
                        'peso': random.randint(1, 5),
                    }
                    try:
                        model.objects.get_or_create(**obj_data)
                    except Exception as e:
                        self.stderr.write(self.style.ERROR(f'Error creating {model_name} object: {e}'))
            elif model_name == 'infrastructure.TActividadTipo':
                for index, row in tipos_actividad.iterrows():
                    obj_data = {
                        'nombre': row['tipos_actividad'],
                    }
                    try:
                        model.objects.get_or_create(**obj_data)
                    except Exception as e:
                        self.stderr.write(self.style.ERROR(f'Error creating {model_name} object: {e}'))
            else:
                for _ in range(40):  # Number of objects per model
                    obj_data = {}
                    for field in model._meta.fields:
                        if field.name == 'id':  # Skip ID field
                            continue
                        if field.choices:
                            obj_data[field.name] = random.choice([choice[0] for choice in field.choices])
                        elif isinstance(field, models.EmailField):
                            obj_data[field.name] = 'facundoolivam@gmail.com' #fake.email()
                        elif field.get_internal_type() == 'CharField':
                            obj_data[field.name] = fake.word()
                        elif field.get_internal_type() == 'TextField':
                            obj_data[field.name] = fake.text()
                        elif field.get_internal_type() == 'IntegerField':
                            obj_data[field.name] = random.randint(1, 100)
                        elif field.get_internal_type() == 'FloatField':
                            obj_data[field.name] = random.uniform(1, 100)
                        elif field.get_internal_type() == 'BooleanField':
                            obj_data[field.name] = random.choice([True, False])
                        elif field.get_internal_type() == 'DateField':
                            obj_data[field.name] = fake.date()
                        elif field.get_internal_type() == 'TimeField':
                            obj_data[field.name] = fake.date_time()
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
                            # else:
                            #     related_obj = related_model.objects.create(**self.get_fake_data(related_model))
                            #     obj_data[field.name] = related_obj

                    try:
                        model.objects.create(**obj_data)
                    except Exception as e:
                        self.stderr.write(self.style.ERROR(f'Error creating {model_name} object: {e}'))

