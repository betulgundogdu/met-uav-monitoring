from flask_restx import Resource, Namespace
from flask_jwt_extended import jwt_required, get_jwt_identity, create_access_token, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from .extensions import db
from .models import Drone, Task, TaskDrone, User
from .api_models import task_model, drone_model, task_input_model, drone_input_model, task_drone_model, task_drone_input_model, login_model, user_model
from datetime import datetime
from sqlalchemy.sql import func

authorizations = {
    "jsonWebToken": {
        "type": "apiKey",
        "in": "header",
        "name": "Authorization"
    }
}
ns = Namespace("api", authorizations=authorizations)

@ns.doc(security="jsonWebToken")
@ns.route('/tasks')
class TaskListAPI(Resource):
    method_decorators = [jwt_required()]
    @ns.marshal_list_with(task_model) # check returned data list
    def get(self):
        #return Task.query.filter_by(user=current_user).all()
        return Task.query.all()
    @ns.expect(task_input_model) # check expected data
    @ns.marshal_with(task_model) # check returned data 
    def post(self):
        task = Task(title=ns.payload["title"], time_created=datetime.now(), time_updated=datetime.now()) # ns.payload has data information
        db.session.add(task)
        db.session.commit()
        return task, 201 # succesfully created http status code

@ns.doc(security="jsonWebToken")
@ns.route('/tasks/<int:id>')
class TaskAPI(Resource):
    method_decorators = [jwt_required()]
    @ns.marshal_with(task_model)
    def get(self, id):
        task = Task.query.get(id)
        return task
    
    @ns.expect(task_input_model)
    @ns.marshal_with(task_model)
    def put(self, id):
        task = Task.query.get(id)
        task.title = ns.payload['title']
        task.status = ns.payload['status']
        task.desc = ns.payload['desc']
        task.user_id = ns.payload['user_id']
        task.time_updated = func.now()
        db.session.commit()
        return task, 200
    
    def delete(self, id):
        task = Task.query.get(id)
        db.session.delete(task)
        db.session.commit()

@ns.doc(security="jsonWebToken")
@ns.route('/drones')
class DroneListAPI(Resource):
    method_decorators = [jwt_required()]
    @ns.marshal_list_with(drone_model)
    def get(self):
        return Drone.query.all()
    
    @ns.expect(drone_input_model)
    @ns.marshal_with(drone_model)
    def post(self):
        drone = Drone(name=ns.payload["name"])
        db.session.add(drone)
        db.session.commit()
        return drone, 201

@ns.doc(security="jsonWebToken")
@ns.route('/drones/<int:id>')
class DroneAPI(Resource):
    method_decorators = [jwt_required()]
    @ns.marshal_with(drone_model)
    def get(self, id):
        drone = Drone.query.get(id)
        return drone
    
    @ns.expect(drone_input_model)
    @ns.marshal_with(drone_model)
    def put(self, id):
        drone = Drone.query.get(id)
        drone.name = ns.payload['name']
        drone.desc = ns.payload['desc']
        drone.time_updated = func.now()
        db.session.commit()
        return drone
    
    def delete(self, id):
        drone = Drone.query.get(id)
        db.session.delete(drone)
        db.session.commit()

@ns.doc(security="jsonWebToken")
@ns.route('/task_drone')
class TaskDroneListAPI(Resource):
    method_decorators = [jwt_required()]
    @ns.marshal_list_with(task_drone_model)
    def get(self):
        return TaskDrone.query.all()
    
    @ns.expect(task_drone_input_model)
    @ns.marshal_with(task_drone_model)
    def post(self):
        task_drone = TaskDrone(task_id=ns.payload["task_id"], drone_id=ns.payload["drone_id"])
        db.session.add(task_drone)
        db.session.commit()
        return task_drone, 201
    
@ns.doc(security="jsonWebToken")
@ns.route('/task_drone/<int:id>')
class TaskDroneAPI(Resource):
    method_decorators = [jwt_required()]
    @ns.marshal_list_with(task_drone_model)
    def get(self):
        return TaskDrone.query.get(id)
    
    @ns.expect(task_drone_input_model)
    @ns.marshal_with(task_drone_model)
    def put(self, id):
        task_drone = TaskDrone.query.get(id)
        task_drone.task_id = ns.payload['task_id']
        task_drone.drone_id = ns.payload['drone_id']
        db.session.commit()
        return task_drone, 200
    
    def delete(self, id):
        task_drone = TaskDrone.query.get(id)
        db.session.delete(task_drone)
        db.session.commit()
        return {}, 204 # no content https status code
    
@ns.route("/register")
class Register(Resource):
    @ns.expect(login_model)
    @ns.marshal_with(user_model)
    def post(self):
        user = User(username=ns.payload["username"], password_hash=generate_password_hash(ns.payload["password"]))
        db.session.add(user)
        db.session.commit()
        return user, 201
    
@ns.route("/login")
class Login(Resource):
    @ns.expect(login_model)
    def post(self):
        user = User.query.filter_by(username=ns.payload["username"]).first()
        if not user:
            return {"error": "User does not exist"}, 401
        if not check_password_hash(user.password_hash, ns.payload["password"]):
            return {"error": "Password is incorrect"}, 401
        return {"access_token": create_access_token(user)}