from django.shortcuts import render

def index(request):
    context = {}
    return render(request, 'index.html', context)

def scores(request):
    context = {
        "headings": ["team", "event", "penalty"], 
        "rows": [
            ["team_name", "event_name", 20],
            ["team_name", "event_name", 20],
            ["team_name", "event_name", 20]
        ]
    }
    return render(request, "scores.html", context)