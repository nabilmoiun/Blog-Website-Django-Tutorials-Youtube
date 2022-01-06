from notification.models import Notificaiton


def user_notifications(request):
    context = {}

    if request.user.is_authenticated:
        notifications = Notificaiton.objects.filter(
            user=request.user
        ).order_by('-created_date')
        unseen = notifications.exclude(is_seen=True)
        context['notifications'] = notifications
        context['unseen'] = unseen.count()

    return context