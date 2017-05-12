import os
from flask import Flask
from wcontrol.src.momentjs import momentjs

app = Flask(__name__)
app.config.from_object(os.environ.get("WCONTROL_CONF"))
app.jinja_env.globals['momentjs'] = momentjs
