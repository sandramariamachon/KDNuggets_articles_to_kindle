# KDNuggets articles Scraper

A script that scrapes the latest articles from my favourite Data Science blog [KDNuggets](https://www.kdnuggets.com/). Scraped articles are converted to PDF file and sent to Kindle. Using Window's "Task Scheduler" (or Mac's "Automator") you can trigger the script daily, for a new batch of the latest articles!

⚙ The scraper is written in ***Python***. Other tools include  ***Beautiful Soup*** (for web scraping), ***Pdfkit*** (for HTML to PDF convertion) and ***MIME*** (to send the PDF file to Kindle).

## Contents
- Python files *scrape_send_final.py*, *send_email.py*, *scrape_article.py* which scrape articles, converts them to PDF and sends it to your Kindle's email address.
- *wkhtmltopdf.exe* which runs alongside pdfkit. Wkhtmltopdf is an open source simple and much effective command-line shell utility that enables user to convert any given HTML (Web Page) to PDF document or an image (jpg, png, etc).
- *scheduled.bat* file which runs the *scrape_send_final.py* and can be run routinely by Task Scheduler (optional step).

## How to use

-  Run *scrape_send_final.py* to scrape the articles and send the email to your Kindle
-  Make sure to insert your sender email and password, as well as Kindle email address in *send_email.py*
-  If you want to run a scraper automatically you can use software such as "Task Scheduler". Check the short video below:

https://user-images.githubusercontent.com/55002027/115935365-f226c000-a48a-11eb-930a-b43aa6d4517a.mp4


## License
MIT
