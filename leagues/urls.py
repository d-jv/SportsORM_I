from django.urls import path
from . import views

urlpatterns = [
	path('', views.home),
	path('index', views.index, name="index"),
	path('initialize', views.make_data, name="make_data"),
	path('leagues', views.leagues),
	path('leagues/<int:league_id>', views.showLeague),
	path('teams', views.teams),
	path('players', views.players),
]
