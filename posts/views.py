# from django.shortcuts import render
from django.shortcuts import render, HttpResponse
from api.services.api_posts import ApiPosts


# Create your views here.

def index(request):
    data = ApiPosts.fetch_all_posts()
    return render(request, 'index.html', {'data': data})


def single_post(request, post_id):
    data = ApiPosts.fetch_single_post(post_id)
    return render(request, 'singlePost/singlePost.html', {'data': data, 'post_id': post_id})
