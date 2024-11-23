from runna.middleware import get_current_authenticated_user

def logs(HistoryModelName, action, instance):
    HistoryModelName.objects.create(
        parent=instance,
        action=action,
        user=get_current_authenticated_user(),
        **{field.name: getattr(instance, field.name, None) for field in instance._meta.fields if field.name != 'id'}
    )