import csv
from application.configs.paths import PATH_TO_CSV


def find_average_parameters(path_to_csv_file):

    with open(path_to_csv_file) as csv_file:

        height_inches_list = []
        weight_pounds_list = []

        reader = csv.DictReader(csv_file)

        for row in reader:
            height_inches_list.append(float(row["Height(Inches)"]))
            weight_pounds_list.append(float(row["Weight(Pounds)"]))

        average_height_inches = sum(height_inches_list) / len(height_inches_list)
        average_weight_pounds = sum(weight_pounds_list) / len(weight_pounds_list)

    return average_height_inches, average_weight_pounds


def get_formatted_parameters():
    average_height, average_weight = find_average_parameters(PATH_TO_CSV)
    height_sm = round((average_height * 2.54), 2)
    weight_kg = round((average_weight * 0.453592), 2)

    return f"Средний рост в см: {height_sm}, средний вес в кг: {weight_kg}"
