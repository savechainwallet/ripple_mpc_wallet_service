from peewee import DatabaseProxy, Model
database_proxy = DatabaseProxy()  # Create a proxy for our db.

class BaseModel(Model):
    class Meta:
        database = database_proxy