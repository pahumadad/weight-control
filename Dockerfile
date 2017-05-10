FROM python:3.6

# RUN mkdir weight-control
COPY requirements.txt weight-control/requirements.txt
COPY wcontrol weight-control/wcontrol
WORKDIR weight-control
ENV WCONTROL_CONF=wcontrol.conf.config
RUN pip install -r requirements.txt
RUN  python -m wcontrol.src.main -c
ENV WEIGHT_CONTROL_OAUTH_GOOGLE_ID=1037220217614-drg97r936ktvfl4vht7e5mql9sodrcft.apps.googleusercontent.com
ENV WEIGHT_CONTROL_OAUTH_FACEBOOK_SECRET=eb5fdcf8af6d465a64931c83addb19f3
ENV WEIGHT_CONTROL_OAUTH_GOOGLE_SECRET=ZcrWM0IniQEJ8DISt-CWTUIN
ENV WEIGHT_CONTROL_OAUTH_FACEBOOK_ID=686678611517103
ENV FLASK_APP=/weight-control/wcontrol/src/main.py
CMD python -m flask run --host=0.0.0.0
# CMD bash
