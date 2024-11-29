from runna.middleware import get_current_authenticated_user
from django.db.utils import IntegrityError


def logs(HistoryModelName, action, instance):
    try:
        HistoryModelName.objects.create(
            parent=instance,
            action=action,
            by_user=get_current_authenticated_user(),
            **{field.name: getattr(instance, field.name, None) for field in instance._meta.fields if field.name != 'id'}
        )
    except ValueError:
        HistoryModelName.objects.create(
            parent=instance,
            action=action,
            by_user=None,
            **{field.name: getattr(instance, field.name, None) for field in instance._meta.fields if field.name != 'id'}
        )
    except IntegrityError:
        pass
