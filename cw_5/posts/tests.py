from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Post

User = get_user_model()

class PostModelTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.post = Post.objects.create(
            title='Test Post',
            description='This is a test post.',
            author=self.user
        )

    def test_post_creation(self):
        self.assertEqual(self.post.title, 'Test Post')
        self.assertEqual(self.post.description, 'This is a test post.')
        self.assertEqual(self.post.author, self.user)

    def test_post_str(self):
        self.assertEqual(str(self.post), 'Test Post')

    def test_post_author(self):
        self.assertEqual(self.post.author.username, 'testuser')