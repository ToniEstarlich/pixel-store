from django.utils.timezone import now

def timestamp(request):
    return {
        'timestamp': int(now().timestamp())
    }
