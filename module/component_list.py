from fasthtml.common import Div, A



class Component_list:
    def __init__(
            self,
            elements    : list  = None,     #{'title': 'title_value', 'href': 'href_value'}
            text        : str   = 'left',   #enum('left', 'center', 'right')
            isUpercase  : bool  = False,
            isSecondary : bool  = False
        ) -> None:

        self.elements   = elements
        self.text       = text
        self.isUpercase = isUpercase
        self.isSecondary= isSecondary



    def do(self) -> Div:
        #attributes
        for element in self.elements:
            if self.isUpercase:
                element['title'] = element['title'].upper()
            else:
                element['title'] = element['title'].capitalize()

        #content
        style = 'px-2 w-48 rounded-lg border-x-4'

        if self.isSecondary:
            style += ' text-green-100 bg-green-500/70 hover:text-purple-200 hover:border-purple-200'
        else:
            style += ' text-purple-100 bg-purple-500/70 hover:text-green-300 hover:border-green-300'

        if self.text == 'left':
            style += ' text-left'
        elif self.text == 'center':
            style += ' text-center'
        else:
            style += ' text-right'

        links = []
        for element in self.elements:
            link = A(element['title'], href = element['href'], cls = style)
            links.append(link)

        #list
        return Div(
            *links,
            cls = 'grid gap-2 font-extrabold text-xl italic'
        )
