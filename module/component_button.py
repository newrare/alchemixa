from fasthtml.common    import Button, Div
from lucide_fasthtml    import Lucide as Icon

from module.translate   import Translate



class Component_button:
    def __init__(
            self,
            key         : str   = None,
            text        : str   = None,
            icon        : str   = None,
            target      : str   = None,
            is_selected : bool  = False,
            is_disabled : bool  = False,
            is_upercase : bool  = False

        ) -> None:

        self.key        = key
        self.text       = text
        self.icon       = icon
        self.target     = target
        self.is_selected = is_selected
        self.is_disabled = is_disabled
        self.is_upercase = is_upercase



    def do(self) -> Button:
        #attributes
        if self.key and not self.text:
            self.text = Translate.get(key = self.key)

        if self.is_upercase:
            self.text = self.text.upper()
        else:
            self.text = self.text.capitalize()

        style_selected = ''

        style = 'bg-purple-600 hover:bg-green-700'

        if self.is_disabled:
            style = 'bg-gray-400 text-gray-200 cursor-not-allowed'

        if self.is_selected:
            style_selected = 'outline-dashed outline-green-700 outline-2 outline-offset-4'

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
                text-white
                gap-2
            '''
        )

        #button
        return Button(
            content,
            cls = style + ' ' + style_selected + '''
                px-4
                py-2
                rounded-lg
                border-y-2
                font-extrabold
            '''
        )
