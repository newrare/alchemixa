import os

from dotenv             import load_dotenv
from fasthtml.common    import A

from module.translate   import Translate

load_dotenv()



class Component_link:
    def __init__(
            self,
            href    : str   = '#',
            key     : str   = None,
            text    : str   = None,
            color   : str   = os.getenv('COLOR_PRIMARY'),
            blank   : bool  = False,
        ) -> None:

        self.href   = href
        self.key    = key
        self.text   = text
        self.color  = color
        self.blank  = blank



    def __str__(self) -> str:
        return str(self.component())



    def do(self) -> A:
        target = ''

        if self.blank:
            target = 'target="_blank"'

        if self.key and not self.text:
            self.text = Translate.get(key = self.key)

        if not self.text:
            self.text = self.href

        #default style: text-purple-500 hover:text-purple-300
        style = 'text-' + self.color + '-500 hover:text-' + self.color + '-300'

        if self.color == 'white':
            style = 'text-white'
        elif self.color == 'black':
            style = 'text-black'

        return A(
            self.text,
            href    = self.href,
            target  = target,
            cls     = style + '''
                hover:overline
            '''
        )
