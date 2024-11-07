import requests
from bs4 import BeautifulSoup
import json

def count_headings(url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        counts = {}
        for i in range(1, 7):
            tag = f'h{i}'
            counts[tag] = len(soup.find_all(tag))
        return counts
    except Exception as e:
        return {"error": str(e)}

def main():
    with open('address.txt', 'r') as file:
        urls = file.read().split(',')
    results = {}

    for url in urls:
        url = url.strip()
        results[url] = count_headings(url)
    
    with open('results.json', 'w') as json_file:
        json.dump(results, json_file, indent=4, ensure_ascii=False)

if __name__ == "__main__":
    main()
