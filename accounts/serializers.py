from rest_framework import serializers

from .models import MyUser

class MyUserSerializer(serializers.ModelSerializer):
    class Meta:
        pass
        model = MyUser
        # fields = (
        #     'title',
        #     'description',
        #     'director',
        # )
        fields = '__all__'







