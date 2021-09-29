from main import db, bcrypt, app
import datetime
import os

class User(db.Model):

    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(40), nullable=False)
    last_name = db.Column(db.String(40), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)
    registered_on = db.Column(db.DateTime, nullable=False)
    last_login = db.Column(db.DateTime)
    is_admin = db.Column(db.Boolean, nullable=False, default=False)
    is_director = db.Column(db.Boolean, nullable=False, default=False)
    club = db.relationship("Club",backref="user", lazy=True, uselist=False)


    def __init__(self, first_name, last_name, email, password_try, admin=False, is_director=False):

        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = bcrypt.generate_password_hash(password_try)
        self.registered_on = datetime.datetime.now()
        self.is_admin = admin
        self.is_director = is_director

    def check_user_pass(self, attemp):
        return bcrypt.check_password_hash(self.password, attemp)

    def __repr__(self):
        return f"< User : {self.email}, {self.last_name.upper()} {self.first_name}>"


class Club(db.Model):

    __tablename__="clubs"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    short_name = db.Column(db.String(10), nullable=False, unique=True)
    name = db.Column(db.String(100), nullable=False, unique=True)
    city = db.Column(db.String(60), nullable=False)
    athletes = db.relationship("Athlete", backref="club", lazy=True)


    def __repr__(self):
        return f"<{self.name}, {self.short_name} -- {self.city}>"




category_comp = db.Table("category_comp", 
    db.Column("category_id", db.Integer, db.ForeignKey("categories.id")),
    db.Column("competition_id", db.Integer, db.ForeignKey("competitions.id"))
)

club_comp = db.Table("club_comp", 
    db.Column("club_id", db.Integer, db.ForeignKey("clubs.id")),
    db.Column("competition_id", db.Integer, db.ForeignKey("competitions.id"))
)
# stage_athlete = db.Table("stage_athlete", 
#     db.Column("stage_id", db.Integer, db.ForeignKey("stages.id")),
#     db.Column("athlete_id", db.Integer, db.ForeignKey("athletes.id")),
#     db.Column("result_id", db.Integer, db.ForeignKey("results.id")),
# )

class Result(db.Model):
    __tablename__ = "results"
    athlete_id = db.Column( db.Integer, db.ForeignKey("athletes.id"), primary_key=True)
    stage_id = db.Column( db.Integer, db.ForeignKey("stages.id"), primary_key=True)
    rank = db.Column(db.Integer)
    time = db.Column(db.Time)

    athlete = db.relationship("Athlete",back_populates="result", lazy=True, uselist=False)
    stage = db.relationship("Stage",back_populates="result", lazy=True, uselist=False)

    def __repr__(self):
        return f"<{self.athlete.last_name}--{self.time}, {self.stage.name} ({self.stage.competition.name})>"


class Athlete(db.Model):

    __tablename__="athletes"

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(60), nullable=False)
    last_name = db.Column(db.String(60), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    si = db.Column(db.String(15), unique=True)
    sex = db.Column(db.String(10), nullable=False)
    born = db.Column(db.Date, nullable=False)  
    club_id = db.Column(db.Integer, db.ForeignKey("clubs.id"), nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey("categories.id"), nullable=False)

    result = db.relationship("Result",back_populates="athlete", lazy=True,viewonly=True)
    stages = db.relationship("Stage",secondary="results",lazy="subquery", back_populates="athletes")

    def __repr__(self):
        return f"<{self.first_name.upper()} {self.last_name} -- {self.club.short_name}>"


class Category(db.Model):

    __tablename__="categories"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60), nullable=False, unique=True)
    short_name = db.Column(db.String(10), nullable=False, unique=True)
    athletes = db.relationship("Athlete", backref="category", lazy=True)


    def __repr__(self):
        return f"<{self.name.upper()}>"

class Stage(db.Model):

    __tablename__="stages"

    id = db.Column(db.Integer, primary_key=True)
    competition_id = db.Column(db.Integer, db.ForeignKey("competitions.id"))
    name = db.Column(db.String(15), nullable=False)
    short_name = db.Column(db.String(15), nullable=False)
    length = db.Column(db.Float, nullable=False)
    controls = db.Column(db.Integer, nullable=False)

    result = db.relationship("Result",back_populates="stage", lazy=True,viewonly=True)
    athletes = db.relationship("Athlete",secondary="results",lazy="subquery", back_populates="stages")


    def __repr__(self):
        return f"<{self.name.upper()}--{self.controls}hedef, {self.length}km> ({self.competition.name})"

class Competition(db.Model):

    __tablename__ = "competitions"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(300), nullable=False, unique=True)
    city = db.Column(db.String(60), nullable=False)
    adress = db.Column(db.String(300), nullable=False)
    is_active = db.Column(db.Boolean, nullable=False)
    si_available = db.Column(db.Boolean, nullable=False)
    date = db.Column(db.DateTime, nullable=False)
    register_due = db.Column(db.DateTime, nullable=False)

    
    stages = db.relationship("Stage", lazy="subquery", backref=db.backref("competition", lazy=True))
    categories = db.relationship("Category", secondary=category_comp, lazy="subquery", backref=db.backref("competitions", lazy=True))
    clubs = db.relationship("Club", secondary=club_comp, lazy="subquery", backref=db.backref("competitions", lazy=True))

    def __repr__(self):
        return f"<{self.name}, {self.date} -- {self.city}>"


class TokenBlocklist(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    jti = db.Column(db.String(36), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False)



# Race = db.Table("athelete_stage", 
#     db.Column("athlete_id", db.Integer, db.ForeignKey("athletes.id")),
#     db.Column("stage_id", db.Integer, db.ForeignKey("stages.id")), 
#     db.Column("rank",db.Integer),
#     db.Column("time",db.Time)
# )
# athelete_stage = db.Table("athelete_stage", 
#     db.Column("athlete_id", db.Integer, db.ForeignKey("athletes.id")),
#     db.Column("stage_id", db.Integer, db.ForeignKey("stages.id")),

# )

# stage_comp = db.Table("stage_comp", 
#     db.Column("stage_id", db.Integer, db.ForeignKey("stages.id")),
#     db.Column("competition_id", db.Integer, db.ForeignKey("competitions.id"))
# )