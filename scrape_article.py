from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
from urllib.parse import urljoin  
import io
import os
import pdfkit #requires pip install pdfkit as well as https://wkhtmltopdf.org/downloads.html

SITE = "https://www.kdnuggets.com/news/index.html"
HDR = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/7046A194A'}
ABSOLUTE_PATH = "https://www.kdnuggets.com"
 
# Utility function
'''def convert_html_to_pdf(source_html, output_filename): 
    result_file = open(output_filename, "w+b") # open output file for writing (truncated binary) 
    pisa_status = pisa.CreatePDF(    # convert HTML to PDF
            source_html,                # the HTML to convert
            dest=result_file)           # file handle to recieve result  
    result_file.close()                 # close output file
    return pisa_status.err  # return False on success and True on errors'''

def get_article_to_content(url):
    article_page = urlopen(Request(url, headers = HDR))
    article_soup = BeautifulSoup(article_page, 'html.parser')
    article = article_soup.find_all(id = "post-") 
    article_absolute = str(article)
    all_images = article[0].find_all('img') 
    all_href = article[0].find_all(href=True) 
    for image in all_images:   
        absolute_image = urljoin(ABSOLUTE_PATH, image['src']) 
        article_absolute = article_absolute.replace(image['src'], absolute_image)
    for href in all_href:
        absolute_href = urljoin(ABSOLUTE_PATH, href['href'])  
        article_absolute = article_absolute.replace(href['href'], absolute_href)
    return article_absolute

     
def scrape_articles(articles_info, file_name):
    pdf_content = ""
    for article_info in articles_info:
        pdf_content = pdf_content + "<h1>" + article_info[1] + "</h1>" + get_article_to_content(article_info[0])[1:-1]
    options = { #important:https://pypi.org/project/pdfkit/
        'page-size': 'Letter',
        'margin-top': '0.75in',
        'margin-right': '0.75in',
        'margin-bottom': '0.75in',
        'margin-left': '0.75in',
        'encoding': "UTF-8"
    }
    pdfkit.from_string(pdf_content, file_name, options = options)

# to test internally
'''temp_url_list = [
  "https://www.kdnuggets.com/2021/03/mongodb-icloud-solutions-2021.html",
  "https://www.kdnuggets.com/2021/03/overview-mlops.html",
  "https://www.kdnuggets.com/2021/03/multilingual-clip--huggingface-pytorch-lightning.html"
    ]
scrape_articles(temp_url_list, 'DONE.pdf')'''
 
