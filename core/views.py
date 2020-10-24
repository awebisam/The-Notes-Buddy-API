from django.shortcuts import render
from .models import Note
from .serializers import NoteSerializer, UserSerializer
from rest_framework import viewsets
from rest_framework import permissions
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

# Create your views here.
def index(request):
    return render(request, 'index.html')

class NoteViewSet(viewsets.ModelViewSet):
    queryset = Note.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = NoteSerializer

    def get_queryset(self):
        # filtered by its owner and return the queryset
        owner_queryset = self.queryset.filter(createdBy=self.request.user)
        return owner_queryset


class UserCreate(viewsets.ModelViewSet):
    http_methods_name = ["post"]
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.AllowAny, )

    def create(self,request):
        resp = super().create(request)
        user = User.objects.get(username = resp.data['username'])
        token, created = Token.objects.get_or_create(user=user)
        resp.data['token'] = token.key
        return resp