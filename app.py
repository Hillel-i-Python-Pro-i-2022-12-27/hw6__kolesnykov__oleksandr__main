from application.configs.paths import USEFUL_DATA_PATH, OUTPUT_DATA_PATH
from application.work_with_files.actions import create_data_file, write_to_output_data, read_file
from application.users_generator.generate_users import users_generator
from flask import Flask
from webargs import fields
from webargs.flaskparser import use_args


app = Flask(__name__)


@app.route("/")
def hello_world():
    return "Hello World !"


@app.route("/get-content/")
def get_useful_content():
    create_data_file("useful_data.txt")
    write_to_output_data(USEFUL_DATA_PATH)
    return read_file(OUTPUT_DATA_PATH)


@app.route("/generate-users/")
@use_args({"amount": fields.Int(missing=100)}, location="query")
def get_users_generator(args):
    amount = args["amount"]
    users = users_generator(amount)
    temp = "".join(f"<li>" f"<span>{user}</span>" f"</li>" for user in users)
    return f"<ol>{temp}</ol>"


if __name__ == "__main__":
    app.run()
