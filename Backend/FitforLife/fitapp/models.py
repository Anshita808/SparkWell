from mongoengine import Document, StringField, IntField , ReferenceField, CASCADE,DateField
from django.contrib.auth.hashers import make_password
from django.contrib.auth.hashers import check_password

class User(Document):
    username = StringField(required=True)
    email = StringField(required=True, unique=True)
    password = StringField(required=True)
    gender = StringField()
    age = IntField()
    location = StringField()
    profile_image = StringField()
    
    def set_password(self, raw_password):
        self.password = make_password(raw_password)
    
    def check_password(self, raw_password):
        return check_password(raw_password, self.password)

class Trainer(Document):
    name = StringField(required=True)
    email = StringField(required=True , unique=True)
    password = StringField(required=True)
    gender = StringField()
    age = IntField()
    location=StringField()
    specialization = StringField()
    profile_image = StringField()
    experience = IntField()
    contact_number = StringField()

    def set_password(self, raw_password):
        self.password = make_password(raw_password)
    
    def check_password(self, raw_password):
        return check_password(raw_password, self.password)
    
class WorkoutPlan(Document):
    name = StringField(required=True)
    goal = StringField(required=True)
    duration = StringField(required=True)
    description = StringField()
    trainer = ReferenceField(Trainer, reverse_delete_rule=CASCADE)
    exercises = StringField()
    trainer_name = StringField()

class UserWorkoutLog(Document):
    user = ReferenceField(User, required=True , reverse_delete_rule=CASCADE)
    date = StringField(required=True)
    workout_plan = StringField(required=True) 
    exercises = StringField()
    duration = IntField()
    user_name = StringField()

class Goal(Document):
    user = ReferenceField(User , required=True , reverse_delete_rule=CASCADE)
    goal_type = StringField()
    target = StringField()
    timeline = StringField()
    username = StringField()

class NutritionPlan(Document):
    name = StringField(required=True)
    goal = StringField(required=True)
    duration = StringField(required=True)
    guidelines = StringField()
    trainer = ReferenceField(Trainer, reverse_delete_rule=CASCADE)
    trainer_name = StringField()

class UserNutritionLog(Document):
    user = ReferenceField(User, required=True , reverse_delete_rule=CASCADE)
    date = StringField(required=True)
    nutrition_plan = StringField(required=True) 
    meals = StringField()
    calories = IntField()
    user_name = StringField()