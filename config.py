import os
SECRET_KEY = os.urandom(32)
# Grabs the folder where the script runs.
basedir = os.path.abspath(os.path.dirname(__file__))

# Enable debug mode.
DEBUG = True

#----------------------------------------------------------------------------#
# App Config.
#----------------------------------------------------------------------------#

# app = Flask(__name__)
# moment = Moment(app)
# app.config.from_object('config')
# db.init_app(app)
# db = SQLAlchemy(app)
# TODO: connect to a local postgresql database
# migrate = Migrate(app, db)
# db.create_all()
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://richardph911@localhost:5432/Fyyurdb'
# Connect to the database
SQLALCHEMY_DATABASE_URI = 'postgresql://richardph911@localhost:5432/Fyyurdb'
SQLALCHEMY_TRACK_MODIFICATIONS = False