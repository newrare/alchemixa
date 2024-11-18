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

The project is configured to be deployed on Vercel. You can deploy the project by pushing the code to the Git repository. The deployment will be done automatically by Vercel.

https://alchemixa.vercel.app/



## Icon

We use fastHTML icon library for the project [lucide-fasthtml](https://github.com/curtis-allan/lucide-fasthtml). You can find the icons at the following link:
[Lucide Icons](https://lucide.dev/icons/)

Example of usage:

```python
from lucide_fasthtml import Lucide as Icon

Icon("sun", color="red", stroke_width="1.5", absolute_sw=True, size=16)
```

## License

This project is licensed under the MIT License.



## Report Issues

Please feel free to report any issues or bugs in the project. We will be happy to fix them.
