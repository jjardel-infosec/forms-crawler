import aiohttp
import asyncio
from bs4 import BeautifulSoup
from urllib.parse import urlparse, urljoin
import time
import os

visited_urls = set()
max_depth = 3  # Maximum recursion depth
concurrent_requests = 10  # Number of concurrent requests
crawl_delay = 1  # Delay between requests to avoid overloading the server

async def fetch(url):
    async with aiohttp.ClientSession() as session:
        try:
            async with session.get(url, allow_redirects=True, timeout=10) as response:
                if response.status == 200:
                    return await response.text()
                else:
                    return None
        except Exception as e:
            return None

def get_internal_links(url, html_content):
    internal_links = set()
    soup = BeautifulSoup(html_content, 'html.parser')
    for link in soup.find_all('a', href=True):
        next_url = urljoin(url, link['href'])
        parsed_next_url = urlparse(next_url)
        if parsed_next_url.scheme and parsed_next_url.netloc == urlparse(url).netloc:
            internal_links.add(next_url)
    return internal_links

async def crawl(url, depth, file_path):
    if depth <= max_depth and url not in visited_urls:
        visited_urls.add(url)
        html_content = await fetch(url)
        if html_content:
            soup = BeautifulSoup(html_content, 'html.parser')
            forms = soup.find_all('form')
            input_texts = soup.find_all('input', {'type': 'text'})
            if forms or input_texts:
                print("\033[92mForm Found\033[0m:", url)  # Green color for "Form Found" message
                save_form(url, file_path)
            internal_links = get_internal_links(url, html_content)
            await asyncio.gather(*[crawl(link, depth + 1, file_path) for link in internal_links])

def save_form(url, file_path):
    file_name = os.path.basename(file_path)
    file_name_without_extension = os.path.splitext(file_name)[0]
    save_path = os.path.join('/home/kali/path/to-save', file_name_without_extension + "_forms.txt")
    with open(save_path, 'a') as file:
        #file.write("URL: {}\n".format(url))
        file.write("{}\n".format(url))  # Escrever apenas a URL
        file.write("\n")

async def main():
    directory_path = '/home/kali/path-to-read/files/'
    files = sorted(os.listdir(directory_path))  # Organize files alphabetically
    print("Select a file to crawl or exit:")
    for i, file_name in enumerate(files, 1):
        print(f"{i}. {file_name}")
    print(f"{len(files) + 1}. Exit")
    while True:
        try:
            choice = int(input("Enter your choice (1-%d): " % (len(files) + 1)))
            if choice == len(files) + 1:
                return
            elif 1 <= choice <= len(files):
                file_path = os.path.join(directory_path, files[choice - 1])
                break
            else:
                print("Invalid choice. Please enter a number between 1 and", len(files) + 1)
        except ValueError:
            print("Invalid choice. Please enter a number.")

    with open(file_path, 'r') as file:
        links = file.readlines()
    for link in links:
        link = link.strip()
        await crawl(link, 0, file_path)

if __name__ == "__main__":
    start_time = time.time()
    asyncio.run(main())
    print("Execution time:", round(time.time() - start_time, 2), "seconds")
