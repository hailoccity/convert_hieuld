import os
import shutil
import zipfile


def read_zip_file(file_zip):
    archive = zipfile.ZipFile(file_zip, 'r')
    lists = archive.infolist()
    for file in lists:
        file_name = file.filename
        name = os.path.basename(file_name)  # get name + type
        names = os.path.splitext(name)[0]  # get name file
        print(name)

    txt = archive.read(lists[1])
    print(txt)


def unzip_file(file, root_dir):
    with zipfile.ZipFile(file, 'r') as zip_ref:
        zip_ref.extractall(root_dir)


def check_file(file):
    check = zipfile.is_zipfile(file)
    return check
    # return un_file

if __name__ == '__main__':
    root_dir = r'C:\Users\hieuld\PycharmProject\demo_S3\chalice-poc\tmp_unzip'
    file = r'C:\Users\hieuld\PycharmProject\demo_S3\chalice-poc\tmp\demo.zip'
    # unzip_file(file, root_dir)
    read_zip_file(file)
