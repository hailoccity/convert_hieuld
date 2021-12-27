from marshmallow import Schema, fields, ValidationError, EXCLUDE, validates
from datetime import datetime


def validate_year(value):
    if value < 0:
        raise ValidationError("Year: Invalid")
    if value > datetime.now().year:
        raise ValidationError("Year Invalid")
