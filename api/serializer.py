from rest_framework import serializers

from app.models import Todo

class TodoSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Todo
        # fields = '__all__'
        fields = ['id','name','status']