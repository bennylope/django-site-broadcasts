from broadcasts.models import BroadcastMessage


def broadcast_message(request):
    """Adds the latest available broadcast message to the context, or None"""
    return {"broadcast_message": BroadcastMessage.objects.latest()}
