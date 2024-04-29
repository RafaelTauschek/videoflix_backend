import os
from django.views.decorators.cache import cache_page
from django.shortcuts import get_object_or_404
from django.conf import settings
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from rest_framework.authtoken.views import APIView, Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from .serializers import VideoSerializer
from .models import Video
import logging

logger = logging.getLogger(__name__)

VIDEO_FOLDER = './media/videos'
CACHE_TTL = getattr(settings, 'CACHE_TTL', DEFAULT_TIMEOUT)


class VideoView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, pk=None, format=None):
        print(request)
        if pk:
            video = get_object_or_404(Video, pk=pk)
            resolutions = get_video_resolutions(video)
            data = {
                'video': VideoSerializer(video).data,
                'resolutions': resolutions
            }
            return Response(data, status=status.HTTP_200_OK)
        else:
            videos = Video.objects.all()
            serializer = VideoSerializer(videos, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
    
    @cache_page(CACHE_TTL)
    def post(self, request, format=None):
        logger.debug("POST request data: %s", request.data)
        serializer = VideoSerializer(data=request.data, context={'request': request})
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    @cache_page(CACHE_TTL)
    def patch(self, request, pk=None, format=None):
        instance = get_object_or_404(Video, pk=pk)
        serializer = VideoSerializer(instance, data=request.data, context={'request': request})
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    @cache_page(CACHE_TTL)
    def put(self, request, pk=None, format=None):
        instance = get_object_or_404(Video, pk=pk)
        serializer = VideoSerializer(instance, data=request.data, context={'request': request})
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk=None, format=None):
        instance = get_object_or_404(Video, pk=pk)
        serializer = VideoSerializer(instance, context={'request': request})
        if serializer.is_valid(raise_exception=True):
            serializer.delete()
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

def get_video_resolutions(video):
    resolutions = {}
    base_filename = os.path.splitext(os.path.basename(video.video_file.path))[0]
    for resolution in ['360p', '720p', '1080p']:
        filename = f'{base_filename}_{resolution}.mp4'
        filepath = os.path.join(VIDEO_FOLDER, filename)
        if os.path.exists(filepath):
            resolutions[resolution] = filepath
    return resolutions
    
    

