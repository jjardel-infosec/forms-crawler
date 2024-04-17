# Web Crawler Python
This is a web crawler written in Python using asyncio, aiohttp, and BeautifulSoup to find and save forms on web pages.

## Requirements
- Python 3.7 or higher
- Libraries: aiohttp, BeautifulSoup

## Features
- Allows selecting a text file containing a list of URLs to be crawled at limited depth.
- Extracts and saves URLs of forms found on web pages into a text file.

## How to Use
1. Clone the repository or download the `crawler.py` file.
2. Make sure you have Python and the required libraries installed (`aiohttp`, `BeautifulSoup`). You can install the dependencies by running:
    ```
    pip install aiohttp beautifulsoup4
    ```
3. Run the `crawler.py` script.
4. Choose the text file containing the URLs to be crawled.
5. Wait while the web crawler crawls the URLs and saves the forms found.

## Example File Structure
- `crawler.py`: The main script.
- `README.md`: This documentation file.
- `requirements.txt`: Python requirements list file.
- `example_urls.txt`: An example text file containing URLs to be crawled.

## Limitations
- Crawling is limited to a maximum depth of 3.
- Request rate is limited to avoid overloading the server.

## Contribution
Contributions are welcome! If you encounter issues or have suggestions for improvements, feel free to open an issue or submit a pull request.

## License
This project is licensed under the [MIT License]([LICENSE](https://opensource.org/license/mit)).
