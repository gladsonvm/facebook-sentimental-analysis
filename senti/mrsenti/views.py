from django.shortcuts import render
from textblob import TextBlob
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