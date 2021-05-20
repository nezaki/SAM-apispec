from marshmallow import Schema, fields


class ExampleSchema(Schema):
    id = fields.Int()
    content = fields.Str()
