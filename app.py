from flask import Flask
from webargs import fields
from webargs.flaskparser import use_args

from application.astronauts_info.info_about_astronauts import list_of_astronauts, get_count_of_astronauts
from application.configs.paths import USEFUL_DATA_PATH, OUTPUT_DATA_PATH
from application.find_average.find_average import get_formatted_parameters
from application.work_with_files.actions import create_data_file, write_to_output_data, read_file
from application.users_generator.generate_users import users_generator

from application.db_services.db_create_table import create_db_table
from application.db_services.db_connection import DBConnection

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


@app.route("/space/")
def get_info_about_astronauts():
    temp = "".join(f"<li>" f"<span>{astronaut}</span>" f"</li>" for astronaut in list_of_astronauts())
    return f"""
    Сейчас в космосе {get_count_of_astronauts()} космонавтов
    <ol>{temp}</ol>
    """


@app.route("/mean/")
def get_the_mean():
    return get_formatted_parameters()


@app.route("/db/create_user")
@use_args({"contact_name": fields.Str(required=True), "phone_value": fields.Int(required=True)}, location="query")
def create_user(args):
    with DBConnection() as connection:
        with connection:
            connection.execute(
                "INSERT INTO phones (contact_name, phone_value) VALUES (:contact_name, :phone_value);",
                {"contact_name": args["contact_name"], "phone_value": args["phone_value"]},
            )

    return "Success"


create_db_table()

if __name__ == "__main__":
    app.run()
