from django.http import HttpResponse
from django.template import loader
from .models import Keyword

def index(request):
    if 'keyword' in request.POST:
        keyword = request.POST['keyword']
        results = Keyword.objects.filter(name=keyword).select_related()
    else:
        results = None

    keywords = Keyword.objects.select_related()
    template = loader.get_template('keywords.html')
    context = {
        'keywords': keywords,
        'results': results,
    }

    return HttpResponse(template.render(context, request))
