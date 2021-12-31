from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import viewsets , filters
from rest_framework import generics
from .serializers import FilmSerializer, ProfileSerializer , LikeSerializer, DislikeSerializer
from .models import Film, Category, Profile, Like , Dislike
from rest_framework.permissions import IsAuthenticated

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# from celery.schedules import crontab
# from django.http.response import HttpResponse
# from django.shortcuts import render
#
# from .tasks import send_mail_func
# from django_celery_beat.models import PeriodicTask, CrontabSchedule
# import json





# Create your views here.

class FilmView(viewsets.ModelViewSet):
    search_fields = ['title','director']
    filter_backends = (filters.SearchFilter,)
    queryset = Film.objects.all()
    serializer_class = FilmSerializer

    def get_queryset(self):
        """
        Optionally restricts the returned purchases to a given user,
        by filtering against a `username` query parameter in the URL.
        """
        queryset = Film.objects.all()
        category  = self.request.query_params.get('category')
        if category  is not None:
            queryset = queryset.filter(category__name =category )
        return queryset

class ProfileView(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


class LikeView(viewsets.ModelViewSet):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer

    def get_queryset(self):
        if self.request.method == 'post':
            id = self.request.GET.get('id')
            if id:
                film= Film.objects.get(id=id)
                like =Like.objects.create(user=self.request.user,film=film)
                like.save()
                return Response({"message": "%s liked!" % film.title}, status=status.HTTP_200_OK)

            return Response({"message": "ERROR!"}, status=status.HTTP_400_BAD_REQUEST)


class DislikeView(viewsets.ModelViewSet):
    queryset = Dislike.objects.all()
    serializer_class = DislikeSerializer

    def get_queryset(self):
        if self.request.method == 'post':
            id = self.request.GET.get('id')
            if id:
                film= Film.objects.get(id=id)
                like =Dislike.objects.create(user=self.request.user,film=film)
                like.save()
                return Response({"message": "%s liked!" % film.title}, status=status.HTTP_200_OK)

            return Response({"message": "ERROR!"}, status=status.HTTP_400_BAD_REQUEST)



#
# @api_view(['POST'])
# def like(request):
#     if request.method == 'post':
#         id=request.GET.get('id')
#         type=request.GET.get('type')
#
#         if id and type:
#             if type in ['Like', 'Comments']:
#                 model = eval(type)
#                 obj = model.objects.get(id=id)
#                 if obj.likes.filter(user=request.user):
#                     obj.likes.filter(user=request.user).delete()
#
#                     return Response({"message": "%s disliked!" % obj.title}, status=status.HTTP_200_OK)
#                 else:
#                     obj.likes.create(user=request.user)
#                     return Response({"message": "%s liked!" % obj.title}, status=status.HTTP_200_OK)
#         return Response({"message": "ERROR!"}, status=status.HTTP_400_BAD_REQUEST)
#
#








# Create your views here.


# def send_mail_to_all(request):
#     send_mail_func.delay()
#     return HttpResponse("Sent")
#
# def schedule_mail(request):
#     schedule, created = CrontabSchedule.objects.get_or_create(hour = 1, minute = 34)
#     task = PeriodicTask.objects.create(crontab=schedule, name="schedule_mail_task_"+"5", task='send_mail_app.tasks.send_mail_func')#, args = json.dumps([[2,3]]))
#     return HttpResponse("Done")








# class ListFilmView(APIView):
#     def get(self, request , format=None):
#
#         film = Film.objects.filter()

# class APIListCreateFilm(generics.ListCreateAPIView):
#     queryset = Film.objects.all()
#     serializer_class = FilmSerializer
#     # permission_classes = [IsAuthenticated]
#
# class APIRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Film.objects.all()
#     serializer_class = FilmSerializer
#     permission_classes = [IsAuthenticated]