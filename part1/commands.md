# Commands

## Create venv

1. `python -m venv venv` # Create a virtual environment
2. `venv\Scripts\activate` # Activate the virtual environment
3. `pip install pip-tools` # Install pip-tools
4. Spara `requirements.in` med texten `selenium`
5. `pip-compile` # Compile the requirements file
6. `pip install -r requirements.txt` # Install the requirements

## Create git repo

1. Create repo on GitHub
2. `git init` # Initialize local repository
3. Create `.gitignore` and add files/folders to ignore
4. `git add .` # Stage all files for commit
5. `git commit -m "MESSAGE..."` # Create commit
6. `git remote add origin <URL>` # Connect local repo to remote repo (replace <URL>)
7. `git push` # Push code online... (gives error message)
8. `git push --set-upstream origin main` # Push code to online repo
9. Check github if it worked

## Push new changes

1. `git add .` # Track new changes
2. `git commit -m "MESSAGE..."` # Create commit
3. `git push` # Push new changes online
4. `git pull` # Get changes from online repo (remote)
5. `git push` # Push changes to online repo (remote)
6. Check github.com that it worked

## Övning till lunch

- Uppdatera lokala filer och skicka upp till remote
- Uppdatera filer på github.com och ladda ner lokalt med git
