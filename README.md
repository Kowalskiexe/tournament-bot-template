# Tournament bot template / sample bot

This is a minimalistic sample bot for a tournament to demonstrate how such bot could be made.

This sample bot can also be used as a template to create your own bot in Python.

### Requirements
* [Python](https://www.python.org/) installed on your system
* [git](https://git-scm.com/) installed on your system
* rudimentary programming knowledge

### Step 1.
Clone this repo with commands
```bash
git clone https://github.com/kowalskiexe/tournament-bot-template
```

### Step 2.
Create [virtual enviroment](https://python.land/virtual-environments/virtualenv) in Python
```bash
python -m venv .tournament-bot-template
```
Source virtual enviroment

On linux / macOS:
```bash
source .tournament-bot-template/bin/activate
```
On Windows:
```bash
# In cmd.exe
.tournament-bot-template\Scripts\activate.bat
# In PowerShell
.tournament-bot-template\Scripts\Activate.ps1
```

Install needed dependencies

On linux / macOS:
```bash
cd tournament-bot-template
pip install -r requirements.txt
```

Now you can run the bot and test its functionality
Start the bot by:
```bash
# in the projects root directory
python -m bot
```
Test the bot by running:
On linux / macOS:
```bash
curl -X POST -H "Content-type: text/json" -d '{"opponents_last_move": "testify"}' localhost:5000
```
On Windows
```powershell
# in PowerShell, not cmd.exe
Invoke-WebRequest -Uri 'http://localhost:5000' -Method Post -Headers @{'Content-type'='text/json'} -Body '{"opponents_last_move": "testify"}'
```

### Step 3.
Implement your strategy in strategy.py file.

### Step 4.
When ready, build your [docker image](https://www.youtube.com/watch?v=Gjnup-PuquQ) by running a command `docker build -t YOUR-BOT-NAME .` in the project's root directory (the one with this README.md file in it).

Then your docker image can be used by the judge bot.
