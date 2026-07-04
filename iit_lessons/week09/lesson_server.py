# import requests

# response = requests.get("https://api.github.com")

# print(response.status_code)

#=======================================#

# import json
# person = {
# 	"name": "John",
# 	"age": 45
# }
# print(person)
# json_data = json.dumps(person)
# print(json_data)

#=======================================#

# from flask import Flask

# app = Flask(__name__)

# @app.route("/")
# def home():
#     return "Hello students!"

# @app.route("/info")
# def info():
#     return "About students"

# app.run()

#=======================================#

# from flask import Flask
# from flask import jsonify

# app = Flask(__name__)

# @app.route("/user")
# def user():
#     return jsonify({
#         "name": "John",
#         "age": 40
#     })

# app.run()

#=======================================#

# from flask import Flask

# app = Flask(__name__)

# @app.route("/<name>")
# def main(name):
#     return f"Your name is {name}"

# app.run()

#=======================================#

# from flask import Flask

# app = Flask(__name__)

# @app.route("/<name>/country/<country>")
# def main(name, country):
#     return f"Your name is {name} and your country is {country}"

# app.run()

#=======================================#

# from flask import Flask, request
# import requests

# app = Flask(__name__)

# @app.route("/")
# def main():
#     name = request.args.get("name")
#     country = request.args.get("country")
#     return f"Your name is {name} and your country is {country}"

# app.run()

#=======================================#

# from flask import Flask, request

# app = Flask(__name__)

# @app.route("/", methods=["POST"])
# def main():
#     data = request.get_json()

#     print(data)
#     return data

# app.run()

#=======================================#

# from flask import Flask
# from pydantic import BaseModel, ValidationError

# class User(BaseModel):
#     name: str
#     age: int

# app = Flask(__name__)

# @app.route("/name/<name>/age/<age>")
# def main(name, age):
#     try:
#         user = User(name=name, age=age)
#         return f"Your name is {name} and you are {age} of age"
#     except Exception as e:
#         print('833254: '+ str(e))
#         return str(e), 400

# app.run()

#=======================================#

# import requests
# import json

# weather_response = requests.get("https://api.open-meteo.com/v1/forecast?latitude=6.9271&longitude=79.8612&current_weather=true").json()
# print(weather_response)