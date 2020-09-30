from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework import generics
from django.contrib.auth.models import User


# Create your views here.
def index(request):
    return render(request, 'index.html')


class NoteViewSet(viewsets.ModelViewSet):
    queryset = Note.objects.all()
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = NoteSerializer

    def get_queryset(self):
        # filtered by its owner and return the queryset
        owner_queryset = self.queryset.filter(createdBy=self.request.user)
        return owner_queryset


class UserCreate(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.AllowAny, )
