###LIB###
import os

from supabase           import create_client
from dotenv             import load_dotenv
from fasthtml.common    import *



###INIT###
load_dotenv()

headers = [Link(rel="icon", href="/public/image/favicon.ico", type="image/x-icon")]

if "prod" == os.getenv("ENV"):
    headers.append(Link(rel="stylesheet", href="/public/css/style.min.css"))
else:
    headers.append(Script(src='https://cdn.tailwindcss.com'))

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
    return Div(
        P(PROJECT_TITLE, cls="bg-zinc-100 text-4xl font-extrabold text-zinc-600"),
        card_players(get_players())
    )



###START###
serve()
