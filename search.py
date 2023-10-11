import os
import aiohttp
from bs4 import BeautifulSoup

async def make_request(url):
    headers = {
        'Ocp-Apim-Subscription-Key': os.environ['BING_API_KEY']
    }
    async with aiohttp.ClientSession(headers=headers) as session:
        async with session.get(url) as response:
            if response.status == 200:
                return await response.text()
            else:
                return ''

def parse_results(html):
    soup = BeautifulSoup(html, 'html.parser')
    results = []
    for tag in soup.find_all('a'):
        url = tag.get('href')
        if url is None or not url.startswith('http'):
            continue
        title_tag = tag.find('h2')
        if title_tag is None:
            continue
        title = title_tag.get_text()
        description_tag = tag.find('p')
        description = ''
        if description_tag is not None:
            description = description_tag.get_text()
        results.append({'url': url, 'title': title, 'description': description})
    return results

async def search(query):
    url = f'https://bing.com/search?q={query}&count=10'
    html = await make_request(url)
    return parse_results(html)