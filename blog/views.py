from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from blog.models import Post

def blog_v(request):
    posts = Post.objects.filter(pulikate_date__lte = timezone.now()).order_by("-create_date")
    return render(request, 'blog/blog_v.html', {"posts":posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post}) 

