from runna.middleware import get_current_authenticated_user
from django.db.utils import IntegrityError
from datetime import datetime


def logs(HistoryModelName, action, instance, current_user=None ,descripcion_temp=None):

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
