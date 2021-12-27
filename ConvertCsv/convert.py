import csv, json
import os
from marshmallow import Schema, fields, ValidationError
from schema_user import ValueSchema, UserSchema
from datetime import datetime

root_dir = r'C:\Users\hieuld\PycharmProject\convert_json\ConvertCsv\file_data'
save_dir = r"C:\Users\hieuld\PycharmProject\convert_json\ConvertCsv\file_converted"


def obj_dict(obj):
    return obj.__dict__


#
# class Note_User:
#     def __init__(self):
#         self.id = 1
#         self.name = "HieuLD"
def users():
    user = [
        {
            "id": "1",
            "name": "HieuLD"
        }
    ]
    return user


class Value_Prescription:

    def __init__(self, need, cause):
        self.need = str(need)
        self.cause = str(cause)


class Prescription_note:
    def __init__(self, value=Value_Prescription):
        self.value = value
        self.decristion = "Hello World"
        self.Users = users()


class Weight:
    def __init__(self, value):
        self.value = value
        self.update = str(datetime.now())


class Height:
    def __init__(self, value):
        self.value = value
        self.update = str(datetime.now())


class User:

    def __init__(self, id, name, age, address, prescription_note=Prescription_note, weight=Weight, height=Height):
        self.id = int(id)
        self.name = str(name)
        self.age = int(age)
        self.address = str(address)
        self.prescription_note = prescription_note
        self.weight = weight
        self.height = height


def convert(root_dir, saves_dir):
    file_names = os.listdir(root_dir)
    for file_paths in file_names:
        file_path = os.path.join(root_dir, file_paths)
        # rows = []
        data_object = []
        file_name = os.path.basename(file_path).split(".")[0]
        with open(file_path) as stream:
            reader = csv.DictReader(stream)
            for row in reader:
                get_value_pre = Value_Prescription(row["need"], row["cause"])
                get_weight = Weight(row["value_weight"])
                get_height = Height(row["value_height"])
                get_value = Prescription_note(get_value_pre)

                # rows.append(row)

                data_object.append(
                    User(row["id"], row["name"], row["age"], row["address"], get_value, get_weight, get_height))

        # validate data ngay trong nay

        saves_file = os.path.join(saves_dir, file_name)
        # print(rows)
        # data[row['Id']] = record = {}
        # for header, value in row.items():

        # process(header, value, record)
        show = json.dumps(data_object, default=obj_dict, indent=4)
        # print(show)

        with open(saves_file + '.json', "w") as stream:
            stream.write(show)
        try:
            # user_schema = UserSchema()
            # show = json.dumps(data_object, default=obj_dict, indent=4)
            # dump_schema = user_schema.dumps(data_object, many=True)
            show_schema = UserSchema(many=True).loads(show)
            print(show_schema)
        except ValidationError as e:
            print(e.messages)


def convert_v2(csv_file):
    file = open(csv_file, 'r')
    csvreader = csv.reader(file)
    header = next(csvreader)
    print(header)
    rows = []
    for row in csvreader:
        rows.append(row)
    result = json.dumps(rows)
    print(result)
    with open("test_v2.json", 'w') as f:
        json.dump(rows, f, indent=2)
    file.close()


if __name__ == '__main__':
    convert(root_dir, save_dir)
