# Chatbot with python 
#### version: 3.9.11

#  lib versions info
#### Flask==2.2.3
#### pytz==2022.7.1
#### chatterbot==1.0.0

# installation
### download and install python 3.9.11
#### https://www.python.org/downloads/release/python-3911/

# add in Evvironment Variables
### User variable for account_name path-->Edite
#### new --> C:\Users\account_name\AppData\Local\Programs\Python\Python39
#### new --> C:\Users\account_name\AppData\Local\Programs\Python\Python39\Scripts

# rename python exe to python39
### C:\Users\account_name\AppData\Local\Programs\Python\Python39
#### chang from python.exe --> to python39.exe

# create virtual environment
#### python39 -m venv venv

# active virtual environment on cmd
#### .\venv\Scripts\activate
# pip information
### pip list
    pip                22.0.4
    setuptools         58.1.0
#### notes wheel not found
# install wheel
#### pip install wheel


# dwonload libraries
### pip install Flask==2.2.3
#### pip freeze
    click==8.1.3
    colorama==0.4.6
    Flask==2.2.3
    importlib-metadata==6.0.0
    itsdangerous==2.1.2
    Jinja2==3.1.2
    MarkupSafe==2.1.2
    Werkzeug==2.2.3
    zipp==3.15.0


### pip install pytz==2022.7.1
#### pip freeze
    the last freeze + pytz==2022.7.1

spacy-2.1.9

# pip install chatterbot==1.0.0

# handling Error
#### on venv\Lib\site-packages\sqlalchemy\util\compat.py
    if win32 or jython:
        time_func = time.time
    else:
        time_func = time.time
# copy arabic file
#### copy arabic file to --> Chatterbotwithpython\venv\Lib\site-packages\chatterbot_corpus\data

# To run this code
#### python39 app.py
# postman GET method
#### http://127.0.0.1:5000/get?msg=الخدمات