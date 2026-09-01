from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Project, BlogPost
from .forms import ProjectForm, BlogPostForm


def dashboard_login(request):
    if request.user.is_authenticated:
        return redirect('dashboard_index')
    error = None
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard_index')
        else:
            error = 'Invalid username or password.'
    return render(request, 'dashboard/login.html', {'error': error})


@login_required
def dashboard_logout(request):
    logout(request)
    return redirect('dashboard_login')


@login_required
def dashboard_index(request):
    project_count = Project.objects.count()
    blog_count = BlogPost.objects.count()
    recent_posts = BlogPost.objects.all()[:5]
    return render(request, 'dashboard/index.html', {
        'project_count': project_count,
        'blog_count': blog_count,
        'recent_posts': recent_posts,
    })


# ---- Projects ----

@login_required
def project_list(request):
    projects = Project.objects.all()
    return render(request, 'dashboard/project_list.html', {'projects': projects})


@login_required
def project_create(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard_project_list')
    else:
        form = ProjectForm()
    return render(request, 'dashboard/project_form.html', {'form': form, 'action': 'New'})


@login_required
def project_edit(request, pk):
    project = get_object_or_404(Project, pk=pk)
    if request.method == 'POST':
        form = ProjectForm(request.POST, instance=project)
        if form.is_valid():
            form.save()
            return redirect('dashboard_project_list')
    else:
        form = ProjectForm(instance=project)
    return render(request, 'dashboard/project_form.html', {'form': form, 'action': 'Edit', 'project': project})


@login_required
def project_delete(request, pk):
    project = get_object_or_404(Project, pk=pk)
    if request.method == 'POST':
        project.delete()
        return redirect('dashboard_project_list')
    return render(request, 'dashboard/confirm_delete.html', {'object': project, 'type': 'project'})


# ---- Blog ----

@login_required
def blog_list(request):
    posts = BlogPost.objects.all()
    return render(request, 'dashboard/blog_list.html', {'posts': posts})


@login_required
def blog_create(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard_blog_list')
    else:
        form = BlogPostForm()
    return render(request, 'dashboard/blog_form.html', {'form': form, 'action': 'New'})


@login_required
def blog_edit(request, pk):
    post = get_object_or_404(BlogPost, pk=pk)
    if request.method == 'POST':
        form = BlogPostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('dashboard_blog_list')
    else:
        form = BlogPostForm(instance=post)
    return render(request, 'dashboard/blog_form.html', {'form': form, 'action': 'Edit', 'post': post})


@login_required
def blog_delete(request, pk):
    post = get_object_or_404(BlogPost, pk=pk)
    if request.method == 'POST':
        post.delete()
        return redirect('dashboard_blog_list')
    return render(request, 'dashboard/confirm_delete.html', {'object': post, 'type': 'blog'})
