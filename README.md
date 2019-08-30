# Image Upload

Image upload uploads images and provide image size and extensions restrictions on it.

## Prerequisites:

You will need the following programmes properly installed on your computer.

* [Python](https://www.python.org/) 3.6+
* [Virtual Environment](https://pypi.org/project/virtualenv/)

To install virtual environment on your system use:

```bash
pip install virtualenv

or

pip3 install virtualenv #if using linux(for python 3 and above)
```

## Installation:

```bash
git clonehttps://github.com/ongraphpythondev/image_upload

cd image_upload

virtualenv venv
      or
virtualenv venv -p python3 #if using linux(for python 3 and above)

venv\Scripts\activate # for windows
      or
source venv/bin/activate # for linux

# install required packages for the project to run
pip install -r requirements.txt

# run migrations for database
python manage.py migrate
```


## Running:

To run the development server after installation:
```bash
# activate the virtual environment
venv\Scripts\activate # for windows
      or
source venv/bin/activate # for linux

# run server
python manage.py runserver
```
