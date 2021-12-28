import csv, json
import os
from marshmallow import Schema, fields, ValidationError
from schema_user import ValueSchema, UserSchema
from datetime import datetime

root_dir = r'C:\Users\hieuld\PycharmProjects\convert_hieuld\ConvertCsv\file_data'
save_dir = r"C:\Users\hieuld\PycharmProjects\convert_hieuld\ConvertCsv\file_converted"


def obj_dict(obj):
    return obj.__dict__


class Set_id:
    def __init__(self, pharmacy_id):
        self.updated = str(datetime.now())
        self.pharmacy_id = pharmacy_id
        self.user = General()


def General():
    user = [
        {
            "id": "1",
            "name": "HieuLD"
        }
    ]
    # temp = [
    #     {
    #         "description": "Ominext",
    #         "updated": str(datetime.now()),
    #         "pharmacy_id": "1",
    #         "user": user
    #     }
    # ]
    return user


class Value_Generic:
    def __init__(self, state, remark):
        self.state = state
        self.remark = remark


class Generic:
    def __init__(self, value=Value_Generic):
        self.value = value


class Value_Prescription:

    def __init__(self, need, cause):
        self.need = str(need)
        self.cause = str(cause)


class Prescription_note:
    def __init__(self, value=Value_Prescription):
        self.value = value


class Pharmacist:
    def __init__(self, value, agreement_date, remark):
        self.value = value
        self.agreement_date = agreement_date
        self.remark = remark


class Weight:
    def __init__(self, value):
        self.value = int(value)
        self.update = str(datetime.now())

    # @property
    # def value(self):
    #     return self.value
    #
    # @value.setter
    # def value(self, value):
    #     if int(value) < 0:
    #         raise Exception("Weight cannot < 0")
    #     self.value = value


class Height:
    def __init__(self, value):
        self.value = int(value)
        self.update = str(datetime.now())


class Patient:

    def __init__(self, id, patient_id, nsips_patient_id, pharmacy_id, sex, prescription_note=Prescription_note,
                 pharmacis=Pharmacist, weight=Weight, height=Height, generic=Generic):
        self.id = int(id)
        self.patient_id = patient_id
        self.nsips_patient_id = nsips_patient_id
        self.pharmacy_id = pharmacy_id
        self.updated = str(datetime.now())
        self.sex = int(sex)
        self.prescription_note = prescription_note
        self.pharmacist = pharmacis
        self.weight = weight
        self.height = height
        self.generic = generic


def convert(root_dir, saves_dir):
    file_names = os.listdir(root_dir)
    for file_paths in file_names:
        file_path = os.path.join(root_dir, file_paths)
        # rows = []
        data_object = []
        file_name = os.path.basename(file_path).split(".")[0]
        try:
            with open(file_path) as stream:
                reader = csv.DictReader(stream)

                for row in reader:
                    get_value_pre = Value_Prescription(row["need"], row["cause"])
                    get_set_id = Set_id(row["pharmacy_id"])
                    get_value_generic = Value_Generic(row["state"], row["remark"])
                    # get_weight = Weight(row["value_weight"])
                    # get_height = Height(row["value_height"])
                    get_value_prescription_note = Prescription_note([get_value_pre])
                    get_value_pharmacist = Pharmacist(row['value_phar'], row["agreement_date"], row["remark"]
                                                      )
                    get_generic = Generic(get_value_generic)

                    data_object.append(
                        Patient(row["id"], row["patient_id"], row["nsips_patient_id"], row["pharmacy_id"], row["sex"],
                                get_value_prescription_note, get_value_pharmacist,
                                Weight(row["weight"]), Height(row["height"]), get_generic))
                    # get_weight,
                    # get_height, get_generic))

            # validate data hear

            saves_file = os.path.join(saves_dir, file_name)
            # print(rows)
            # data[row['Id']] = record = {}
            # for header, value in row.items():

            # process(header, value, record)
            show = json.dumps(data_object, default=obj_dict, indent=4)
            # print(show)

            with open(saves_file + '.json', "w") as stream:
                stream.write(show)
        except Exception as e:
            print(e)
            # print(e)

        # try:
        #     # user_schema = UserSchema()
        #     # show = json.dumps(data_object, default=obj_dict, indent=4)
        #     # dump_schema = user_schema.dumps(data_object, many=True)
        #     show_schema = UserSchema(many=True).loads(show)
        #     print(show_schema)
        # except ValidationError as e:
        #     print(e.messages)


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
