import json
import requests

from bs4 import BeautifulSoup
from django.http import HttpResponse
from django.views.generic import TemplateView


class MainView(TemplateView):
    template_name = 'core/main.html'

def scrapeLinks(links):
    print(links)

def getData(reference):
    search = {
        'FSF': 1,
        'search': reference,
        'TOKEN': '3wq1nht7eg7tr'
    }
    request = requests.get("https://register.fca.org.uk/shpo_searchresultspage?", params=search)._content
    soup = BeautifulSoup(request)
    table = soup.find('table', {"id": "SearchResults"})

    if table:
        data = {
            'format': 'table',
            'links': table.findAll('a')

        }
        
        return data

def reference(request):
    if request.method == 'POST' and request.is_ajax():
        data = getData(int(request._post['ref']))

        if data['format'] == 'table':
            scrapeLinks(data['links'])

        return HttpResponse(button, content_type="application/json")
    else :
        return render_to_response('core/main.html', locals())