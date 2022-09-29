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
    "Management": Team("Management Team", ["Brooks", "Chevy", "Errin", "Kevin", "Lukas", "Andrew"], "Management Team is required to make sure everything around Base Camp is running well and is clean."),
    "Procurement": Team("Procurement Team",["Mike", "Dylan", "Anna", "Zaul", "Luke", "River"], "Procurement Team is required to make sure everyone at Base Camp is fed."),
    "Documentation": Team("Documentation Team",["Colt", "Isaiah", "Cooper", "Cannon", "Angela", "Antonio", "Gabbi"], "Documentation Team is required to make sure everything we do here at Base is captured."),
    "Community": Team("Community Team",["Joshua", "Malcolm", "Amber", "J.W.", "Eric"],"Community Team is required to make sure here at Base Camp we have fun events.")
}

def index_page(request):
    context={
    "lp":["Management", "Procurement", "Documentation", "Community"]}
    return render(request, "index.html",context)




def pages(request, name):
    name = teams[name]
    context = {
        "title": name.title,
        "members": name.members,
        "des": name.des,
    }
    return render(request, "details.html", context)


