from rest_framework import serializers
from .models import Note
from django.contrib.auth.models import User


class NoteSerializer(serializers.ModelSerializer):
    createdBy = serializers.HiddenField(
        default=serializers.CurrentUserDefault())

    class Meta:
        model = Note
        fields = ('id','name', 'note', 'createdBy', 'timeStamp',)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user
