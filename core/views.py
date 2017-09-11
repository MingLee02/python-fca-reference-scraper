import json

from django.http import HttpResponse
from django.views.generic import TemplateView


class MainView(TemplateView):
    template_name = 'core/main.html'

def reference(request):
    print(int(request._post['ref']))

    if request.method == 'POST' and request.is_ajax():
        return HttpResponse(json.dumps({'name': 'SUCCESS'}), content_type="application/json")
    else :
        return render_to_response('core/main.html', locals())