from flask import request

from flask_restful import Resource
from flask_jwt_extended import create_access_token,create_refresh_token ,jwt_required, JWTManager, current_user, get_jwt

import datetime

from main.models import User, Athlete, Club, Category, TokenBlocklist
from main import db
from marshmallow import ValidationError
from main.schemas.auth import UserSchema, ClubSchema, AthleteSchema

# create schemas

user_schema = UserSchema()
athlete_schema = AthleteSchema()
club_schema = ClubSchema()

# #############################
# æpi resources

class RegisterApi(Resource):
    def post(self):
        
        # Load request data
        try :
            user_data = user_schema.load(request.json["user"], unknown="EXCLUDE")
            athlete_data = athlete_schema.load(request.json["athlete"], unknown="EXCLUDE")
            club = Club.query.filter_by(name=athlete_data["club"]["name"]).first()
            category = Category.query.filter_by(short_name=athlete_data["category"]["short_name"]).first()
            user = User.query.filter_by(email=user_data["email"]).first()
            athlete = Athlete.query.filter_by(email= athlete_data["email"]).first()
        except ValidationError as error:
            return {"status":"fail", "message":error.messages}

        # check if user or athlete already exists
        if user is None and athlete is None:
            try:
                # Create user and athlete objects
                user = User(
                    user_data["first_name"], 
                    user_data["last_name"], 
                    user_data["email"], 
                    user_data["password"]
                )

                athlete = Athlete(
                    first_name=athlete_data["first_name"], 
                    last_name=athlete_data["last_name"], 
                    email=athlete_data["email"], 
                    si=None if athlete_data["si"] == 0 else athlete_data["si"], 
                    category_id = category.id,
                    born = athlete_data["born"], 
                    club_id = club.id,
                    sex = athlete_data["sex"]
                )

                # add relations and commit to the database
                club.athletes.append(athlete)

                db.session.add(user)
                db.session.add(athlete)
                db.session.commit()

                # return with success status and craeted athlete
                athlete_out = athlete_schema.dump(athlete)                
                return {"status":"success", "message":"User added to the database !!", "athlete":athlete_out }

            except Exception as e:
                print(e)
                return {"status": "fail", "message": str(e)}

        else:
            return {"status": "fail", "message" : "This email is already taken!!"}

        

class LoginApi(Resource):
    def post(self):
        email = request.json.get("email")
        password =request.json.get("password")

        try:
            user = User.query.filter_by(email=email).one_or_none()

            if user:

                if user.check_user_pass(password):
                    user.last_login = datetime.datetime.now()
                    db.session.commit()
                    access_token = create_access_token(identity= user)
                    refresh_token = create_refresh_token(identity= user)

                    return {"status":"success","access_token":access_token, "refresh_token":refresh_token}, 200

                else:
                    return {"status":"fail", "message":"Password is incorrect!!"}, 404

            else:
                return {"status":"fail", "message":"Invalid email entered !!"}, 404

        except Exception as e:
            print(e)
            return {"status":"fail", "message":str(e)}


class LogoutApi(Resource):

    @jwt_required()
    def delete(self):
        # print(current_user)

        # jwt = get_jwt()
        # print(jwt)
        # print(get_jwt()["sub"])
        try:
            jti = get_jwt()["jti"]
            now = datetime.datetime.now()
            db.session.add(TokenBlocklist(jti=jti, created_at=now))
            db.session.commit()
            return {"message" : "JWT revoked!!"}

        except Exception as e:
            return {"status" : "success", "status":"fail", "message":str(e)}



class RefreshApi(Resource):
    @jwt_required(refresh=True)
    def post(self):
        try:
            new_access_token = create_access_token(identity= current_user)
            return {"status" : "success", "access_token": new_access_token}

        except Exception as e:
            return {"status":"fail", "message":str(e)}


