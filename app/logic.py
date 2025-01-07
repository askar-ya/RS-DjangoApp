from django.db.models import Q



from .models import Reels


def search(request):
    q = request.GET.get('q')
    print(q)

    data = Reels.objects.filter(Q(description__contains=q)).order_by('-id')
    print(data)

    return data