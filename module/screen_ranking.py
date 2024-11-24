from fasthtml.common        import *
from module.model_player    import Model_player



class Screen_ranking:

    @classmethod
    def view_content(cls, lang: str = 'en'):
        players = Model_player.get_players()

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
