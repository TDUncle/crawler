import requests
import re
url = "http://zuimeia.com"
r = requests.get('http://zuimeia.com/community/app/hot/?platform=2')
pattern = re.compile(r'<a class="community-app-cover-wrapper" href="(.*?)" target="_blank">')
urlList = pattern.findall(r.content)

def requestsUrl(url):
    r = requests.get(url)
    title = re.findall(r'"app-title"><h1>(.*?)</h1>',r.content)
    #print title
    category = re.findall(r'<a class="app-tag" href="/community/app/category/title/.*?/?platform=2">(.*?)</a>',r.content)
    #print category
    
    describe = re.findall(r'<div id="article_content">(.*?)<div class="community-image-wrapper">',r.content)
    #print type(describe[0])
    strdescribe = srtReplace(describe[0])
    #print strdescribe
    
    downloadUrl = re.findall(r'<a class="download-button direct hidden" href="(.*?)"',r.content)
    #print downloadUrl

    return title,category,strdescribe,downloadUrl


def srtReplace(string):
    listReplace = ['<p>', '<br>', '<h1>', '<h2>', '<h3>', '<h4>', '<h5>', '<h6>', '<h7>','<strong>','</p>', '<br/>', '</h1>', '</h2>', '</h3>', '</h4>', '</h5>',
                   '</h6>', '</h7>','</strong>','<b>', '</b>']
    for eachListReplace in listReplace:
        string = string.replace(str(eachListReplace),'\n')

    string = string.replace('\n\n','')
    return string

def categornFinal(category):
    categoryFinal =''
    for eachCategory in category:
        categoryFinal = categoryFinal+str(eachCategory)+'-->'
    return categoryFinal

def urlReplace(url):
    url = url.replace('&amp;', '&')
    return url

requestsUrl("http://zuimeia.com/community/app/27369/?platform=2")
for eachUrl in urlList:
    eachUrl = url+eachUrl
    content = requestsUrl(eachUrl)
    categoryFinal =''
    
    title = content[0][0]
    category = categornFinal(content[1])
    strdescribe = content[2]
    downloadUrl = urlReplace(content[3][0])

    with open('c:/wqa.txt', 'a+') as fd:
        fd.write('title:'+title+'\n'+'category:'+category+'\n'+'strdescribe:'+strdescribe+'\n'+'downloadUrl:'+downloadUrl+'\n\n\n-----------------------------------------------------------------------------------------------------------------------------\n\n\n')


    
    
    
    


