# Environment Preparation
- Install [Anaconda](https://www.continuum.io/downloads)
- Import the environment.yml file and activate the environment
  - `conda env create -f environment.yml`
  - `source activate over-bot`
- If you get an error during the `conda env create` command, you need to install
  the latest `discord.py` from Github: `pip install
  git+https://github.com/Rapptz/discord.py.git`
  - For some reason pypi is still on version 0.9.2 of discord.py, and we need v0.10.0+
- Export the API key for the bot to an environment variable called OVERBOT_TOKEN
  - `export OVERBOT_TOKEN=<token>`
