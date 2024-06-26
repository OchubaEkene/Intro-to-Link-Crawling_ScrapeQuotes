# Install necessary libraries
import requests
from bs4 import BeautifulSoup
import time
import pandas as pd


def scrape_page(url):
    # Handle HTTP Requests
    response = requests.get(url)
    response.raise_for_status()  # Raise an exception for HTTP errors

    # Parse HTML
    soup = BeautifulSoup(response.content, 'html.parser')

    # Create Variable to hold data
    quotes_data = []

    # Fetch Divs that contain necessary data
    divs = soup.find_all('div', class_='quote')

    # Loop through all divs to fetch out data
    for div in divs:
        quote = div.find('span', class_='text').text
        author = div.find('small', class_='author').text
        tags = [tag.text for tag in div.find_all('a', class_='tag')]

        quotes_data.append({
            'quote': quote,
            'author': author,
            'tags': ', '.join(tags),  # Join tags into a single string
            'page_url': url
        })

    return quotes_data


def main(max_depth=10):
    base_url = 'http://quotes.toscrape.com/page/'
    all_quotes = []
    page_number = 1

    while page_number <= max_depth:
        url = f'{base_url}{page_number}/'
        print(f'Scraping {url}...')
        quotes_data = scrape_page(url)
        if not quotes_data:  # If no quotes are found, break the loop
            break
        all_quotes.extend(quotes_data)
        page_number += 1
        time.sleep(2)  # Be respectful to the server by adding a delay between requests

    # Save data to a CSV file
    df = pd.DataFrame(all_quotes)
    df.to_csv('quotes.csv', index=False)
    print('Data saved to quotes.csv')


if __name__ == '__main__':
    main(max_depth=10)  # change the max_depth parameter to control the depth
