from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
from datetime import date
from datetime import timedelta 
import scrape_article 
import send_email 
import os

yesterday = str((date.today() - timedelta(days = 1))).split("-") #['YEAR', 'MONTH', 'DAY'], ['2021', '03', '27']
date_to_scrape = yesterday #['2021', '03', '05'] #for custom scrape date
date_to_scrape[1] = date_to_scrape[1].lstrip('0')
date_to_scrape[2] = date_to_scrape[2].lstrip('0') 

SITE = "https://www.kdnuggets.com/news/index.html"
HDR = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/7046A194A'}

print("Please wait!")

def month_to_num(month):
     return {
            'Jan' : "1",
            'Feb' : "2",
            'Mar' : "3",
            'Apr' : "4",
            'May' : "5",
            'Jun' : "6",
            'Jul' : "7",
            'Aug' : "8",
            'Sep' : "9", 
            'Oct' : "10",
            'Nov' : "11",
            'Dec' : "12"
    }[month]

def clean_up_date(text):
    for ch in ['-',',','.']:
        text = text.replace(ch, "")
    return text
 

#main page scraping:
req = Request(SITE, headers = HDR)
page = urlopen(req)
soup = BeautifulSoup(page, 'html.parser')
articles_holder = soup.find(class_="three_ul")  #three_ul holds all articles
all_links = articles_holder.find_all("li")
all_dates = articles_holder.find_all("font")


index = 0
list_of_urls = []
for element in all_dates:
    date = clean_up_date(element.get_text()).split(" ")
    date.pop(0) #removes the first element which is empty (due to the way the website is set up)
    if(month_to_num(date[0]) == date_to_scrape[1] and date[1] == date_to_scrape[2] and date[2] == date_to_scrape[0]):
        list_of_urls.append( [all_links[index].a['href'], all_links[index].a.b.get_text()])  
    index = index + 1

#print(list_of_urls)
print("Scraping completed!")
file_name = ("KDnuggets articles from " + date_to_scrape[0] + "-" + date_to_scrape[1] + '-' + date_to_scrape[2] + ".pdf")
scrape_article.scrape_articles(list_of_urls, file_name) # call to receive the article preformatted...
print("pdf saved!")
send_email.send_to_kindle(file_name) 
os.remove(file_name)