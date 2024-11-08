###LIB###
import os

from supabase           import create_client
from dotenv             import load_dotenv
from fasthtml.common    import *



###INIT###
load_dotenv()

header = [
    Script(code='', src='https://cdn.tailwindcss.com'),
    Link(rel="icon", href="/public/image/favicon.ico", type="image/x-icon")
]

app, rt     = fast_app(live=True, hdrs=header)
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
    return Div(
        *[Div(
            P(player.get("username")),
            P(player.get("mail")),
            Hr()
        ) for player in players]
    )

def card_style(title, image_url, description):
    return Div(
        Div(
            Img(src=image_url, _class="w-full h-48 object-cover"),
            Div(
                H2(title, _class="text-xl font-bold mb-2"),
                P(description, _class="text-gray-700 text-base"),
                _class="p-4"
            ),
            _class="bg-white shadow-md rounded-lg overflow-hidden"
        ),
        _class="max-w-sm mx-auto"
    )



###ROUTE###
@rt('/')
def get():
    return Div(
        P(PROJECT_TITLE),
        card_players(get_players()),
        card_style("Title", "/public/image/favicon.ico", "Description")
    )



###START###
serve()
