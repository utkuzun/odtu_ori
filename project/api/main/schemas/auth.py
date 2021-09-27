from marshmallow import Schema, fields, validate,validates, ValidationError, validates_schema, post_dump
from main.models import User, Athlete, Club, Category



# #########################
# marshmallow schemas

class ClubSchema(Schema):

    id = fields.Int(required= True, dump_only=True)
    short_name = fields.String(required= True)
    name = fields.String(required= True) #validata unique name and short_name
    city = fields.String(required= True)

    # Nested fields
    user = fields.Nested("UserSchema",only=("id","first_name", "last_name", "email"))
    athletes = fields.List(fields.Nested("AthleteSchema",exclude=("club",)))
    stages = fields.List(fields.Nested("StageSchema", only=("id", "short_name", "competition")))

class RaceSchema(Schema):

    id = fields.Int(required= True, dump_only=True)
    rank = fields.Int()
    time = fields.Time()

    athlete = fields.Nested("AthleteSchema",exclude=("competitions",))
    stage = fields.Nested("StageSchema",exclude=("competition",))




class AthleteSchema(Schema):

    id = fields.Int(required= True, dump_only=True)
    first_name = fields.String(required=True)
    last_name = fields.String(required=True)
    email = fields.Email(required=True)
    born = fields.Date(required=True)
    si = fields.Integer()
    category = fields.Nested("CategorySchema", exclude=("competitions","athletes"))
    sex = fields.String(required = True, validate= validate.OneOf(choices=["Erkek", "Kadın", "E", "M","K","W", "Man", "Woman"])) 

    # Nested fields
    club = fields.Nested("ClubSchema",only=("id","short_name", "name", "city"))
    stages = fields.List(fields.Nested("StageSchema", only=("id", "name","competition")))
    
    # validate if si number already in use
    @validates("si")
    def validate_si(self, value):
        if value != 0:
            athelete = Athlete.query.filter_by(si=value).first()
            if athelete:
                raise ValidationError("This si number already in use!!")

    # @pre_load
    # def load_category_objects(self, data, **kwargs):
    #     category = Category.query.filter_by(short_name = data["category"]).first()
    #     data[]


    # @post_dump
    # def format_category(self, data, **kwargs):
    #     data["category"] = data["category"]["short_name"]
    #     return data

    # validate if category exists
    @validates("category")
    def validate_category(self, value):
        category = Category.query.filter_by(short_name=value["short_name"]).first()
        if category is None:
            raise ValidationError("This category doesn't exists!!")

    # validate if club exists
    @validates("club")
    def validate_club(self, value):
        club = Club.query.filter_by(name=value["name"]).first()
        if club is None:
            raise ValidationError("This club doesn't exists!!")

    # validate if email number already in use
    @validates("email")
    def validate_email(self, value):
        athelete = User.query.filter_by(email=value).first()
        if athelete:
            raise ValidationError("This email already in use!!")


class CategorySchema(Schema):
    id = fields.Int(required= True, dump_only=True)
    short_name = fields.String(required= True)
    name = fields.String(required= True)

    # Nested fields
    competitions = fields.List(fields.Nested("CompetitionSchema", only=("id", "name", "date", "city")))
    athletes = fields.List(fields.Nested("AthleteSchema", only=("id", "first_name","last_name")))


class StageSchema(Schema):
    id = fields.Int(required= True, dump_only=True)
    short_name = fields.String(required= True)
    name = fields.String(required= True)
    length = fields.Float()
    controls = fields.Integer()

    # Nested fields
    competition = fields.Nested("CompetitionSchema", only=("id", "name", "date", "city"))
    athletes = fields.List(fields.Nested("AthleteSchema", only=("id", "first_name","last_name", "category")))


class CompetitionSchema(Schema):
    id = fields.Int(required= True, dump_only=True)
    name = fields.String(required= True) # validate unique name
    city = fields.String(required= True)
    adress = fields.String(required= True)
    si_available = fields.Boolean(reqired= True)
    is_active = fields.Boolean(reqired= True)
    date = fields.DateTime(reqired=True)
    register_due = fields.DateTime(reqired=True)

    # Nested fields
    categories = fields.List(fields.Nested("CategorySchema",exclude=("competitions","athletes")))
    clubs = fields.List(fields.Nested("ClubSchema",exclude=("competitions","athletes","user")))
    stages = fields.List(fields.Nested("StageSchema",exclude=("competition","athletes")))

class UserSchema(Schema):
    id = fields.Int(required= True, dump_only=True)
    first_name = fields.String(validate=validate.Length(min=1, max=40),required=True)
    last_name = fields.String(validate=validate.Length(min=1, max=40),required=True)
    email = fields.Email(required=True)
    password = fields.String(required=True, load_only=True) 
    password_rep = fields.String(required=True, load_only=True) 
    club = fields.Nested("ClubSchema", only=("id","short_name", "name", "city"))

    # validate if email number already in use
    @validates("email")
    def validate_email(self, value):
        athelete = User.query.filter_by(email=value).first()
        if athelete:
            raise ValidationError("This email already in use!!")



    @validates_schema()
    def validate_passwords(self, data, **kwargs):
        errors = {}
        if data["password"] != data["password_rep"]:
            errors["password_rep"] = ["Passwords don't match with each other!!"]

        if errors:
            raise ValidationError(errors)

