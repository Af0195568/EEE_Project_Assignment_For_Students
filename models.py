from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()
class Employee(db.Model):
    _tablename_ = "Employee"

    id = db.Column(db.Integer, primary_key=True)
    employee_id = db.Column(db.Integer(),unique = True)

    name = db.Column(db.String())
    age = db.Column(db.Integer())
    position = db.Column(db.String(80))

    def _init_(self, employee_id, name, age, position, email):
        self.employee_id = employee_id
        self.name = name
        self.age = age
        self.position = position
        self.email = email

    def _repr_(self):
        return f"{self.name}:{self.employee_id}"