import requests
from bs4 import BeautifulSoup
import chardet

# URL of the Project Gutenberg page
url = "https://www.gutenberg.org/files/164/164-h/164-h.htm"
try:
    # Fetch the content of the URL
    response = requests.get(url)
    response.raise_for_status()  # This will raise an exception for HTTP errors
    
    # Detect encoding if not provided by the server
    if 'charset' in response.headers.get('Content-Type', ''):
        encoding = response.encoding
    else:
        detected_encoding = chardet.detect(response.content)
        encoding = detected_encoding['encoding']
    
    # Use detected encoding to decode the response content
    html_content = response.content.decode(encoding)

    # Use BeautifulSoup to parse HTML content
    soup = BeautifulSoup(html_content, 'html.parser')

    # Find the main text of the book; Gutenberg HTML often has the text within <body> or specific <div>
    # You might need to adjust the selection method based on specific structure of the HTML page
    main_text = soup.find('body')
    if main_text:
        text = main_text.get_text(separator='\n', strip=True)
    else:
        text = soup.get_text(separator='\n', strip=True)

    # Save the extracted text to a .txt file
    with open('output.txt', 'w', encoding='utf-8') as file:
        file.write(text)

    print("Text has been saved to output.txt")

except requests.exceptions.RequestException as e:
    print(f"An error occurred while fetching the URL: {e}")
except Exception as e:
    print(f"An error occurred: {e}")


# with open('output.txt', 'r', encoding='utf-8') as file:
#     text = file.read()
#     print(text)