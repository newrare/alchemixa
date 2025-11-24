from fasthtml.common            import *

from module.common              import Common
from module.component_button    import Component_button
from module.component_link      import Component_link
from module.component_list      import Component_list
from module.component_title     import Component_title
from module.translate           import Translate



class Screen_title:

    @classmethod
    def view_content(cls, lang: str = 'en'):
        #title
        title = Div(
            Component_title(text = 'Alchemixa', size = 'extra', isAnimated = True, isShadow = True).do(),
            cls='mx-16 flex justify-end'
        )

        #menu
        links = [
            {'title': Translate.do(lang = lang, key = 'new_game'),  'href'  : '#'               },
            {'title': Translate.do(lang = lang, key = 'continue'),  'href'  : '#'               },
            {'title': Translate.do(lang = lang, key = 'options'),   'click' : 'modal_option'    },
            {'title': Translate.do(lang = lang, key = 'ranking'),   'href'  : 'ranking'         },
            {'title': Translate.do(lang = lang, key = 'credits'),   'href'  : '#'               }
        ]

        menu = Div(
            Component_list(elements = links, text = 'right').do(),
            cls='mx-16 justify-items-end'
        )

        #version
        version = Component_link(
            text    = Common.version(lang),
            href    = Common.git_url(),
            isBlank = True,
            isButton= True
        )

        section_version = Div(
            version.do(),
            cls = 'mx-16 w-fit'
        )

        #content
        content = Div(
            title,
            menu,
            section_version,
            cls = 'h-full grid grid-cols-1 gap-8 py-8 content-end'
        )

        #option
        selected_en     = 'outline-dashed outline-green-700 outline-2 outline-offset-4'
        selected_fr     = ''
        click_fr        = 'change_lang("fr")'
        click_en        = 'modal_close_by_id("modal_option")'

        if lang == 'fr':
            selected_fr = 'outline-dashed outline-green-700 outline-2 outline-offset-4'
            selected_en = ''
            click_fr    = 'modal_close_by_id("modal_option")'
            click_en    = 'change_lang("en")'

        option = Div(
            Div(
                H2("Options", cls='text-4xl font-bold'),
                A(Button("X", cls='px-4 bg-purple-600 rounded-full border-x-2 hover:bg-purple-700'), onclick = 'modal_close_by_id("modal_option")'),
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
                    Component_button(text = "English", is_selected = selected_en).do(),
                    onclick = click_en,
                ),
                Div(
                    Component_button(text = "Français", is_selected = selected_fr).do(),
                    onclick = click_fr,
                ),
                cls='flex flex-row justify-around mx-4 mb-2'
            ),
            Div(),
            cls='bg-purple-900/70 text-white flex flex-col gap-4 rounded-lg border-x-4 border-purple-300 w-full md:w-4/6 lg:w-1/2 xl:w-1/4 min-w-96'
        )

        modal = Div(
            option,
            id      = 'modal_option',
            cls     = 'fixed inset-0 flex items-center justify-center bg-purple-950/70 z-50 hidden',
            onclick = 'modal_close_by_id("modal_option")'
        )

        #page
        return Div(
            modal,
            content,
            cls = 'w-screen h-screen min-h-[420px] bg-no-repeat bg-center bg-cover bg-[url("/public/image/home.jpeg")] rain-container',
            #grid justify-items-end content-end pb-16 min-h-96
        )
