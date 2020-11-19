from mongoengine import Document, fields



class Product(Document):
    name = fields.StringField(required=True)
    description = fields.StringField()
    params = fields.DictField()


