from marshmallow import ValidationError


def validate_id(id):
    if id < 0:
        raise ValidationError("Age must > 0")
    return id


def validate_age(age):
    if age < 0:
        raise ValidationError("Age must > 0 , gia tri false: {}".format(age))
    return age


def validate_name(name):
    if len(name) > 50:
        raise ValidationError("Name must length < 50 word")
    return name
