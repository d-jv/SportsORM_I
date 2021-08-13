from django.shortcuts import render, redirect
from .models import League, Team, Player

from . import team_maker

def index(request):
	context = {
		"leagues": League.objects.all(),
		"teams": Team.objects.all(),
		"players": Player.objects.all(),
	}
	return render(request, "leagues/index.html", context)

def make_data(request):
	team_maker.gen_leagues(10)
	team_maker.gen_teams(50)
	team_maker.gen_players(200)

	return redirect("index")

###########################################

def home(request):
	return render(request, 'home.html')

def leagues(request):
	data = {
		'leagues': League.objects.all(),
		'baseballs' : League.objects.filter(name__contains='Baseball'),
		'wleagues' : League.objects.filter(name__contains='Womens'),
		'anyHockeys' : League.objects.filter(name__contains='Hockey'),
		'noFootballs' : League.objects.exclude(name__contains='Football'),
		'conferences' : League.objects.filter(name__contains='conference'),
	}
	return render(request, 'leagues.html', data)

def teams(request):
	data = {
		'teams' : Team.objects.all(),
		'hqDallas' : Team.objects.filter(location__contains = 'Dallas'),
		'cityLocs' : Team.objects.filter(location__contains = 'City'),
		'tTeams' : Team.objects.filter(location__startswith = 'T'),
		'ascLocs' : Team.objects.all().order_by('location'),
		'descTNames' : Team.objects.all().order_by('-team_name'),
	}
	return render(request, 'teams.html', data)

def players(request):
	data = {
		'players' : Player.objects.all(),
		'coopers' : Player.objects.filter(last_name__contains = 'Cooper'),
		'joshuas' : Player.objects.filter(first_name__contains = 'Joshua'),
		'coopNotJs' : Player.objects.filter(last_name__contains = 'Cooper') & Player.objects.exclude(first_name__contains = 'Joshua'),
		'alexWyatts' : Player.objects.filter(first_name__contains = 'Alexander') | Player.objects.filter(first_name__contains = 'Wyatt'),
	}
	return render(request, 'players.html', data)


def showLeague(request, league_id):
	league = League.objects.get(id=league_id)
	return redirect(request.META.get('HTTP_REFERER'))