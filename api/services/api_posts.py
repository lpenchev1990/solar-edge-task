import requests
from urllib3 import request
from django.conf import settings


class ApiPosts:
    BASE_URL = 'https://jsonplaceholder.typicode.com/'
    
    articles_per_page = 20
    @staticmethod
    def fetch_all_posts(page):
        url = f"{ApiPosts.BASE_URL}/posts"
        response = requests.get(url)
        count = 0
        start_from = (page - 1) * settings.ARTICLES_PER_PAGE
        end_at = start_from + settings.ARTICLES_PER_PAGE
        elements_to_show = []
        for item in response.json():
            if start_from <= count < end_at:
                elements_to_show.append(item)
            count += 1
        return {"elements": elements_to_show, 'count': count}

    @staticmethod
    def fetch_single_post( data):
        url = f"{ApiPosts.BASE_URL}/posts/{data}"
        print(url)
        response = requests.get(url)
        return response.json()

    @staticmethod
    def fetch_comments(post_id):
        url = f"{ApiPosts.BASE_URL}/posts/{post_id}/comments"
        response = requests.get(url)
        return response
