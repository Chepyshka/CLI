import requests
from bs4 import BeautifulSoup
from collections import Counter
import re

def fetch_webpage(url):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"Не вдалося отримати сторінку: {e}")
        return None

def analyze_text_content(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    text = soup.get_text()
    words = re.findall(r'\b\w+\b', text.lower())
    word_counts = Counter(words)
    print("Частота появи слів у тексті новини:")
    for word, count in word_counts.most_common(10):
        print(f"{word}: {count}")

def analyze_html_structure(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    tags = [tag.name for tag in soup.find_all()]
    tag_counts = Counter(tags)
    print("\nЧастота появи HTML-тегів:")
    for tag, count in tag_counts.most_common(10):
        print(f"<{tag}>: {count}")


def count_links_and_images(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    links = soup.find_all('a')
    images = soup.find_all('img')
    print(f"\nКількість посилань на сторінці: {len(links)}")
    print(f"Кількість зображень на сторінці: {len(images)}")


def analyze_webpage(url):
    html_content = fetch_webpage(url)
    if html_content:
        analyze_text_content(html_content)
        analyze_html_structure(html_content)
        count_links_and_images(html_content)

if __name__ == "__main__":
    url = input("Введіть URL сторінки новин для аналізу: ")
    analyze_webpage(url)

