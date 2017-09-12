import csv

import requests

from bs4 import BeautifulSoup
from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.views.generic import TemplateView

from .models import Company


class MainView(TemplateView):
    template_name = 'core/main.html'


def getAddress(soup):
    address = soup.findAll('span', {"class": "addressline"})
    address_final = []
    for addressline in address:
        address_final.append(addressline.text.strip())
    return [x for x in address_final if x]


def getContactDetails(soup):
    other = soup.findAll('div', {"class": "col-sm-6 addresssection rightside"})
    lines = [span.get_text() for span in other]

    if lines:
        line = lines[0].split('\n')
        result = [x for x in line if x]
        phoneInList = result.index(' Phone: ')
        emailInList = result.index(' Email: ')
        siteInList = result.index('Website:')
        number = result[phoneInList + 1]
        email = result[emailInList + 1]
        try:
            site = result[siteInList + 1]
        except IndexError:
            site = None

        return number, email, site
    else:
        return ' ', ' ', ' '


def scrapeLinks(links):
    for link in links:
        request = requests.get(link.get('href'))._content
        soup = BeautifulSoup(request)
        company = soup.h1.text

        number, email, site = getContactDetails(soup)

        Company.objects.create(
            name=company,
            address=getAddress(soup),
            phone=number,
            email=email,
            website=site
        )


def getData(reference):
    search = {
        'FSF': 1,
        'search': reference,
        'TOKEN': '3wq1nht7eg7tr'
    }
    request = requests.get(
        "https://register.fca.org.uk/shpo_searchresultspage?",
        params=search
    )._content
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
        Company.objects.all().delete()
        if data['format'] == 'table':
            scrapeLinks(data['links'])

        data = serializers.serialize("json", Company.objects.all())
        return HttpResponse(data, content_type='application/json')
    else:
        return render_to_response('core/main.html', locals())


def export(request):
    model = Company
    writer = csv.writer(open('test.csv', 'w'))

    headers = []
    for field in model._meta.fields:
        headers.append(field.name)
    writer.writerow(headers)

    for obj in Company.objects.all():
        row = []
        for field in headers:
            val = getattr(obj, field)
            if callable(val):
                val = val()
            row.append(val)
        writer.writerow(row)
    return render_to_response('core/main.html', locals())
