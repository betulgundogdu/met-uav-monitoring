from flask_restx import fields
from .extensions import api

user_model = api.model("User", {
    "id": fields.Integer,
    "username": fields.String,
    "type": fields.Boolean,
})

login_model = api.model("Login", {
    "username": fields.String,
    "password": fields.String
})

drone_model = api.model("Drone", {
    "id": fields.Integer,
    "name": fields.String,
    "desc": fields.String
})

drone_input_model = api.model("DroneInput", {
    "name": fields.String,
    "desc": fields.String
})

task_drone_model = api.model("TaskDrone", {
    "id": fields.Integer,
    "task_id": fields.Integer,
    "drone_id": fields.Integer,
})

task_drone_input_model = api.model("TaskDroneInput", {
    "task_id": fields.Integer,
    "drone_id": fields.Integer
})

task_model = api.model("Task", {
    "id": fields.Integer,
    "title": fields.String,
    "desc": fields.String,
    "status": fields.String,
    "drones": fields.List(fields.Nested(drone_model)),
    # "user_id": fields.Integer,
    "time_created": fields.DateTime,
    "time_updated": fields.DateTime
})

task_input_model = api.model("TaskInput", {
    "title": fields.String,
    "desc": fields.String,
    "status": fields.String,
    "user_id": fields.Integer,
    "time_created": fields.DateTime,
    "time_updated": fields.DateTime
})

