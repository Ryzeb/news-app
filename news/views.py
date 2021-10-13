from django.shortcuts import render
from newsapi import *
from newsapi import NewsApiClient
def index(request):
    newsapi = NewsApiClient(api_key=" f3309bfa72364626903822e9b0d06b1b")
    topheadlines = newsapi.get_top_headlines(sources='google-news-in')
    articles = topheadlines['articles']
    desc = []
    news = []
    img = []
    for i in range(len(articles)):
        myarticles = articles[i]
        news.append(myarticles['title'])
        desc.append(myarticles['description'])
        img.append(myarticles['urlToImage'])
    mylist = zip(news,desc,img)
    return render(request, 'index.html', context = {"mylist":mylist})

def bbc(request):
    newsapi = NewsApiClient(api_key=" f3309bfa72364626903822e9b0d06b1b")
    l = newsapi.get_top_headlines(sources='reuters')
    articles = l['articles']
    desc = []
    news = []
    img =  []
    for i in range(len(articles)):
        myarticles = articles[i]
        news.append(myarticles['title'])
        desc.append(myarticles['description'])
        img.append(myarticles['urlToImage'])
    mylist = zip(news, desc, img)
    return render(request ,'bbc.html',context = {"mylist":mylist})

def sports(request):
    newsapi = NewsApiClient(api_key=" f3309bfa72364626903822e9b0d06b1b")
    l = newsapi.get_top_headlines(sources='bbc-sport')
    articles = l['articles']
    desc = []
    news = []
    img = []
    for i in range(len(articles)):
        myarticles = articles[i]
        news.append(myarticles['title'])
        desc.append(myarticles['description'])
        img.append(myarticles['urlToImage'])
    mylist = zip(news, desc, img)
    return render(request, 'sports.html', context={"mylist": mylist})
def business(request):
    newsapi = NewsApiClient(api_key=" f3309bfa72364626903822e9b0d06b1b")
    l = newsapi.get_top_headlines(sources='business-insider')
    articles = l['articles']
    desc = []
    news = []
    img = []
    for i in range(len(articles)):
        myarticles = articles[i]
        news.append(myarticles['title'])
        desc.append(myarticles['description'])
        img.append(myarticles['urlToImage'])
    mylist = zip(news, desc, img)
    return render(request, 'business.html', context={"mylist": mylist})
def tech(request):
    newsapi = NewsApiClient(api_key=" f3309bfa72364626903822e9b0d06b1b")
    l = newsapi.get_top_headlines(sources='techcrunch')
    articles = l['articles']
    desc = []
    news = []
    img = []
    for i in range(len(articles)):
        myarticles = articles[i]
        news.append(myarticles['title'])
        desc.append(myarticles['description'])
        img.append(myarticles['urlToImage'])
    mylist = zip(news, desc, img)
    return render(request, 'tech.html', context={"mylist": mylist})




# Create your views here.
