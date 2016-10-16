import requests
from bs4 import BeautifulSoup
import re
import json
import time

headers = {
'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
'Accept-Encoding': 'gzip, deflate, br',
'Connection': 'keep-alive',
'Cookie': '__cfduid=d653bf931cbde10f9243b63e991f70dc41466778585; loid=a5WUnHRHlleKL9OSSR; loidcreated=2016-06-24T14%3A29%3A45.413Z; _recent_srs=t5_2qu49; _ga=GA1.2.54465388.1466778724; pc=ne; __utma=55650728.54465388.1466778724.1466778728.1466843492.2; __utmz=55650728.1466778728.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utmb=55650728.0.10.1466843492; __utmc=55650728',
'Host': 'www.reddit.com',
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:47.0) Gecko/20100101 Firefox/47.0',
}
# url = 'https://www.reddit.com/r/AskReddit/comments/4qfh55/what_are_some_of_the_best_life_tips/'
# url = 'https://www.reddit.com/r/community/comments/2fchpz/what_ever_happened_to_the_deans_dalmatian_fetish/'
url = 'https://www.reddit.com/r/AskReddit/comments/4qfh01/what_are_some_classes_you_must_take_in/'

r = requests.get(url,headers=headers)
r.encoding = r.apparent_encoding
# print r.text

# div class="md"

soup = BeautifulSoup(r.text)
res = soup.select("div.md")
comments = []
for item1 in res[1:]:
    comments.append(item1.contents)
print comments

fd = open('comments.txt','w+')

p_soup = BeautifulSoup(str(comments))
res2 = p_soup.findAll('p')
for item2 in res2:
    ct = str(item2.contents).encode('utf-8')
    print ct[3:-2]
    fd.write(ct[3:-2] + '\n')

fd.close()