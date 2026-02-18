#!/usr/bin/python3
"""
restful-api.task_02_requests
"""
import requests
import csv


def fetch_and_print_posts():
    """
    fetch_and_print_posts
    """
    url = "https://jsonplaceholder.typicode.com/posts"
    x = requests.get(url)
    print(f"Status Code: {x.status_code}")

    if x.status_code == 200:
        posts = x.json()
        for i in posts:
            print(i['title'])


def fetch_and_save_posts():
    """
    fetch_and_save_posts
    """
    url = "https://jsonplaceholder.typicode.com/posts"
    x = requests.get(url)

    if x.status_code == 200:
        posts = x.json()
        data = []
        for i in posts:
            item = {
                'id': i['id'],
                'title': i['title'],
                'body': i['body']
            }
            data.append(item)
        with open('posts.csv', 'w', newline='', encoding='utf-8') as csvfile:
            field = ['id', 'title', 'body']
            writer = csv.DictWriter(csvfile, fieldnames=field)
            writer.writeheader()
            writer.writerows(data)
