from flask import request
from flask_restful import Resource
from flask_jwt_extended import jwt_required

from main.models import User, Athlete, Club, Category, TokenBlocklist, Competition
from main.schemas.auth import UserSchema, ClubSchema, AthleteSchema, CompetitionSchema

try:
    club_schema = ClubSchema()
    clubs_schema = ClubSchema(many=True, exclude=("athletes", "user"))


    competition_schema = CompetitionSchema()
    competitions_schema = CompetitionSchema(many=True,only=("adress","id", "name", "date", "city","si_available","is_active", "register_due"))

    athlete_schema = AthleteSchema()
except Exception as error:
    print(error)

    
class ClubApi(Resource):
    ### returns one club with spesified club_id 
    # @jwt_required()
    def get(self, club_id):

        try:
            # query club with club id return club with success status
            club = Club.query.filter_by(id = club_id).first()

            if club:
                club_out = club_schema.dump(club)
                return {"status" : "success", "club" : club_out}

            else : 
                # if club doesn't exists return error
                return {"status": "fail", "message" : "Club doesn't exists!!!"}

        except Exception as error:
            # if there is an error print and response with fail
            print(error)
            return {"status": "fail", "message" : error}


class ClubsAllApi(Resource):
    # @jwt_required()
    def get(self):

        # return all clubs in the database

        try:
            clubs = Club.query.all()

            if clubs:
                clubs_out = clubs_schema.dump(clubs)
                return {"status" : "success", "clubs" : clubs_out}

            else : 
                return {"status": "fail", "message" : "No club exists yet!!!"}

        except Exception as error:
            # if there is an error print and response with fail
            print(error)
            return {"status": "fail", "message" : error}




class CompetitionApi(Resource):
    ### returns one Competitions with spesified Competitions_id 
    # @jwt_required()
    def get(self, competition_id):

        try:
            # query Competitions with Competitions id return Competitions with success status
            competition = Competition.query.filter_by(id = competition_id).first()

            if competition:
                competition_out = competition_schema.dump(competition)
                return {"status" : "success", "competition" : competition_out}

            else : 
                # if Competitions doesn't exists return error
                return {"status": "fail", "message" : "Competitions doesn't exists!!!"}

        except Exception as error:
            # if there is an error print and response with fail
            print(error)
            return {"status": "fail", "message" : error}


class CompetitionsAllApi(Resource):
    # @jwt_required()
    def get(self):

        # return all Competitionss in the database

        try:
            competitions = Competition.query.all()
            print(Competition)

            if competitions:
                competitions_out = competitions_schema.dump(competitions)
                return {"status" : "success", "competitions" : competitions_out}

            else : 
                return {"status": "fail", "message" : "No competition exists yet!!!"}

        except Exception as error:
            # if there is an error print and response with fail
            print(error)
            return {"status": "fail", "message" : error}


class AthleteApi(Resource):
    ### returns athlete api
    # @jwt_required()
    def get(self, athlete_id):

        try:
            athlete = Athlete.query.filter_by(id=athlete_id).first()

            if athlete:
                athlete_out = athlete_schema.dump(athlete)
                return {"status":"succes", "athletes":athlete_out}
            else: 
                return {"status": "fail", "message" : "No athlete exists with this id!!!"}

        except Exception as e:
            print(e)
            return {"status": "fail", "message": e}


