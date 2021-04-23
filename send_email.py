import smtplib
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import formatdate
from email import encoders

def send_to_kindle(file_name): 
    msg = MIMEMultipart()
    send_from = msg['From'] = 'xxxxxxxxx@gmail.com'
    PASSWORD = "xxxxxxxx"
    send_to = msg['To'] = 'xxxxxxxxx@kindle.com' # Can be 'Send to Kindle' email
    msg['Date'] = formatdate(localtime=True)
    msg['Subject'] = "Latest articles from kdnuggets"
    fp = open(file_name, "rb")
    pdf_file = MIMEApplication(fp.read())
    fp.close()
    encoders.encode_base64(pdf_file)
    pdf_file.add_header('Content-Disposition', "attachment; filename=" + file_name)
    msg.attach(pdf_file) 
    # Send the email
    try:
        server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
        server.ehlo()
        #server.starttls()
        server.login(send_from, PASSWORD)   #make sure to enable less secure apps in google preferences: https://myaccount.google.com/lesssecureapps
        server.sendmail(send_from, send_to, msg.as_string())
        server.close()
        print( 'successfully sent the mail' )
    except Exception as e:
        print(e)
