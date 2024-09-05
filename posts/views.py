# from django.shortcuts import render
from django.shortcuts import render, HttpResponse
from api.services.api_posts import ApiPosts
from django.conf import settings


# Create your views here.

def index(request):
    return get_posts(request,1)

def all_posts(request, page_number):
    return get_posts(request,page_number)

def get_posts(request, page):
    pagination_pages = []
    data = ApiPosts.fetch_all_posts(int(page))
    if data['count'] > 0:
        all_pages = int(data['count']/settings.ARTICLES_PER_PAGE)
        pagination_pages = generate_pagination_numbers(int(page), all_pages)
    return render(request, 'index.html', {'data': data['elements'], 'current_page': int(page), 'pagination_pages': pagination_pages})



def generate_pagination_numbers(page, all_pages):

    # Initialize an empty list for pages
    pages_list = []

    # Calculate the two previous pages
    first_previous = page - 2
    second_previous = page - 1

    # Add previous pages to the list if they are within the valid range
    if first_previous > 0:
        pages_list.append(first_previous)
    if second_previous > 0:
        pages_list.append(second_previous)

    # Add the current page to the list if it is within the valid range
    if 0 < page <= all_pages:
        pages_list.append(page)

    # Calculate the two next pages
    first_next = page + 1
    second_next = page + 2

    # Add next pages to the list if they are within the valid range
    if first_next <= all_pages:
        pages_list.append(first_next)
    if second_next <= all_pages:
        pages_list.append(second_next)

    return pages_list


def single_post(request, post_id):
    data = ApiPosts.fetch_single_post(post_id)
    return render(request, 'singlePost/singlePost.html', {'data': data, 'post_id': post_id})
