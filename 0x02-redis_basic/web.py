#!/usr/bin/env python3
"Implements an expiring web cache and tracker"""
from functools import wraps
from typing import Callable
import redis
import requests

redis_client = redis.Redis()


def url_count(method: Callable) -> Callable:
    """Counts the no. of times a url is accessed"""
    @wraps(method)
    def wrapper(url):
        redis_client.incr(f'count:{url}')
        cached_html = redis_client.get(f'cached:{url}')
        if cached_html:
            return cached_html.decode('utf-8')
        html = method(url)
        redis_client.setex(f'cached:{url}', 10, html)
        return html

    return wrapper


@url_count
def get_page(url: str) -> str:
    """Obtain the HTML content of a URL"""
    response = requests.get(url)
    return response.text
