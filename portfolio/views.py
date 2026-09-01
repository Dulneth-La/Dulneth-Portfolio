from django.shortcuts import render, get_object_or_404, redirect
from django.core.mail import send_mail
from django.conf import settings
from django.utils.safestring import mark_safe
import markdown
from .models import Project, BlogPost
from .forms import ContactForm


def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def projects(request):
    projects = Project.objects.all()
    projects_data = []
    for p in projects:
        tech_list = [t.strip() for t in p.technologies.split(',') if t.strip()]
        projects_data.append({'project': p, 'tech_list': tech_list})

    return render(request, 'projects.html', {
        'projects_data': projects_data
    })


def blog_list(request):
    posts = BlogPost.objects.all()
    category = request.GET.get('category')
    if category:
        posts = posts.filter(category=category)
    return render(request, 'blog_list.html', {
        'posts': posts,
        'current_category': category,
    })


def blog_post(request, slug):
    post = get_object_or_404(BlogPost, slug=slug)
    md = markdown.Markdown(extensions=['fenced_code', 'codehilite', 'tables', 'nl2br'])
    post_html = md.convert(post.content)
    return render(request, 'blog_post.html', {
        'post': post,
        'content_html': mark_safe(post_html),
    })


def contact(request):
    success = False
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact_msg = form.save()

            send_mail(
                subject=f"Portfolio Contact: {contact_msg.subject}",
                message=f"From: {contact_msg.name} <{contact_msg.email}>\n\n{contact_msg.message}",
                from_email=contact_msg.email,
                recipient_list=[settings.CONTACT_EMAIL],
                fail_silently=False,
            )

            success = True
            form = ContactForm()
    else:
        form = ContactForm()

    return render(request, 'contact.html', {'form': form, 'success': success})
