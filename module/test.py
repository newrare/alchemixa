import os

from dotenv                 import load_dotenv
from starlette.testclient   import TestClient

from module.translate       import Translate

load_dotenv()



class Test:
    is_already_tested: bool = False



    @classmethod
    def check(cls, is_test, app) -> None:
        #check if is_test is necessary
        if "dev" != os.getenv("ENV") or is_test == False or cls.is_already_tested:
            return None

        #not testing specific routes
        exceptions  = [
            '/live-reload',
            '/{fname:path}.{ext:static}',
            '/lang/{lang}'
        ]

        #start testing
        client = TestClient(app)

        for route in app.routes:
            route_test = route.path

            if route_test in exceptions:
                continue

            response_code = client.get(route_test).status_code

            if response_code == 200:
                print('OK: ' + route_test)
            else:
                print('ERROR: ' + route_test)

        #dont forget to test langs
        langs = Translate.availlables

        for route in langs:
            response_code = client.post('/lang/' + route).status_code

            if response_code == 200:
                print('OK: /lang/' + route)
            else:
                print('ERROR: /lang/' + route)

        #set is_already_tested to True
        cls.is_already_tested = True

        return None
