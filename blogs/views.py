from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Blog, Category

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