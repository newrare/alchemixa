from fasthtml.common    import Div, H1, H2, H3, H4, H5, H6

from module.translate   import Translate



class Component_title:
    def __init__(
            self,
            key         : str       = None,
            text        : str       = None,
            size        : str       = 'medium', #enum('tiny', 'small', 'medium', 'large', 'extra')
            isAnimated  : bool      = False,
            isUpercase  : bool      = False,
            isSecondary : bool      = False,
        ) -> None:

        self.key        = key
        self.text       = text
        self.size       = size
        self.isAnimated = isAnimated
        self.isUpercase = isUpercase
        self.isSecondary= isSecondary



    def do(self) -> Div:
        #attributes
        if self.key and not self.text:
            self.text = Translate.get(key = self.key)

        if self.isUpercase:
            self.text = self.text.upper()
        else:
            self.text = self.text.capitalize()

        #content
        title = None
        style = 'font-extrabold font-title'

        if self.isSecondary:
            style += ' text-green-500'
        else:
            style += ' text-purple-400'

        if self.isAnimated:
            style += ' animate__animated animate__pulse animate__infinite animate__slower'

        if self.size == 'extra':
            title = H1(self.text, cls = style + ' text-6xl')
        elif self.size == 'large':
            title = H2(self.text, cls = style + ' text-4xl')
        elif self.size == 'medium':
            title = H3(self.text, cls = style + ' text-2xl')
        elif self.size == 'small':
            title = H4(self.text, cls = style + ' text-xl')
        elif self.size == 'tiny':
            title = H5(self.text, cls = style + ' text-lg')
        else:
            title = H6(self.text, cls = style)

        #button
        return Div(
            title,
            cls='flex justify-center'
        )
