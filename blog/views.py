from django.shortcuts import render
def blog_v(request):
    return render(request, 'blog/blog_v.html', {})

