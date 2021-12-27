from marshmallow import Schema, fields, ValidationError, EXCLUDE, validates, post_load
from validate_user import *


class ValueSchema(Schema):
    need = fields.String()
    cause = fields.String()


class UserSchema(Schema):
    id = fields.Integer()
    name = fields.String(validate=validate_name)
    age = fields.Integer(validate=validate_age)
    address = fields.String()
    value = fields.Nested(ValueSchema)
