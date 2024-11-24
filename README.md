# Alchemixa

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

This project is built using FastHTML, TailwindCSS and Supabase (BDD). The project is configured to be deployed on Vercel with auto-deployment from Git.

Alchemixa is a Web Game Alchemist deck building.



## Prerequisites

- Python 3.12
- Pip
- tailwindcss (ex: linux cli)



## Alias (bashrc)

```bash
alias pyRun='python main.py'
alias pyCss='tailwindcss -i ./tailwind.app.css -o ./public/css/style.min.css --minify'
```



## Installation

Clone the repository, setup the virtual environment, activate it and install the dependencies.

```bash
git clone git@github.com:newrare/alchemixa.git
cd alchemixa
cp .env .env.local
python -m .venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```
Dont forget to install tailwindcss and configure supabase in your .env.local file.



## Running the project on local (dev)

To run the project, you need to set the environment variables in .env.local file.

```bash
ENV=dev
URL=http://localhost:5001/
SUPABASE_URL=your_supabase_url
SUPABASE_KEY=your_supabase_key
```

Then run the project using the following command:

```bash
python main.py
pyRun
```

The project will be running (with hot auto reload) on http://localhost:5001



## Deployment

Before deploying the project, you need to build the CSS file using the following command:

```bash
pyCss
```

The project is configured to be deployed on Vercel. You can deploy the project by pushing the code to the Git repository. The deployment will be done automatically by [Vercel](https://alchemixa.vercel.app/).

Don't forget to set secret the environment variables in the Vercel Web settings.
Don't forget to add libraries to requirements.txt file before deploying (push on Git).



## Translation

The project is translated into several languages. You can add a new language by creating a new file in the `translation` folder. The file should be named as `<lang_iso_code>.json` (ex: `fr.json` for French). The file should contain the translations in the following format:

```json
{
    "key": "Singular translation",
    "keys": "Same to key but plural",
    "string": "A variable {value} can be set to the string",
    "key_not_found": "When the key does not exist in the current translation file, we use the key from the default language [en.json]"
}
```

You can use the translation in the project using the following code:

```python
from module.translate import Translate

msg = Translate.do(key = 'key')                    #get singular key value with default language
msg = Translate.do(key = 'keys')                   #get plurial keys value with default language
msg = Translate.do(key = 'key', number = 2)        #get plurial keys value with default language
msg = Translate.do(key = 'string', value= 'foo')   #get string value and put variable to the string with default language
msg = Translate.do(key = 'key', lang = 'fr')       #get singular key value for french language
```



## Icon and Font

We use fastHTML icon library for the project [lucide-fasthtml](https://github.com/curtis-allan/lucide-fasthtml). You can find the icons at the following link:
[Lucide Icons](https://lucide.dev/icons/)

Example of usage:

```python
from lucide_fasthtml import Lucide as Icon

Icon("sun", color="red", stroke_width="1.5", absolute_sw=True, size=16)
```
Be careful, when you use an icon, a file is automatically created: icons.py

We can use the custom CSS class `.font-title` for H1 to H6 elements.



## License

This project is licensed under the MIT License.



## Report Issues

Please feel free to report any issues or bugs in the project. We will be happy to fix them.
