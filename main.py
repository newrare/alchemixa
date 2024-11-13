###LIB###
import os

from supabase           import create_client
from dotenv             import load_dotenv
from fasthtml.common    import *;
from view.title         import Title



###INIT###
load_dotenv()

headers = [Link(rel="icon", href="/public/image/favicon.ico", type="image/x-icon")]

if "prod" == os.getenv("ENV"):
    headers.append(Link(rel="stylesheet", href="/public/css/animate.min.css"))
    headers.append(Link(rel="stylesheet", href="/public/css/style.min.css"))
else:
    headers.append(Script(src='https://cdn.tailwindcss.com'))
    headers.append(Link(rel="stylesheet", href="https://cdnjs.cloudflare.com/ajax/libs/animate.css/4.1.1/animate.min.css"))

app, rt     = fast_app(live=True, hdrs=headers)
supabase    = create_client(
    os.getenv("SUPABASE_URL"),
    os.getenv("SUPABASE_KEY")
)



###CONSTANT###
PROJECT_TITLE = "Alchemixa"



###METHOD###
def get_players():
    response = supabase.table("player").select("*").execute()

    return response.data

def card_players(players):
    results = []

    for player in players:
        results.append(Div(
            P(player.get("username")),
            P(player.get("mail")),
            Hr()
        ))

    return Div(
        * results
    )



###ROUTE###
@rt('/')
def get():
    return Title.get_view()

@rt('/players')
def get():
    return Div(
        card_players(get_players())
    )



###START###
serve()
