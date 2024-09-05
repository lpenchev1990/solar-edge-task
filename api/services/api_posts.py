import requests
from urllib3 import request


class ApiPosts:
    BASE_URL = 'https://jsonplaceholder.typicode.com/'

    @staticmethod
    def fetch_all_posts(params=None):
        url = f"{ApiPosts.BASE_URL}/posts"
        response = requests.get(url, params=params)
        return response.json()

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
