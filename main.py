###LIB###
import os

from dotenv                 import load_dotenv
from fasthtml.common        import *;
from starlette.testclient   import TestClient

from module.translate       import Translate
from view.player            import Player       as View_player
from view.title             import Title        as View_title



###ENV###
#GLOBAL_CONSTANT = 'value'
load_dotenv()



###HEADER###
headers = [
    Title(os.getenv("PROJECT_TITLE")),
    Link(rel = 'icon', href = '/public/image/favicon.ico', type = 'image/x-icon')
]

if "prod" == os.getenv("ENV"):
    headers.append(Link(rel = 'stylesheet', type = 'text/css', href = '/public/css/animate.min.css'))
    headers.append(Link(rel = 'stylesheet', type = 'text/css', href = '/public/css/style.min.css'))
else:
    headers.append(Script(src = 'https://cdn.tailwindcss.com'))
    headers.append(Link(rel = 'stylesheet', href = "https://cdnjs.cloudflare.com/ajax/libs/animate.css/4.1.1/animate.min.css"))



###APP###
debug = False

if "dev" == os.getenv("ENV"):
    debug = True

app, rt = fast_app(
    debug   = debug,
    live    = True,
    pico    = False,
    hdrs    = headers
)





###ROUTE###
@rt('/')
def get():
    return View_title.get_view()

@rt('/players')
def get():
    return View_player.get_view()

@rt('/test')
def get():
    msg = Translate.get(key = 'price', value= '50', number = 1, lang = 'fr')

    return Div(
        P(msg, cls = 'text-2xl'),
    )



###TEST###
is_test: bool = False

if "dev" == os.getenv("ENV") and is_test:
    client = TestClient(app)

    print(client.get('/'))



###RUN###
serve()
