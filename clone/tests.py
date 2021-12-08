from django.test import TestCase
from .models import Profile, Image, Comment

# Create your tests here.
class ProfileTestClass(TestCase):
    #setUp method
    def setUp(self):
        self.valentino=Profile(profile_name="Valentino", profile_photo="https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.gq.com%2Fstory%2Finstagram-feed-chronology&psig=AOvVaw3JAlqBZqM8_HHn4GlDZBfM&ust=1639067591238000&source=images&cd=vfe&ved=0CAsQjRxqFwoTCPiMp97Q1PQCFQAAAAAdAAAAABAO", bio="flowers")

    def test_instance(self):
        self.assertTrue(isinstance(self.valentino, Profile))

    def test_save_method(self):
        self.valentino.save_profile()
        profiles=Profile.objects.all()
        self.assertTrue(len(profiles) > 0)

    def test_delete_profile(self):
        self.john=Profile(profile_name="Junior", profile_photo="https://www.pexels.com/photo/person-holding-phone-while-logging-in-on-instagram-application-174938/", bio="Man holding a phone")
        self.junior.save_profile()

        profiles=Profile.objects.all()
        self.john.delete_profile()
        self.assertEqual(len(profiles), 0)


class CommentTestClass(TestCase):
    #setup method

    def setUp(self):
        self.commentone=Comment(comment="Awesome stuff")

    def test_instance(self):
        self.assertTrue(isinstance(self.commentone, Comment))

    def test_save_method(self):
        self.commentone.save_comment()
        comments=Comment.objects.all()
        self.assertTrue(len(comments) > 0)

    def test_delete_comment(self):
        self.commentone=Comment(comment="i love the creativity")
        self.commentone.save_comment()

        comments=Comment.objects.all()
        self.commentone.delete_comment()
        self.assertEqual(len(comments),0)

class ImageTestClass(TestCase):
    #setUp method

    def setUp(self):
        self.valentino=Profile(profile_name="valentino", profile_photo="https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.theverge.com%2F2020%2F8%2F19%2F21373809%2Finstagram-suggested-posts-update-end-feed&psig=AOvVaw3JAlqBZqM8_HHn4GlDZBfM&ust=1639067591238000&source=images&cd=vfe&ved=0CAsQjRxqFwoTCPiMp97Q1PQCFQAAAAAdAAAAABAJ", bio="Cool Cat")
        self.valentino.save_profile()

        self.commentone=Comment(comment="Great Picture")
        self.commentone.save_comment()

        self.imageone=Image(image="https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.computerhope.com%2Fjargon%2Fi%2Finstagram.htm&psig=AOvVaw3JAlqBZqM8_HHn4GlDZBfM&ust=1639067591238000&source=images&cd=vfe&ved=0CAsQjRxqFwoTCPiMp97Q1PQCFQAAAAAdAAAAABAD", image_name="Log into IG", caption="Man holding phone to log in to IG", profile=self.valentino, comments=self.commentone, likes=4)
        self.imageone.save_image()

    def test_instance(self):
        self.assertTrue(isinstance(self.imageone, Image))

    def tearDown(self):
        Profile.objects.all().delete()
        Comment.objects.all().delete()
        Image.objects.all().delete()

    def test_save_image(self):
        self.imageone.save_image()
        images=Image.objects.all()
        self.assertTrue(len(images) > 0)

    def test_delete_image(self):
        images=Image.objects.all()

        self.imageone.delete_image()
        self.assertEqual(len(images), 0)

    def test_update_caption(self):
        self.imageone.save_image()
        Image.update_caption(Image, caption="That is so fun", new_caption="Man logged into IG")    
        Image.objects.filter(caption="Georgeous").update(caption="No one is born genius, just work smart")
        self.assertTrue(Image.objects.get(caption="I love her creativity"))


    
