from rest_framework import generics
from app.models import Reels, Authors
from rest_framework import serializers
from rest_framework.pagination import CursorPagination
from datetime import datetime, date, time


class AuthorsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Authors
        fields = "__all__"


class ReelsSerializer(serializers.ModelSerializer):
    author = AuthorsSerializer()

    class Meta:
        model = Reels
        fields = "__all__"



class CursorSetPagination(CursorPagination):
    page_size = 2
    page_size_query_param = 'page_size'
    ordering = 'id'


class ReelsList(generics.ListAPIView):

    serializer_class = ReelsSerializer
    pagination_class = CursorSetPagination


    def get_queryset(self):

        query = {}

        author = self.request.GET.get('author')
        if author:
            query['author__nick'] = author

        q_key = 'description__icontains'
        q_where = self.request.GET.get('q_where')
        if q_where:
            print('q-->', q_where)
            if q_where == 'author_dis':
                q_key = 'author__description__icontains'


        q = self.request.GET.get('q')
        if q:
            print('q-->', q)
            query[q_key] = q


        subs_start = self.request.GET.get('subs_start') or 0
        subs_end = self.request.GET.get('subs_end') or 1000000000

        if (subs_start != 0) and (subs_end != 1000000000):
            subs_range = (int(subs_start), int(subs_end))
            print('-->', subs_range)
            query['author__subscribers__range'] = subs_range

        views_start = self.request.GET.get('views_start') or 0
        views_end = self.request.GET.get('views_end') or 10000000000
        if (views_start != 0) and (views_end != 10000000000):
            views_range = (int(views_start), views_end)
            query['views__range='] = views_range

        like_start = self.request.GET.get('like_start') or 0
        like_end = self.request.GET.get('like_end') or 10000000000
        if (like_start != 0) and (like_end != 10000000000):
            likes_range = (int(like_start), like_end)
            query['likes__range='] = likes_range

        comment_start = self.request.GET.get('comment_start') or 0
        comment_end = self.request.GET.get('comment_end') or 10000000000
        if (comment_start != 0) and (comment_end != 10000000000):
            comment_range = (int(comment_start), comment_end)
            query['comment_range='] = comment_range


        self.queryset = Reels.objects.filter(**query)
        ignore = self.request.GET.getlist('ignore[]')
        if ignore:
            self.queryset = self.queryset.exclude(author__nick__in=ignore)



        return self.queryset

