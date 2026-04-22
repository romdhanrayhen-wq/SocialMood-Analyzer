from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

analyzer = SentimentIntensityAnalyzer()

def analyze_sentiment(text):
    scores = analyzer.polarity_scores(text)
    score  = scores['compound']

    positif = round(scores['pos'] * 100, 1)
    negatif = round(scores['neg'] * 100, 1)
    neutre  = round(scores['neu'] * 100, 1)

    if score > 0.05:
        sentiment = 'Positif'
        emoji     = '😊'
        couleur   = 'success'
    elif score < -0.05:
        sentiment = 'Negatif'
        emoji     = '😡'
        couleur   = 'danger'
    else:
        sentiment = 'Neutre'
        emoji     = '😐'
        couleur   = 'warning'

    return {
        'sentiment' : sentiment,
        'emoji'     : emoji,
        'score'     : round(score, 2),
        'confiance' : round(abs(score) * 100, 1),
        'couleur'   : couleur,
        'detail'    : {
            'positif' : positif,
            'negatif' : negatif,
            'neutre'  : neutre,
        }
    }
