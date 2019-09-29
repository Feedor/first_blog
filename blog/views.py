from django.utils import timezone
from django.shortcuts import render
from blog.models import Post
def blog_v(request):
    posts = Post.objects.filter(pulikate_date__lte = timezone.now()).order_by("-create_date")
    return render(request, 'blog/blog_v.html', {"posts":posts})

