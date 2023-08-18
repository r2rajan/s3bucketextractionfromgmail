# Scrape email messages in gmail for any s3 bucket links and print the sender and the bucketname
from redbox import gmail
from redbox.query import BODY, SUBJECT, ALL
from urlextract import URLExtract
from urllib.parse import urlparse

def urlextraction(msgbody):
    extractor = URLExtract()
    urls = extractor.find_urls(msg.text_body)
    for each_url in urls: 
        url=urlparse(each_url)
        if url.hostname:
            return url.hostname
        
def extractbucketname(url):
    if s3host in url:
        s3_bucketname=url.split('.')[0]
        return s3_bucketname

# Set credentials
gmail.username = "myemail@gmail.com"
gmail.password = "myappsecret"
inbox = gmail["INBOX"]
s3host="s3.amazonaws.com"

# Search and process messages
msgs = inbox.search(BODY ("s3.amazonaws.com") )

for msg in msgs:
    #x=urlextraction(msg.text_body)
    s3bucket=extractbucketname(urlextraction(msg.text_body))
    if s3bucket:
        print(msg.from_, s3bucket)
