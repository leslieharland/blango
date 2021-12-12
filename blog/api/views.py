from rest_framework import generics

from blog.api.serializers import PostSerializer
from blog.models import Post
from django.contrib.auth.models import User
from blog.api.serializers import PostSerializer, UserSerializer
from rest_framework.authentication import SessionAuthentication


class PostList(generics.ListCreateAPIView):
    authentication_classes = [SessionAuthentication]
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class UserDetail(generics.RetrieveAPIView):
    lookup_field = "email"
    queryset = User.objects.all()
    serializer_class = UserSerializer
