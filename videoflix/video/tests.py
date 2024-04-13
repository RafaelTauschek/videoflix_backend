from django.test import TestCase, Client
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from .models import Video
from rest_framework import status
from django.urls import reverse
from django.core.files.uploadedfile import SimpleUploadedFile
from user.models import CustomUser


class AuthenticatedClient(Client):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.token = None

    def authenticate(self, user):
        self.token = Token.objects.create(user=user)
        self.defaults['HTTP_AUTHORIZATION'] = 'Token ' + self.token.key


class VideoViewTest(TestCase):
    def setUp(self):
        self.client = AuthenticatedClient()
        self.user = CustomUser.objects.create_user(email='test@test.de', password='TEst123!')
        self.client.authenticate(self.user)

    def test_get_video(self):
        response = self.client.get('/videos/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)


    def test_get_single_video(self):
        video_file = SimpleUploadedFile('video.mp4', b"file_content", content_type='video/mp4')
        video = Video.objects.create(
            title='Test Video',
            description='Test video description',
            video_file=video_file,
            fsk=0,
            duration_time=120
        )
        response = self.client.get(f'/videos/{video.pk}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        

def test_create_video(self):
    video_data = {
        'title': 'New Test Video',
        'description': 'New test video description',
        'fsk': 12,
        'duration_time': 150
    }
    response = self.client.post(reverse('video-list'), video_data)
    self.assertEqual(response.status_code, status.HTTP_200_OK)


def test_update_video(self):
    video_file = SimpleUploadedFile('video.mp4', b"file_content", content_type='video/mp4')
    video = Video.objects.create(
        title='Test Video',
        description='Test video description',
        video_file=video_file,
        fsk=0,
        duration_time=120
    )
    updated_data = {
        'title': 'Updated Test Video',
        'description': 'Updated test video description',
        'fsk': 16,
        'duration_time': 180
    }
    response = self.client.put(reverse('video-detail', kwargs={'pk': video.pk}), updated_data, content_type='application/json')
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    video.refresh_from_db()
    self.assertEqual(video.title, 'Updated Test Video')

def test_partial_update_video(self):
    video_file = SimpleUploadedFile('video.mp4', b"file_content", content_type='video/mp4')
    video = Video.objects.create(
        title='Test Video',
        description='Test video description',
        video_file=video_file,
        fsk=0,
        duration_time=120
    )
    partial_data = {
        'title': 'Partial Update Test Video',
        'fsk': 12,
    }
    response = self.client.patch(reverse('video-detail', kwargs={'pk': video.pk}), partial_data, content_type='application/json')
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    video.refresh_from_db()
    self.assertEqual(video.title, 'Partial Update Test Video')


def test_delete_video(self):
    video_file = SimpleUploadedFile('video.mp4', b"file_content", content_type='video/mp4')
    video = Video.objects.create(
        title='Test Video',
        description='Test video description',
        video_file=video_file,
        fsk=0,
        duration_time=120
    )
    response = self.client.delete(reverse('video-detail', kwargs={'pk': video.pk}))
    self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
    self.assertEqual(Video.objects.count(), 0)

    


