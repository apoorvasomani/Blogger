from django.shortcuts import render
from api.models import Post
from rest_framework import generics
from api import serializers


class PostList(generics.ListCreateAPIView):
	queryset = Post.objects.all()
	serializer_class = serializers.PostSerializer

	def perform_create(self, serializer):
		serializer.save()


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Post.objects.all()
	serializer_class = serializers.PostSerializer