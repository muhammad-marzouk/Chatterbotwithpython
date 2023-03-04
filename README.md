# Chatbot with python 3.9.11
# installation
### download and install python 3.9.11
# create virtual environment
#### python39 -m venv
# active virtual environment on cmd
#### .\venv\Scripts\activate
#  pro versions info
#### Flask==2.2.3
#### pytz==2022.7.1
#### chatterbot==1.0.0

# handling Error
#### on venv\Lib\site-packages\sqlalchemy\util\compat.py
    if win32 or jython:
        time_func = time.time
    else:
        time_func = time.time
# To run this code
#### python39 app.py