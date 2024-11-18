from fasthtml.common    import *
from module.common      import Common
from lucide_fasthtml    import Lucide as Icon



class Title:
    def get_view():
        version = Common.get_version()
        git     = Common.get_git_url()

        divTitle = Div(
            H1('Alchemixa', cls = 'font-extrabold text-orange-400 text-6xl italic gb-red-500 animate__animated animate__pulse animate__infinite animate__slower'),
            Icon('test-tube-diagonal', color='orange'),
            cls='mx-16 flex justify-end'
        )

        divMenu = Div(
            A('New game',   href = '#'),
            A('Continue',   href = '#'),
            A('Options',    href = '/options', cls='hover:text-blue-500'),
            A('Players',    href = '/players', cls='hover:text-blue-500'),
            A('Credits',    href = '#'),
            cls='grid grid-cols-1 justify-items-end font-extrabold text-orange-50 text-xl italic gap-1 mx-16'
        )

        aVersion = A(
            version,
            href    = git,
            target  = '_blank',
            cls     = 'text-blue-400 hover:text-blue-500'
        )

        divVersion = Div(
            Img(src='/public/image/favicon.ico', cls='w-16 h-16'),
            aVersion,
            cls = 'flex items-end mx-16'
        )

        divCol = Div(
            divTitle,
            divMenu,
            divVersion,
            cls = 'flex flex-col w-full gap-8'
        )

        divOverlay = Div(
            divCol,
            cls = 'w-screen h-screen bg-orange-700/60 grid justify-items-end content-end pb-16'
        )

        return Div(
            divOverlay,
            cls = 'w-screen h-screen bg-no-repeat bg-center bg-cover bg-[url("/public/image/home.jpeg")]'
        )



    def get_option():
        modal = Div(
            Div(
                H2("Options", cls='text-4xl font-bold'),
                A(Button("X", cls='px-4 bg-purple-600 rounded-full border-x-2 hover:bg-purple-700'), href='/'),
                cls='flex flex-row justify-between mx-4 pt-4'
            ),
            Hr(cls='h-1 rounded bg-purple-300 border-0 mx-4'),
            P(
                "Nous ajouterons plusieurs options ici au fur et à mesure du développement.",
                Br(),
                Br(),
                "Veuillez choisir votre langue de prédilection.",
                cls='px-4 py-2 font-semibold'
            ),
            Div(
                Button("English", cls='bg-purple-600 font-extrabold px-4 py-2 rounded-lg border-y-2 hover:bg-green-700'),
                Button("Français", cls='bg-purple-600 font-extrabold px-4 py-2 rounded-lg border-y-2 hover:bg-green-700'),
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
            cls='w-screen h-screen bg-no-repeat bg-center bg-cover bg-[url("/public/image/home.jpeg")]'
        )

