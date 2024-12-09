from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

monthly_challenges = {
    "january" : "Eat no meat for the entire month",
    "february": "Walk for at least 20 minutes every day!",
    "march": "Learn Django for at least 20 minutes every day!",
 
    "april" : "Walk for at least 20 minutes every day!",
    "may": "Eat no meat for the entire month",
    "june" : "Walk for at least 20 minutes every day!",

    "july": "Learn Django for at least 20 minutes every day!",
    "august": "Eat no meat for the entire month",
    "september" : "Walk for at least 20 minutes every day!",

    "october" : "Learn Django for at least 20 minutes every day!",
    "november": "Eat no meat for the entire month",
    "december": None,
}

# Create your views here.

def index(req):
    return render (req, "challenges/index.html", {
        "months": list(monthly_challenges.keys())
 })

#========== CHALLENGES (GETS MONTH BY NUMBER) ==========
def monthly_challenge_by_number(req, month):
    months = list(monthly_challenges.keys())

    if month > len(months):
        return HttpResponseNotFound("Invalid month!")
    
    redirect_month = months[month - 1]
    redirect_path = reverse("month-challenge", args = [redirect_month] ) #----- /challenges/january
    return HttpResponseRedirect(redirect_path) #-- REDIRECTION

#========== CHALLENGES (GETS MONTH BY MONTH) ==========
def monthly_challenge(req, month):
    try:
        challenge_text = monthly_challenges[month]
        return render(req, "challenges/challenge.html", {
            "text": challenge_text,
            "month": month
        })
    except:
        return HttpResponseNotFound("<h1>This month is not supported</h1>")