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
        Div(
            Ul(
                Li("New game"),
                Li("Continue"),
                Li("Options"),
                A(
                    Li("Players"),
                    href='/players',
                    cls='hover:text-blue-500'
                ),
                Li("Credits"),
                cls='font-extrabold text-orange-50 text-2xl text-right italic mx-16'
            ),
            cls='w-screen h-screen bg-orange-700/50 grid grid-cols-1 content-end pb-16'
        ),
        cls='w-screen h-screen bg-no-repeat bg-center bg-cover bg-[url("/public/image/home.jpeg")]'
    )

@rt('/players')
def get():
    return Div(
        card_players(get_players())
    )

###START###
serve()
