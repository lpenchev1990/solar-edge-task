# from django.shortcuts import render
import json

from django.shortcuts import render, HttpResponse
from api.services.api_posts import ApiPosts
from django.http import JsonResponse
# from apiCalls.apiCalls import getDatas
# Create your views here.



def get_comments(request, post_id):
    data = ApiPosts.fetch_comments(post_id)

    return HttpResponse(data, content_type="application/json")

