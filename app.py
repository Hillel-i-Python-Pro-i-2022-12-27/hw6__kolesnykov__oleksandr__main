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
def phones_create_user(args):
    with DBConnection() as connection:
        with connection:
            connection.execute(
                "INSERT INTO phones (contact_name, phone_value) VALUES (:contact_name, :phone_value);",
                {"contact_name": args["contact_name"], "phone_value": args["phone_value"]},
            )

    return "Success"


@app.route("/db/read-all")
def phones_read_all():
    with DBConnection() as connection:
        phones = connection.execute("SELECT * FROM phones;").fetchall()

    return "<br>".join([f'{user["phone_id"]}: {user["contact_name"]} - {user["phone_value"]}' for user in phones])


@app.route("/db/read/<int:phone_id>")
def phones_users__read(phone_id: int):
    with DBConnection() as connection:
        user = connection.execute(
            "SELECT * " "FROM phones " "WHERE (phone_id=:phone_id);",
            {
                "phone_id": phone_id,
            },
        ).fetchone()

    return f'{user["phone_id"]}: {user["contact_name"]} - {user["phone_value"]}'


@app.route("/db/update/<int:phone_id>")
@use_args({"contact_name": fields.Str(), "phone_value": fields.Int()}, location="query")
def phones_users_update(args, phone_id):
    with DBConnection() as connection:
        with connection:
            contact_name = args.get("contact_name")
            phone_value = args.get("phone_value")

            if contact_name is None and phone_value is None:
                return "Need to provide at least one argument"

            args_for_request = []

            if contact_name is not None:
                args_for_request.append("contact_name=:contact_name")
            if phone_value is not None:
                args_for_request.append("phone_value=:phone_value")

            args_2 = ", ".join(args_for_request)

            connection.execute(
                "UPDATE phones " f"SET {args_2} " "WHERE phone_id=:phone_id;",
                {
                    "phone_id": phone_id,
                    "contact_name": contact_name,
                    "phone_value": phone_value,
                },
            )

    return "Success"


@app.route("/db/delete_user/<int:phone_id>")
def phones_delete_user(phone_id):
    with DBConnection() as connection:
        with connection:
            connection.execute(
                "DELETE " "FROM phones " "WHERE (phone_id=:phone_id);",
                {
                    "phone_id": phone_id,
                },
            )

    return "Success"


create_db_table()


if __name__ == "__main__":
    app.run()
