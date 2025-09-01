from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Blog, Category
from django.db.models import Q


# Create your views here.
def posts_by_category(request, category_id):
  # return HttpResponse('Post by Category')
  posts = Blog.objects.filter(status="Published", category=category_id)

  # Use try/except when you want to do some customized action when 404
  # try:
  #   category = Category.objects.get(pk=category_id)
  # except:
  #   return redirect("home")
  
  # Use get_object_or_404 when you want to show 404 error page
  category = get_object_or_404(Category, pk=category_id)
  context = {
    'posts': posts,
    'category': category,
  }
  return render(request, "posts_by_category.html", context)


def blogs(request, slug):
  single_blog = get_object_or_404(Blog, slug=slug, status="Published")
  context = {
    "single_blog": single_blog,
  }

  return render(request, "blogs.html", context)


def search(request):
  keyword = request.GET.get('keyword')
  blogs = Blog.objects.filter(
    Q(title__icontains=keyword) | 
    Q(short_description__icontains=keyword) | 
    Q(blog_body__icontains=keyword), 
    status='Published')
  context = {
    'blogs': blogs,
    'keyword': keyword
  }
  return render(request, 'search.html', context)