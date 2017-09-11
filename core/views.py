import json
import requests

from bs4 import BeautifulSoup
from django.http import HttpResponse
from django.views.generic import TemplateView


class MainView(TemplateView):
    template_name = 'core/main.html'

def getSearchButton(reference):
    search = {
        'search': reference,
        'TOKEN': '3wq1nht7eg7tr'
    }
    request = requests.get("https://register.fca.org.uk/shpo_searchresultspage?", params=search)._content
    soup = BeautifulSoup(request)
    print(soup)

def reference(request):
    if request.method == 'POST' and request.is_ajax():
        button = getSearchButton(int(request._post['ref']))
        return HttpResponse(button, content_type="application/json")
    else :
        return render_to_response('core/main.html', locals())