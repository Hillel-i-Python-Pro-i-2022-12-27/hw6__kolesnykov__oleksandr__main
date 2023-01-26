from application.configs.paths import INPUT_FILES_PATH, OUTPUT_DATA_PATH


def create_temp_data():
    return "Hello ! I am a file with very important information !"


def create_data_file(file_name):
    path_to_file = INPUT_FILES_PATH.joinpath(f"{file_name}")

    with open(path_to_file, mode="w", encoding="UTF-8") as new_file:
        new_file.writelines(create_temp_data())


def read_file(path_to_file):
    with open(path_to_file, encoding="UTF-8") as file_to_read:
        return file_to_read.read()


def write_to_output_data(file_to_read_path, file_to_write_path=OUTPUT_DATA_PATH):
    with open(file_to_write_path, mode="w", encoding="UTF-8") as file_to_write:
        file_to_write.writelines(read_file(file_to_read_path))
