from django.shortcuts import render
from dataclasses import dataclass
from typing import List

# Create your views here.

@dataclass 
class Team:
    title: str
    members: list
    des: str


teams = {
    "Management": Team("Management Team", ["Brooks", "Chevy", "Errin", "Kevin", "Lukas", "Andrew"], "They"),
    "Procurement": Team("Procurement Team",["Mike", "Dylan", "Anna", "Zaul", "Luke", "River"], "They"),
    "Documentation": Team("Documentation Team",["Colt", "Isaiah", "Cooper", "Cannon", "Angela", "Antonio", "Gabriel"], "They"),
    "Community": Team("Community Team",["Joshua", "Malcolm", "Amber", "J.W.", "Eric"],"They")
}

#Home Page 
def home_page(request):
#Returning my list into my home page
    context={
    "lp":["Management", "Procurement", "Documentation", "Community"]}
    return render(request, "home.html",context)


def pages(request, name):
    name = teams[name]
    context = {
        "title": name.title,
        "members": name.members,
        "des": name.des,
    }
    return render(request, "details.html", context)


