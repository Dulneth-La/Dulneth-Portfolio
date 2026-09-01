from django import forms
from .models import Project, BlogPost, ContactMessage


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'description', 'technologies', 'github_url', 'project_url', 'featured']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'dash-input', 'placeholder': 'Project title'}),
            'description': forms.Textarea(attrs={'class': 'dash-input', 'rows': 4, 'placeholder': 'Describe your project...'}),
            'technologies': forms.TextInput(attrs={'class': 'dash-input', 'placeholder': 'Python, Django, JavaScript'}),
            'github_url': forms.URLInput(attrs={'class': 'dash-input', 'placeholder': 'https://github.com/...'}),
            'project_url': forms.URLInput(attrs={'class': 'dash-input', 'placeholder': 'https://...'}),
            'featured': forms.CheckboxInput(attrs={'class': 'dash-checkbox'}),
        }


class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'category', 'difficulty', 'summary', 'content']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'dash-input', 'placeholder': 'e.g. HackTheBox - Jerry'}),
            'category': forms.Select(attrs={'class': 'dash-select'}),
            'difficulty': forms.Select(attrs={'class': 'dash-select'}),
            'summary': forms.TextInput(attrs={'class': 'dash-input', 'placeholder': 'Short description for blog cards...'}),
            'content': forms.Textarea(attrs={'class': 'dash-input dash-textarea', 'rows': 15, 'placeholder': 'Write your walkthrough in Markdown...'}),
        }


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'subject', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'contact-input', 'placeholder': 'Your name'}),
            'email': forms.EmailInput(attrs={'class': 'contact-input', 'placeholder': 'your@email.com'}),
            'subject': forms.TextInput(attrs={'class': 'contact-input', 'placeholder': 'Subject'}),
            'message': forms.Textarea(attrs={'class': 'contact-input contact-textarea', 'rows': 6, 'placeholder': 'Write your message...'}),
        }
