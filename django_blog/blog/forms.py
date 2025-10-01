from django import forms
from .models import Post, Comment, Tag
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from .models import Profile, Comment

User = get_user_model()

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ("bio", "profile_photo")

class PostForm(forms.ModelForm):

    tags_field = forms.CharField(
        required=False,
        label='Tags (comma separated)',
        widget=forms.TextInput(attrs={'placeholder': 'e.g. django, python, tips'})
    )

    class Meta:
        model = Post
        fields = ['title', 'content']  # author and published_date set automatically
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 10}),
        }

    def __init__(self, *args, **kwargs):
        instance = kwargs.get('instance', None)
        super().__init__(*args, **kwargs)
        if instance:
            # pre-fill tags_field from existing tags
            tag_names = ', '.join([t.name for t in instance.tags.all()])
            self.fields['tags_field'].initial = tag_names

    def clean_tags_field(self):
        value = self.cleaned_data.get('tags_field', '')
        # split by comma, strip whitespace, remove empties, lowercase optional
        tag_names = [t.strip() for t in value.split(',') if t.strip()]
        # optional: enforce max length or valid characters here
        return tag_names

    def save(self, commit=True):
        tag_names = self.cleaned_data.pop('tags_field', [])
        post = super().save(commit=commit)
        # attach tags: create if not exist
        tags = []
        for name in tag_names:
            obj, _created = Tag.objects.get_or_create(name=name)
            tags.append(obj)
        # set tags (replace existing)
        post.tags.set(tags)
        if commit:
            post.save()
        return post


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']  # Only allow editing the content
        widgets = {
            'content': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Write a comment...'})
        }
        labels = {
            'content': ''
        }
