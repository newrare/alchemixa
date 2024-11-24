###LIB###
import os

from dotenv                 import load_dotenv
from fasthtml.common        import *;
from functools              import wraps

from module.screen_ranking  import Screen_ranking
from module.screen_title    import Screen_title
from module.test            import Test
from module.translate       import Translate



###ENV###
load_dotenv()



###HEADER###
headers = [
    Title(os.getenv("PROJECT_TITLE")),
    Link(rel = 'preconnect',    href = 'https://fonts.googleapis.com'),
    Link(rel = 'preconnect',    href = 'https://fonts.gstatic.com', crossorigin=''),
    Link(rel = 'stylesheet',    href = 'https://fonts.googleapis.com/css2?family=Grenze+Gotisch:wght@100..900&family=New+Rocker&display=swap'),
    Link(rel = 'icon',          href = '/public/image/favicon.ico', type = 'image/x-icon'),
    Link(rel = 'stylesheet',    href = '/public/css/global.css',    type = 'text/css')
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
    live    = False,
    pico    = False,
    hdrs    = headers
)



###MIDDLEWARE###
def middleware_security(f):
    @wraps(f)
    async def decorator(*args, **kwargs): #session or request is also possible before *args
        #print('Code your security for admin routes here!')
        return await f(*args, **kwargs)
    return decorator



###ROUTE###
@rt('/', name = 'screen_title')
def get(session):
    return Screen_title.view_content(session.get('lang'))



@rt('/lang/{lang}')
def post(session, lang: str):
    Translate.use(session, lang)

    return Screen_title.view_content(lang)



@rt('/ranking', name = 'screen_ranking')
def get(session):
    return Screen_ranking.view_content(session.get('lang'))



@rt('/options', name = 'screen_title_option')
def get(session):
    return Screen_title.view_option(session.get('lang'))



@rt('/admin', name = 'admin')
@middleware_security
async def get():
    return P('Admin')



###TEST###
@rt('/test')
def get(session):
    return P('Test')



is_test: bool = False
Test.check(is_test, app)



###RUN###
serve()
