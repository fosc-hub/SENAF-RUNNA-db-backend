from django.apps import apps

def file_directory(instance, filename, dir, prefix, model_name):
    """
    Returns a dynamic file path.
    
    If the instance already has an ID, it uses that.
    Otherwise, it counts the number of objects and uses that as a fallback.
    """
    if instance.id:
        return f'{dir}/{prefix}{instance.id}/{filename}'
    else:
        # Get the model class; model_name must be fully qualified: "app_label.ModelName"
        model = apps.get_model(model_name)
        count = model.objects.count() + 1
        return f'{dir}/{prefix}{count}/{filename}'

def upload_to_adjuntos(instance, filename):
    # Adjust the parameters as needed. For example, using the model's app label and name.
    # Here, we assume the model is "infrastructure.TActividad" (replace as appropriate).
    return file_directory(
        instance,
        filename,
        dir=instance.__class__.__name__,  # or a fixed directory name like 'TActividad'
        prefix='archivo_',
        model_name=f'infrastructure.{instance.__class__.__name__}'
    )
