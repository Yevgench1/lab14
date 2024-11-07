import requests
from bs4 import BeautifulSoup
import os
from urllib.parse import urljoin, urlparse

def download_images(url, folder='images'):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        if not os.path.exists(folder):
            os.makedirs(folder)
        
        img_tags = soup.find_all('img')
        for img in img_tags:
            img_url = img.get('src')
            if not img_url:
                continue
            img_url = urljoin(url, img_url)
            img_name = os.path.basename(urlparse(img_url).path)
            img_data = requests.get(img_url).content
            with open(os.path.join(folder, img_name), 'wb') as img_file:
                img_file.write(img_data)
    except Exception as e:
        print(f"Error downloading images from {url}: {e}")

def main():
    with open('address.txt', 'r') as file:
        urls = file.read().split(',')
    
    for url in urls:
        url = url.strip()
        download_images(url)

if __name__ == "__main__":
    main()
