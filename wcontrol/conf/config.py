import os

# TODO: improve DB path selection
basedir = os.path.abspath(os.path.dirname(__file__))

# sqlalchemy database config
SQLALCHEMY_DATABASE_URI = os.environ.get('WCONTROL_DB',
                                         'sqlite:///' + basedir + '/../db/app.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
SQLALCHEMY_TRACK_MODIFICATIONS = False

# forms wtf config
WTF_CSRF_ENABLED = True
SECRET_KEY = 'impossible-to-guess'

# oauth google config
OAUTH_CREDENTIALS = {
        'google': {
            'id': os.environ.get('WEIGHT_CONTROL_OAUTH_GOOGLE_ID'),
            'secret': os.environ.get('WEIGHT_CONTROL_OAUTH_GOOGLE_SECRET')
        },
        'facebook': {
            'id': os.environ.get('WEIGHT_CONTROL_OAUTH_FACEBOOK_ID'),
            'secret': os.environ.get('WEIGHT_CONTROL_OAUTH_FACEBOOK_SECRET')
        }
}

# measurements
MEASUREMENTS = [
        (0, 'weight', 'Weight'),
        (1, 'bmi', 'BMI'),
        (2, 'fat', 'Fat'),
        (3, 'muscle', 'Muscle'),
        (4, 'viceral', 'Viceral Fat'),
        (5, 'bmr', 'Basal Metabolic Rate'),
        (6, 'bodyage', 'Body Age')]
