import requests
from django.http import HttpResponse
from django.shortcuts import render
def home(request):

    data = requests.get("https://newsapi.org/v2/top-headlines?country=in&category=science&apiKey=e684c8cd563c4ed0a212dac7f22dc105")
    news = (data.json())
    params={"news": news["articles"]}

    return render(request, "index.html", params)



def sports(request):

    data = requests.get("https://newsapi.org/v2/top-headlines?country=in&category=sports&apiKey=e684c8cd563c4ed0a212dac7f22dc105")
    news = (data.json())
    params={"news": news["articles"]}

    return render(request, "index.html", params)


def science(request):

    data = requests.get("https://newsapi.org/v2/top-headlines?country=in&category=science&apiKey=e684c8cd563c4ed0a212dac7f22dc105")
    news = (data.json())
    params={"news": news["articles"]}

    return render(request, "index.html", params)


def entertainment(request):

    data = requests.get("https://newsapi.org/v2/top-headlines?country=in&category=entertainment&apiKey=e684c8cd563c4ed0a212dac7f22dc105")
    news = (data.json())
    params={"news": news["articles"]}

    return render(request, "index.html", params)



def business(request):

    data = requests.get("https://newsapi.org/v2/top-headlines?country=in&category=business&apiKey=e684c8cd563c4ed0a212dac7f22dc105")
    news = (data.json())
    params={"news": news["articles"]}

    return render(request, "index.html", params)
