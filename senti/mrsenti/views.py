from django.shortcuts import render
from django.http import HttpResponse
from textblob import TextBlob
import requests
# Create your views here.


def index(request):
    
    context = {'req_post': False}

    template_name = '1.html'
    if request.POST:
        req_post = True
        string_to_analyze = request.POST['senti_string']
        txtblob = TextBlob(string_to_analyze)
        senti_score = txtblob.sentiment
        polarity = txtblob.sentiment.polarity
        if polarity > 0:
            polarity_type = '+ve'
        else:
            polarity_type = '-ve'
        if polarity_type == '+ve':
            pole = 1
            context = {'senti': senti_score, 'polarity': polarity,'pole':pole, 'req_post': req_post}
        else:
            pole = 0
            context = {'senti': senti_score, 'polarity': polarity,'pole':pole, 'req_post': req_post}
    return render(request, template_name, context)

def fbsenti(request):
    code = str(request.GET['code'])
    resp = requests.get('https://graph.facebook.com/v2.3/oauth/access_token? \
        client_id=<Your Client Id here>& \
        redirect_uri=http://localhost:8000/fbsenti& \
        client_secret=<Your Client secret here>&code='+code)
    access_token = str(resp.json()['access_token'])
    user = requests.get('https://graph.facebook.com/me?access_token='+access_token)
    user_id = user.json()['id']
    user_name = user.json()['name']
    statuses = requests.get('https://graph.facebook.com/me/statuses?access_token='+access_token)
    fb_status_message = []
    for post in statuses.json()['data']:
        fb_status_message.append(post['message'])
    # import ipdb;ipdb.set_trace();
    return HttpResponse(fb_status_message)

