from fasthtml.common    import *
from module.common      import Common



class Title:
    def get_view():
        version = Common.get_version()
        git     = Common.get_git_url()

        divTitle = Div(
            H1('Alchemixa', cls = 'font-extrabold text-orange-400 text-6xl italic gb-red-500 animate__animated animate__pulse animate__infinite animate__slower'),
            cls='mx-16 flex justify-end'
        )

        divMenu = Div(
            A('New game',   href = '#'),
            A('Continue',   href = '#'),
            A('Options',    href = '#'),
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
