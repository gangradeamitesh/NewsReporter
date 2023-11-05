import requests
from bs4 import BeautifulSoup as bs
def get_bbc_text(url):
    response = requests.get(url)

    if response.status_code == 200:
        para = ""
        soup = bs(response.content , 'html.parser')
        #article = soup.find('div', class_='lx-stream-asset gel-layout gel-layout--no-flex')
        article = soup.find(id="main-content")
        article_paragraph = soup.find_all('div',class_='ssrcss-7uxr49-RichTextContainer e5tfeyi1')
        if article:
            for paragraph in article_paragraph:
                para += paragraph.get_text()
            return para
        else:
            return "Article Content not found"
    else:
        return "Failed"

