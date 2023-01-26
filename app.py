from application.work_with_files.actions import create_data_file, write_to_output_data, read_file
from application.configs.paths import USEFUL_DATA_PATH, OUTPUT_DATA_PATH
from flask import Flask


app = Flask(__name__)


@app.route("/")
def hello_world():
    return "Hello World !"


@app.route("/get-content")
def get_useful_content():
    create_data_file("useful_data.txt")
    write_to_output_data(USEFUL_DATA_PATH)
    return read_file(OUTPUT_DATA_PATH)


if __name__ == "__main__":
    app.run()
