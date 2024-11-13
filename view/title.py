from fasthtml.common    import *
from module.common      import Common



class Title:
    def get_view():
        version = Common.get_version()

        divTitle = Div(
            H1('Alchemixa', cls='font-extrabold text-orange-400 text-6xl italic'),
            Img(src='/public/image/favicon.ico'),
            cls='mx-16 flex items-center justify-end animate__animated animate__pulse animate__infinite animate__slower'
        )

        divMenu = Div(
            A('New game',   href='#'),
            A('Continue',   href='#'),
            A('Options',    href='#'),
            A('Players',    href='/players', cls='hover:text-blue-500'),
            A('Credits',    href='#'),
            cls='flex flex-col font-extrabold text-orange-50 text-xl italic text-right mx-16'
        )

        aVersion = A(
            version,
            href='https://github.com/newrare/alchemixa',
            target='_blank',
            cls='text-blue-400 text-left mx-16 hover:text-blue-500'
        )

        divCol = Div(
            divTitle,
            divMenu,
            aVersion,
            cls='flex flex-col w-full gap-8'
        )

        divOverlay = Div(
            divCol,
            cls='w-screen h-screen bg-orange-700/60 grid justify-items-end content-end pb-16'
        )

        return Div(
            divOverlay,
            cls='w-screen h-screen bg-no-repeat bg-center bg-cover bg-[url("/public/image/home.jpeg")]'
        )
