from django.shortcuts import render

# Create your views here.
from .models import Post
from .permissions import IsAuthorOrReadOnly # new


from rest_framework import generics , permissions


from .serializers import PostSerializer

class PostList(generics.ListCreateAPIView):
    permission_classes = (IsAuthorOrReadOnly,) # new
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    
    
class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    
    # adding admin permission
    permission_classes = (IsAuthorOrReadOnly,) # new
    # permission_classes = (permissions.IsAdminUser,) #new
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    
    

