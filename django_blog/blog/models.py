from django.conf import settings
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="posts")
    
    class Meta:
        ordering = ['-published_date']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        # Used by CreateView/UpdateView success_url fallback
        return reverse('post-detail', kwargs={'pk': self.pk})

class Profile(models.Model):
    """Extended user profile stored separately so we don't change the AUTH_USER_MODEL."""
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    profile_photo = models.ImageField(upload_to="profile_photos/", null=True, blank=True)

    def __str__(self):
        return f"Profile: {self.user.username}"


# Create / save profile automatically when user is created
@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    else:
        instance.profile.save()
