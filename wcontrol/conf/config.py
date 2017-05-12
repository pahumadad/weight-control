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
MEASUREMENTS = [(0, 'weight', 'Weight'),
                (1, 'bmi', 'BMI'),
                (2, 'fat', 'Fat'),
                (3, 'muscle', 'Muscle'),
                (4, 'viceral', 'Viceral Fat'),
                (5, 'bmr', 'Basal Metabolic Rate'),
                (6, 'bodyage', 'Body Age')]

# bmi categories: |max|description|
BMI = [(15, 'Very severely underweight'),
       (16, 'Severely underweight'),
       (18.5, 'Underweight'),
       (25, 'Normal (healthy weight)'),
       (30, 'Overweight'),
       (35, 'Obese Class I (Moderately obese)'),
       (40, 'Obese Class II (Severely obese)'),
       (1000, 'Obese Class III (Very severely obese)')]

# fat categories: |women (min)|men (min)|description|
FAT = [(10, 2, 'Essential fat'),
       (14, 6, 'Athletes'),
       (21, 13, 'Fitness'),
       (25, 17, 'Average'),
       (31, 22, 'Overweight'),
       (40, 30, 'Obese')]
