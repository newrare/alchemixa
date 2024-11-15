from fasthtml.common    import *
from model.player       import Player as ModelPlayer



class Player:
    def get_view():
        players = ModelPlayer.get_players()

        results = []

        for player in players:
            results.append(Div(
                P(player.username),
                P(player.mail),
                Hr()
            ))

        return Div(
            * results
        )
