import csv
import json
import os
import shutil
import zipfile
import logging

logging.basicConfig(level=logging.DEBUG, filename="sample.log")


def read_zip_file(root_dir, save_file):
    list_name_csv = []
    global name
    file_names = os.listdir(root_dir)
    for file_name in file_names:
        file_path = os.path.join(root_dir, file_name)
        # pass
        archive = zipfile.ZipFile(file_path, 'r')
        archive.extractall(save_file)
        lists = archive.infolist()
        print("List file of folder zip name : {}".format(file_name))
        for file in lists:
            file_namess = file.filename
            name = os.path.basename(file_namess)
            if name == '':
                continue
            list_name_csv.append(name)
            # names = os.path.splitext(name)[0]  # get name file
            print(name)

            # print("Content of file name : {} \n".format(name))
            # if name == "deniro.csv":
            #     txt = archive.read(file)
            #     print(txt)
            #     print("\n")
            # result = json.dumps(txt, indent=2)
            # print(txt)
    return list_name_csv


def read_file_csv(file):
    rows = []
    file_name = os.path.basename(file)
    with open(file) as stream:
        reader = csv.DictReader(stream)
        header = reader.fieldnames
        i = 0
        for row in reader:

            rows.append(row)
            check = 0
            for value in row.values():
                if value is None or value == '':
                    logging.error(" Thu tu row: {}, Value: {} , File name: {}".format(i, row, file_name))
                    continue
            i += 1


    return rows


def unzip_file(files, root_dir):
    with zipfile.ZipFile(files, 'r') as zip_ref:
        zip_ref.extractall(root_dir)


def check_file_zip(files):
    check = zipfile.is_zipfile(files)
    return check
    # return un_file


def check_file_csv(files):
    pass


def check_size_file(files):
    size = os.path.getsize(files)
    if size == 0:
        return False
    return True


def check_font_file(files):
    pass


if __name__ == '__main__':
    save_file = r'C:\Users\hieuld\PycharmProjects\convert_hieuld\ConvertCsv\unzip'
    root_dir = r'C:\Users\hieuld\PycharmProjects\convert_hieuld\ConvertCsv\data'
    root_dir_zip = r"C:\Users\hieuld\PycharmProjects\convert_hieuld\ConvertCsv\data_zip_test"
    file_false = r"C:\Users\hieuld\PycharmProjects\convert_hieuld\ConvertCsv\file_data_false"
    file_test = r"C:\Users\hieuld\PycharmProjects\convert_hieuld\ConvertCsv\file_data"

    # THực hiện loại bỏ các file không đúng định dạng
    file_names = os.listdir(file_test)
    for file_name in file_names:
        file_path = os.path.join(file_false, file_name)
        if check_size_file(file_path) is False:
            logging.warning("File has size invalid: {}".format(file_name))
            continue
        result = read_file_csv(file_path)
        # saves_dir = os.path.join(file_false, file_name)
        # if check_size_file(file_path) is False:
        #     shutil.copyfile(file_path, saves_dir)
        #     os.remove(file_path)
        #     continue

        print(result)

    # file = read_file_csv(file_test)
