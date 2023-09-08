from django.contrib.contenttypes.models import ContentType
from django.utils import timezone

import datetime

from .models import Action

def create_action(user, verb, target=None):
    now = timezone.now()
    last_time = now - datetime.timedelta(seconds=60)
    similar_actions = Action.objects.filter(user=user, verb=verb, created__gte=last_time)
    if target:
        target_cont_type = ContentType.objects.get_for_model(target)
        similar_actions = similar_actions.filter(target_cont_type=target_cont_type, target_id=target.id)
    
    if not similar_actions:
        act = Action(user=user, verb=verb, target=target)
        act.save()
        return True
    return False