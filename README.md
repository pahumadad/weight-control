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

Now, you have to create the environment variables with the absolute path to the `api.py` and the config file.

```
export FLASK_APP=$(pwd)/wcontrol/src/api.py
export WCONTROL_CONF=wcontrol.conf.config
```

To create the database you have to run:

`$ python -m wcontrol.src.api -c`


Authentication
--------------

The app uses OAuth authentication with Google and Facebook.

You have to get your credentials and set them as environment variables with the names:

```
WEIGHT_CONTROL_OAUTH_GOOGLE_ID
WEIGHT_CONTROL_OAUTH_GOOGLE_SECRET
WEIGHT_CONTROL_OAUTH_FACEBOOK_ID
WEIGHT_CONTROL_OAUTH_FACEBOOK_SECRET
```

Running
-------

To run the app you have to activate the virtual environment and then execute:

`$ python -m flask run --host=0.0.0.0 --debugger`



Run the app with Docker
-----------------------

To run the app with docker, just execute the following commands.

```
$ docker build -t weigth-control .
$ sudo service docker start
$ docker run -p 5000:5000 weigth-control
```
