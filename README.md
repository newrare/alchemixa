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
git clone
python -m .venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```



## Running the project

To run the project, you need to set the environment variables in .env file.

```bash
ENV=prod
PYTHONPATH=.venv/lib/python3.12/site-packages
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



## License

This project is licensed under the MIT License.



## Report Issues

Please feel free to report any issues or bugs in the project. We will be happy to fix them.
