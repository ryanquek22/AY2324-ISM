from bs4 import BeautifulSoup
import csv
import chardet
import nltk

nltk.download('punkt')

from nltk.tokenize import sent_tokenize

# file path to html document
html_document_path = r"data/tsla-20231231.html"

print("reading HTML Doc")
# Load the HTML document
with open(html_document_path, 'r', encoding='Windows-1252') as file:
    html_content = file.read()
#print(html_content)


soup = BeautifulSoup(html_content, 'html.parser')
all_text = soup.get_text(separator=' ', strip=True)

sentences = sent_tokenize(all_text)

#sentences = soup.find('span')

with open('html_ouptut.txt', 'w', encoding='utf-8') as output_file:
    for sentence in sentences:
        output_file.write(f"{sentence}\n")
