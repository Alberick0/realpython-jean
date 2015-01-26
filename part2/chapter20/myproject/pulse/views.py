from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader, Context
import requests, json
from pulse.forms import PulseForm

# Create your views here.
def index(request):
    form = PulseForm
    return render(request, 'index.html', {'form': form})


def pulser(request):
    if request.method == 'GET':
        return redirect('/pulses/')
    else:
        url = 'http://text-processing.com/api/sentiment/'
        text = {'text': request.POST.get('pulse')}
        response = requests.post(url, text)
        data = {'label': json.loads(response.content), 'pulse': text}
        t = loader.get_template('pulser.html')
        c = Context(data)
        return HttpResponse(t.render(c))

# import django
# django.setup()