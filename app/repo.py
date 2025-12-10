from .content import Content
import requests


def get(schema: str, **kwargs):
    content = Content()
    res = requests.get('')
    return content


def filter(schema: str, **kwargs):
    content = Content()
    return [content]
