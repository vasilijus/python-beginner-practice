# Diffrent Environments

pip3 install pipenv

# We run pipenv and tell im we want a python3 project
pipenv --three
```
Creating a virtualenv for this project…
Pipfile: /home/sergio/code/Coding Practices/Python/CloudGuru/04 - Managing Pipenv/Pipfile
Using /usr/bin/python3 (3.7.3) to create virtualenv…
⠧ Creating virtual environment...Already using interpreter /usr/bin/python3
Using base prefix '/usr'
New python executable in /home/sergio/.virtualenvs/04_-_Managing_Pipenv-USv_glBy/bin/python3
Also creating executable in /home/sergio/.virtualenvs/04_-_Managing_Pipenv-USv_glBy/bin/python
Installing setuptools, pip, wheel...
done.

✔ Successfully created virtual environment! 
Virtualenv location: /home/sergio/.virtualenvs/04_-_Managing_Pipenv-USv_glBy
Creating a Pipfile for this project…
```

pipenv shell
 - (04 - Managing Pipenv)  sergio@sergio ~/04 - Managing Pipenv   master
python --version
 - 3.7.2

Ctrl+D -> Exit pipenv shell

pipenv run python -V
Python 3.7.2

pipenv run python find_meteors.py

Traceback (most recent call last):
  File "find_meteors.py", line 2, in <module>
    import requests
ModuleNotFoundError: No module named 'requests'

 - Math is part of the Python standard library
 - Requests is an external library

## To install dependency in environment ( pipenv )

`
pipenv install requests
`
 - This will add the ( requests ) to the Pipfile package list ! ( * - latest version )

 looks into folder 'meteors' and fires the find_meteors.py file
```
from meteors import find_meteors 
```

## If the code is meant to be run as a script , put it in - if __name__ == '__main__': block