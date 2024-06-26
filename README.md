# Intro-to-Link-Crawling_ScrapeQuotes
 Scrape Quotes, Authors, Tags, and links of quotes website.

## Steps Taken:

### Install necessary libraries
> Requests, BeautifulSoup, Time, Pandas

### Handle HTTP Requests
> Using Requests

### Parse HTML
> Using BeautifulSoup

### Create Variable to hold data
> quotes_data = []

### Loop through all divs to fetch out data
> for div in divs:

### Create Function to handle Pagination
> def main():

### Use Max_depth to implement depth limit
> def main(max_depth=10):

### Scrape all pages and respect the server by adding a delay
> page_number += 1
> time.sleep(2)

### Save data to a CSV file
> df = pd.DataFrame(all_quotes)
> df.to_csv('quotes.csv', index=False)
> print('Data saved to quotes.csv')

### Ensure that the code is executed only when the script is run directly, and not when it is imported as a module in another script, with max_depth
> if __name__ == '__main__':
    main(max_depth=10)
