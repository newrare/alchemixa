from fasthtml.common    import A, Button

from module.translate   import Translate



class Component_link:
    def __init__(
            self,
            href        : str   = '#',
            key         : str   = None,
            text        : str   = None,
            isBlank     : bool  = False,
            isButton    : bool  = False
        ) -> None:

        self.href       = href
        self.key        = key
        self.text       = text
        self.isBlank    = isBlank
        self.isButton   = isButton



    def do(self) -> A:
        #attributes
        target = ''

        if self.isBlank:
            target = 'target="_blank"'

        if self.key and not self.text:
            self.text = Translate.get(key = self.key)

        if not self.text:
            self.text = self.href

        #button
        if self.isButton:
            button = Button(
                self.text,
                cls = '''
                    px-2
                    rounded-lg
                    border-x-4
                    bg-purple-500/70
                    text-purple-200
                    border-purple-400
                    hover:text-green-300
                    hover:border-green-300
                '''
            )

            return A(
                button,
                href    = self.href,
                target  = target
            )

        #link
        return A(
            self.text,
            href    = self.href,
            target  = target,
            cls     = '''
                text-purple-300
                hover:text-purple-600
                hover:overline
            '''
        )
