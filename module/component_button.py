from fasthtml.common    import Button, Div
from lucide_fasthtml    import Lucide as Icon

from module.translate   import Translate



class Component_button:
    def __init__(
            self,
            key         : str   = None,
            text        : str   = None,
            icon        : str   = None,
            isSelected  : bool  = False,
            isDisabled  : bool  = False,
            isUpercase  : bool  = False

        ) -> None:

        self.key        = key
        self.text       = text
        self.icon       = icon
        self.isSelected = isSelected
        self.isDisabled = isDisabled
        self.isUpercase = isUpercase



    def do(self) -> Button:
        #attributes
        if self.key and not self.text:
            self.text = Translate.get(key = self.key)

        if self.isUpercase:
            self.text = self.text.upper()
        else:
            self.text = self.text.capitalize()

        styleSelected = ''

        style = 'bg-purple-600 hover:bg-green-700'

        if self.isDisabled:
            style = 'bg-gray-400 text-gray-200 cursor-not-allowed'

        if self.isSelected:
            styleSelected = 'outline-dashed outline-green-700 outline-2 outline-offset-4'

        #content
        icon = None

        if self.icon:
            icon = Icon(self.icon)

        content = Div(
            self.text,
            icon,
            cls = '''
                flex
                justify-center
                items-center
                gap-2
            '''
        )

        #button
        return Button(
            content,
            cls = style + ' ' + styleSelected + '''
                px-4
                py-2
                rounded-lg
                border-y-2
                font-extrabold
            '''
        )
