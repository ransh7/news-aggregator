import requests
from django.shortcuts import render, redirect
from bs4 import BeautifulSoup as BSoup
from news.models import Headline
    
def scrape(request):
  session = requests.Session()
  session.headers = {"User-Agent": "Googlebot/2.1 (+http://www.google.com/bot.html)"}
  url = "https://timesofindia.indiatimes.com/briefs"

  content = session.get(url, verify=False).content
  soup = BSoup(content, "html.parser")
  News = soup.find_all('div', {"class":"brief_box"})
  for i in range(0,60):
    if i%6 == 4:
      continue 
    article = News[i]
    link = "https://timesofindia.indiatimes.com" + article.h2.a['href']
    title = article.h2.text
    text = article.p.text
    new_headline = Headline()
    new_headline.title = title
    new_headline.url = link
    new_headline.text = text
    new_headline.save()
  return redirect("../")

def news_list(request):
    headlines = Headline.objects.all()[::-1]
    context = {
        'object_list': headlines,
    }
    return render(request, "news/home.html", context)