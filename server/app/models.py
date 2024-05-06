from .extensions import db
from sqlalchemy.sql import func


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True)
    password_hash = db.Column(db.String(100))
    tasks = db.relationship("Task", back_populates="user")

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), unique=True)
    desc = db.Column(db.String(255))
    status = db.Column(db.String(50))
    drones = db.relationship("Drone", secondary="task_drone", backref="tasks")
    user_id = db.Column(db.ForeignKey("user.id"))
    user = db.relationship("User", back_populates="tasks")

    time_created = db.Column(db.DateTime(timezone=True), server_default=func.now())
    time_updated = db.Column(db.DateTime(timezone=True), onupdate=func.now())

class Drone(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True)
    desc = db.Column(db.String(255))

# This model is created to keep many-to-many drone-task relation information
# A task can have assigned drone(s) and a drone can be assigned multiple tasks,
# therefore many-to-many relation is required
# Also we can keep historical data of tasks with images
class TaskDrone(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    task_id = db.Column(db.Integer, db.ForeignKey("task.id", ondelete="CASCADE"))
    drone_id = db.Column(db.Integer, db.ForeignKey("drone.id", ondelete="CASCADE"))
