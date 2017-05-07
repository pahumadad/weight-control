Weight Control App
==================

This app ...


Instalation
-----------

The app uses Python, Flask and Bootstrap.
In order to install, you have to clone this repository and create a virtual environment. So, inside the folder with the repo, you have to create it with:

`$ python3 -m venv env`

Then, you have to install flask and extensions:

`$ env/bin/pip install -r requeriments.txt`

To create the database you have to run:

`$ ./db_create.py`


Authentication
--------------

The app uses OAuth authentication with Google and Facebook.

You have to get your credentials and set them as environment varialbes with the names:

```
WEIGHT_CONTROL_OAUTH_GOOGLE_ID
WEIGHT_CONTROL_OAUTH_GOOGLE_SECRET
WEIGHT_CONTROL_OAUTH_FACEBOOK_ID
WEIGHT_CONTROL_OAUTH_FACEBOOK_SECRET
```

Running
-------

To run the app just execute run.py

`$ ./run.py`
