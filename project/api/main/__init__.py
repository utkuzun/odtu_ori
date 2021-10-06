from flask import Flask, jsonify, Blueprint
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import backref
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_jwt_extended import create_access_token, jwt_required, JWTManager, current_user
from flask_restful import Api, Resource
import datetime
import os
import sys


sys.path.append('../config')
from config import DevelopmentConfig

# ######################################
# Initiate the app and import app settings from config file

app = Flask(__name__)
app.config.from_object(DevelopmentConfig())
app.config['FLASK_ADMIN_SWATCH'] = 'cerulean'


bcrypt = Bcrypt(app)
db = SQLAlchemy(app)
Migrate(app, db)

# #######################################
# Add views to admin page
admin = Admin(app, name='odtü ori', template_mode='bootstrap3')

from main.models import User, Athlete, Competition, Stage, Category, Club, TokenBlocklist, Result

class MyModelView(ModelView):
    pass
    # @jwt_required()
    # def is_accessible(self):
    #     return current_user.is_admin
# class RaceView(ModelView):
#     form_columns = ["athlete_id", "stage_id", "rank", "time"]
#     # pass

# admin.add_view(RaceView(Race, db.session))

admin.add_view(MyModelView(Result, db.session))
admin.add_view(MyModelView(User, db.session))
admin.add_view(MyModelView(Competition, db.session))
admin.add_view(MyModelView(Stage, db.session))
admin.add_view(MyModelView(Category, db.session))
admin.add_view(MyModelView(Athlete, db.session))
admin.add_view(MyModelView(Club, db.session))
admin.add_view(MyModelView(TokenBlocklist, db.session))


# #####################################
# Manage JWT's

jwt = JWTManager(app)

# Register a callback function that takes whatever object is passed in as the
# identity when creating JWTs and converts it to a JSON serializable format.
@jwt.user_identity_loader
def user_identity_lookup(user):
    return user.id

# Register a callback function that loades a user from your database whenever
# a protected route is accessed. This should return any python object on a
# successful lookup, or None if the lookup failed for any reason (for example
# if the user has been deleted from the database).
@jwt.user_lookup_loader
def user_lookup_callback(_jwt_header, jwt_data):
    identity = jwt_data["sub"]
    return User.query.filter_by(id=identity).one_or_none()


# Callback function to check if a JWT exists in the database blocklist
@jwt.token_in_blocklist_loader
def check_if_token_revoked(jwt_header, jwt_payload):
    jti = jwt_payload["jti"]
    token = db.session.query(TokenBlocklist.id).filter_by(jti=jti).scalar()
    return token is not None



# ################################
# Add Resources
api_bp = Blueprint('api', __name__, url_prefix="/api")
api = Api(api_bp)

from main.resources.tests import Test
from main.resources.tables import ClubApi, ClubsAllApi, CompetitionApi, CompetitionsAllApi
from main.auth.auth import LoginApi, RegisterApi, LogoutApi, RefreshApi

auth_bp = Blueprint('auth', __name__, url_prefix="/auth")
auth = Api(auth_bp)

# Add api resources

api.add_resource(Test, "/test")
api.add_resource(ClubApi, "/club/<int:club_id>")
api.add_resource(ClubsAllApi, "/clubs")
api.add_resource(CompetitionApi, "/competition/<int:competition_id>")
api.add_resource(CompetitionsAllApi, "/competitions")

# Add auth resources

auth.add_resource(LoginApi, "/login")
auth.add_resource(RegisterApi, "/register")
auth.add_resource(LogoutApi, "/logout")
auth.add_resource(RefreshApi, "/refresh")

# register blueprints
app.register_blueprint(api_bp)
app.register_blueprint(auth_bp)