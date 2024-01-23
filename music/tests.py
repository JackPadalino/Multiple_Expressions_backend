from django.test import TestCase
from django.contrib.auth.models import User
from .models import Tag, Track, Video

class MusicTests(TestCase):
    def setUp(self):
        self.test_user1 = User.objects.create_user(
            username='testuser1',
            password='testpassword'
        )

        self.test_user2 = User.objects.create_user(
            username='testuser2',
            password='testpassword'
        )

        self.test_user3 = User.objects.create_user(
            username='testuser3',
            password='testpassword'
        )

    def test_tag_creation(self):
        new_tag = Tag.objects.create(title='Techno')
        self.assertTrue(Tag.objects.filter(title='Techno').exists())
        self.assertEqual(str(new_tag), 'Techno')

    def test_track_creation(self):
        new_track = Track.objects.create(
            title='Test Track',
            file='test.mp3',
            track_photo='test.jpg',
            upload_date='2022-01-01',
        )
        new_track.users.add(self.test_user1,self.test_user2)
        new_track.tags.create(title='Techno')

        self.assertTrue(Track.objects.filter(title='Test Track').exists())
        self.assertEqual(str(new_track), 'Test Track (Tags: Techno, Users: testuser1, testuser2)')

    def test_track_deletion(self):
        new_track = Track.objects.create(
            title='Test Track',
            file='test.mp3',
            track_photo='test.jpg',
            upload_date='2022-01-01',
        )

        self.assertTrue(Track.objects.filter(title='Test Track').exists())
        new_track.delete()
        self.assertFalse(Track.objects.filter(title='Test Track').exists())

    def test_video_creation(self):
        new_video = Video.objects.create(
            title='Test Video',
            file='test.mp4',
            upload_date='2022-01-01',
        )
        new_video.users.add(self.test_user1,self.test_user2)

        new_video.tags.create(title='Techno')

        self.assertTrue(Video.objects.filter(title='Test Video').exists())
        self.assertEqual(str(new_video), 'Test Video (Tags: Techno, Users: testuser1, testuser2)')

    def test_video_deletion(self):
        new_video = Video.objects.create(
            title='Test Video',
            file='test.mp4',
            upload_date='2022-01-01',
        )

        new_video.users.add(self.test_user1)

        # verify that the video exists and is associated with the user
        self.assertTrue(Video.objects.filter(title='Test Video').exists())
        self.assertIn(self.test_user1, new_video.users.all())

        # get the video ID before deletion and then delete
        video_id = new_video.id

        # delete the video then verify that the video no longer exists
        new_video.delete()
        self.assertFalse(Video.objects.filter(title='Test Video').exists())

        # attempting to access the deleted video's users should raise DoesNotExist
        with self.assertRaises(Video.DoesNotExist):
            deleted_video = Video.objects.get(id=video_id)
            users_after_deletion = deleted_video.users.all()


    def test_track_user_association(self):
        new_track = Track.objects.create(
            title='Test Track',
            file='test.mp3',
            track_photo='test.jpg',
            upload_date='2022-01-01',
        )

        # associate only user1 and user2 with the track
        new_track.users.add(self.test_user1, self.test_user2)

        # verify the associations with users 1 and 2 and not 3
        self.assertIn(self.test_user1, new_track.users.all())
        self.assertIn(self.test_user2, new_track.users.all())
        self.assertNotIn(self.test_user3, new_track.users.all())
