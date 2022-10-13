from django.shortcuts import redirect, render, get_object_or_404
from .forms import BlogForm
from .models import Blog

# Create your views here.

def index(request):
    blogs = Blog.objects.all()
    context = {
        'blogs':blogs
    }
    return render(request, 'index.html', context)

def blog(request):
    form = BlogForm(request.POST)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return redirect('index')
    
    context = {
        'form': BlogForm
    }

    return render(request, 'forms.html', context)

def update_blog(request, id):
    instance = get_object_or_404(Blog, id=id)
    form = BlogForm(request.POST or None, instance=instance)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.save()
        return redirect('index')
    context = {
        'form': form
    }
    return render(request, 'forms.html', context)

def delete_blog(request, id):
    instance = get_object_or_404(Blog, id=id)
    instance.delete()
    return redirect('index')
