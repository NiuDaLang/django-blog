from django.shortcuts import render
from blogs.models import Category, Blog

def home(request):
  # categories = Category.objects.all()
  featured_posts = Blog.objects.filter(is_featured=True, status='Published').order_by('-upcated_at')
  posts = Blog.objects.filter(is_featured=False, status='Published').order_by('-upcated_at')
  context = {
    # 'categories': categories,
    'featured_posts': featured_posts,
    'posts': posts,
  }
  return render(request, "home.html", context)