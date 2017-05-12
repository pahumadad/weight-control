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
                (1, 'bmi', 'Body Mass Index (BMI)'),
                (2, 'fat', 'Body Fat Percentage (BFP)'),
                (3, 'muscle', 'Skeletal Muscle'),
                (4, 'visceral', 'Visceral Fat'),
                (5, 'rmr', 'Resting Metabolic Rate (RMR)'),
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

# bfp categories: |women|men|description|
BFP = [(13, 5, 'Essential fat'),
       (20, 12, 'Athletes'),
       (24, 16, 'Fitness'),
       (30, 21, 'Average'),
       (39, 29, 'Overweight'),
       (100, 100, 'Obese')]

# muscle categories: |women|men|description|
MUSCLE = [(24, 33, 'Low'),
          (30, 39, 'Normal'),
          (35, 44, 'High'),
          (100, 100, 'Very High')]
