# Create your views here.
from models import Post
from django.shortcuts import render_to_response, get_object_or_404

def list_posts(request):
    posts = Post.objects.all().order_by('-published_date')
    return render_to_response("posts/list_posts.html", {'posts': posts})

def post_detail(request, post_id):
    post = get_object_or_404(Post, pk = post_id)
    return render_to_response("posts/post_detail.html", {'post': post})
