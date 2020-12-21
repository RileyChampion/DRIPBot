
import requests
from bs4 import BeautifulSoup

async def scrap_site(URL):
    # URL = input('Enter site URL:')
    headers = requests.utils.default_headers()
    headers.update({
        'User-Agent': 'Mozilla/5.0 (Linux; Android 5.1.1; SM-G928X Build/LMY47X) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.83 Mobile Safari/537.36',
    })

    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    result = soup.find('h1')
    if(result == None):
        print("Website is not compabtible with current version of bot.\nPlease look forward to future iterations.")
        exit()
    item_name = result.text

    result = soup.findAll('img')

    item_url = ""

    for img in result:
        if img.has_attr('alt') and item_name.strip() in img['alt']:
            item_image = img
            break
    if(item_image.has_attr('data-original-src')):
        item_url = item_image['data-original-src']
    elif(item_image.has_attr('src')):
        item_url = item_image['src']
    
    
    return [item_name, (item_url if "https:" in item_url else "https:" + item_url)]