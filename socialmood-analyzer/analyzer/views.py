from django.shortcuts import render
from .sentiment import analyze_sentiment
from .models import Analyse
import json

def home(request):
    historique = Analyse.objects.all()[:10]
    total    = Analyse.objects.count()
    positifs = Analyse.objects.filter(sentiment='Positif').count()
    negatifs = Analyse.objects.filter(sentiment='Negatif').count()
    neutres  = Analyse.objects.filter(sentiment='Neutre').count()
    return render(request, 'index.html', {
        'historique' : historique,
        'stats' : {
            'total'    : total,
            'positifs' : positifs,
            'negatifs' : negatifs,
            'neutres'  : neutres,
        }
    })

def analyze(request):
    if request.method == 'POST':
        text = request.POST.get('text', '').strip()
        if not text:
            return render(request, 'index.html', {'erreur': 'Veuillez entrer un texte.'})
        result = analyze_sentiment(text)
        Analyse.objects.create(
            texte     = text,
            sentiment = result['sentiment'],
            score     = result['score']
        )
        return render(request, 'result.html', {
            'text'   : text,
            'result' : result
        })
    return render(request, 'index.html')

def historique(request):
    analyses = Analyse.objects.all()
    return render(request, 'historique.html', {'analyses': analyses})

def dashboard(request):
    analyses = Analyse.objects.all()
    labels = ['Positif', 'Neutre', 'Negatif']
    data   = [
        analyses.filter(sentiment='Positif').count(),
        analyses.filter(sentiment='Neutre').count(),
        analyses.filter(sentiment='Negatif').count(),
    ]
    return render(request, 'dashboard.html', {
        'analyses' : analyses,
        'labels'   : json.dumps(labels),
        'data'     : json.dumps(data),
    })
