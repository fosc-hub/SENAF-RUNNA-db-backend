from runna.middleware import get_current_authenticated_user
from django.db.utils import IntegrityError
from datetime import datetime


def logs(HistoryModelName, action, instance, descripcion_temp=None):
    
    import inspect
    for frame_record in inspect.stack():
        if frame_record[3]=='get_response':
            request = frame_record[0].f_locals['request']
            break
    print(f"Request: {request.user}")

    current_user = request.user

    try:
        descripcion = f"{datetime.now().strftime('%d/%m/%y %H:%M')} {current_user} - " + descripcion_temp
        HistoryModelName.objects.create(
            descripcion=descripcion,
            parent=instance,
            action=action,
            by_user=current_user,
            **{field.name: getattr(instance, field.name, None) for field in instance._meta.fields if field.name != 'id'}
        )
    except ValueError:
        HistoryModelName.objects.create(
            descripcion=descripcion,
            parent=instance,
            action=action,
            by_user=None,
            **{field.name: getattr(instance, field.name, None) for field in instance._meta.fields if field.name != 'id'}
        )
    except IntegrityError:
        pass
