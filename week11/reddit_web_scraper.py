import requests
from bs4 import BeautifulSoup
import time


url = 'https://www.reddit.com/r/technology'

time.sleep(1)

response = requests.get(url)

if response.status_code == 200:

    soup = BeautifulSoup(response.content, 'html.parser')

    posts = soup.select('shreddit-post')

    for post in posts:
        print(f"""
        Title: {post['post-title']})
        Author: {post['author']}
        Posted: {post['created-timestamp']}
        Stats: Score = {post['score']}, Comments = {post['comment-count']}
        Permalink: {post['permalink']}
        """)

else:
    print(f"Failed to retrieve the webpage. Status code: {response.status_code}")