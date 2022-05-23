from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from api.serializer import TodoSerializer
from app.models import Todo

class TodoViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all().order_by('count')
    serializer_class = TodoSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Todo.objects.filter(user=self.request.user.id).all().order_by('count')

    def perform_create(self, serializer):
        serializer.save(user=User.objects.get(pk=self.request.user.id),count=Todo.objects.filter(user=1).count())

    @action(detail=False, methods=['post'])
    def sort(self, request):
        
        ids = request.POST.get('ids').split(",") # [3,10,3,45,70] 
        # print(ids[1])

        for i, t in enumerate(ids):
            print("{} - {}".format(i, t))
            Todo.objects.filter(pk=t).update(count=i)

        return Response("ok")

    @action(detail=False, methods=['delete']) # url_path='borrar'
    def delete(self, request):
        Todo.objects.filter(user=request.user.id).delete()
        return Response("ok")
