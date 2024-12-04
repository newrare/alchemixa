from fasthtml.common            import *

from module.common              import Common
from module.component_button    import Component_button
from module.component_link      import Component_link
from module.component_title     import Component_title
from module.translate           import Translate



class Screen_title:

    @classmethod
    def view_content(cls, lang: str = 'en'):
        divTitle = Div(
            Component_title(text = 'Alchemixa', size = 'extra', isAnimated = True).do(),
            cls='mx-16 flex justify-end'
        )

        divMenu = Div(
            A(Translate.do(lang = lang, key = 'new_game'),  href = '#',         cls='bg-purple-500/70 px-2 w-48 hover:text-green-300 rounded-lg border-x-4 hover:border-green-300'),
            A(Translate.do(lang = lang, key = 'continue'),  href = '#',         cls='bg-purple-500/70 px-2 w-48 hover:text-green-300 rounded-lg border-x-4 hover:border-green-300'),
            A(Translate.do(lang = lang, key = 'options'),   href = 'options',   cls='bg-purple-500/70 px-2 w-48 hover:text-green-300 rounded-lg border-x-4 hover:border-green-300'),
            A(Translate.do(lang = lang, key = 'ranking'),   href = 'ranking',   cls='bg-purple-500/70 px-2 w-48 hover:text-green-300 rounded-lg border-x-4 hover:border-green-300'),
            A(Translate.do(lang = lang, key = 'credits'),   href = '#',         cls='bg-purple-500/70 px-2 w-48 hover:text-green-300 rounded-lg border-x-4 hover:border-green-300'),
            cls='grid grid-cols-1 justify-items-end font-extrabold text-orange-50 text-xl italic gap-2 mx-16'
        )

        linkVersion = Component_link(
            text    = Common.version(lang),
            href    = Common.git_url(),
            isBlank = True,
            isButton= True
        )

        divVersion = Div(
            linkVersion.do(),
            cls = 'mx-16 w-fit'
        )

        divCol = Div(
            divTitle,
            divMenu,
            divVersion,
            cls = 'flex flex-col w-full gap-8'
        )

        divOverlay = Div(
            divCol,
            cls = 'w-screen h-screen min-h-96 grid justify-items-end content-end pb-16'
        )

        return Div(
            divOverlay,
            cls = 'w-screen h-screen bg-no-repeat bg-center bg-cover bg-[url("/public/image/home.jpeg")] rain-container',
            id  = 'title'
        )



    @classmethod
    def view_option(cls, lang: str = 'en'):
        print(lang)
        selected_en = 'outline-dashed outline-green-700 outline-2 outline-offset-4'
        selected_fr = ''

        if lang == 'fr':
            selected_fr = 'outline-dashed outline-green-700 outline-2 outline-offset-4'
            selected_en = ''

        modal = Div(
            Div(
                H2("Options", cls='text-4xl font-bold'),
                A(Button("X", cls='px-4 bg-purple-600 rounded-full border-x-2 hover:bg-purple-700'), href='/'),
                cls='flex flex-row justify-between mx-4 pt-4'
            ),
            Hr(cls='h-1 rounded bg-purple-300 border-0 mx-4'),
            P(
                Translate.do(lang = lang, key = 'option_soon'),
                Br(),
                Br(),
                Translate.do(lang = lang, key = 'choose_lang'),
                cls='px-4 py-2 font-semibold'
            ),
            Div(
                Div(
                    Component_button(text = "English",  isSelected = selected_en).do(),
                    hx_post="/lang/en",
                ),
                Div(
                    Component_button(text = "Français",  isSelected = selected_fr).do(),
                    hx_post="/lang/fr",
                ),
                cls='flex flex-row justify-around mx-4 mb-2'
            ),
            Div(),
            cls='bg-purple-900/70 text-white flex flex-col gap-4 rounded-lg border-x-4 border-purple-300 w-full md:w-4/6 lg:w-1/2 xl:w-1/4 min-w-96'
        )

        overlay = Div(
            modal,
            cls='w-screen h-screen bg-purple-950/70 px-4 py-4 flex items-center justify-center'
        )

        return Div(
            overlay,
            id = 'title',
            cls='w-screen h-screen bg-no-repeat bg-center bg-cover bg-[url("/public/image/home.jpeg")]'
        )
