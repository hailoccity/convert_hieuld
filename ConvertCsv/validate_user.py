from marshmallow import ValidationError


class Validate_Obj:
    # Validate tung truong trong bang du lieu
    #
    @staticmethod
    def validate(self, objects):
        for obj in objects:
            pass
    pass


def validate_id(ids):
    if ids < 0:
        raise ValidationError("Age must > 0")
    return ids


def validate_age(age):
    if age < 0:
        raise ValidationError("Age must > 0 , gia tri false: {}".format(age))
    return age


def validate_name(name):
    if len(name) > 50:
        raise ValidationError("Name must length < 50 word")
    return name
