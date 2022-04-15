import peewee
from peewee import SqliteDatabase, Model, IntegerField, TextField, ForeignKeyField, MySQLDatabase, TimestampField, \
    CharField, BooleanField, TimestampField, PrimaryKeyField

DB = 'my_proj'

database = peewee.MySQLDatabase(DB,
                                host='127.0.0.1',
                                user='root',
                                password=''
                                )


class BaseModel(Model):
    class Meta:
        database = database


class Role(BaseModel):
    """"""
    role_id = PrimaryKeyField()
    role_name = CharField(default='', unique=True)
    added = TimestampField()

    class Meta:
        db_table = f'roles'


class User(BaseModel):
    """

    """
    user_id = PrimaryKeyField()
    nick = CharField(default='')
    password = CharField(default='')
    email = CharField(default='', unique=True)
    banned = BooleanField(default=False)
    added = TimestampField()
    role = ForeignKeyField(Role, backref='users')

    class Meta:
        db_table = f'users'


class Category(BaseModel):
    """

    """
    category_id = PrimaryKeyField()
    category_name = CharField(default='')
    added = TimestampField(default='')


class Game(BaseModel):
    """

    """
    game_id = PrimaryKeyField()
    game_version = CharField()


class Project(BaseModel):
    """

    """
    project_id = PrimaryKeyField()
    title = CharField(default='')
    desc = TextField(default='')
    category = ForeignKeyField(Category, default='', backref='projects')
    game_version = ForeignKeyField(Game, default='')
    mods = TextField(default='')
    user = ForeignKeyField(User)


class File(BaseModel):
    """

    """
    file_id = PrimaryKeyField(default='')
    project = ForeignKeyField(Project, backref='files')
    path = CharField(default='')
    crc = CharField(default='')
    added = TimestampField()


class Image(BaseModel):
    """

    """
    image_id = PrimaryKeyField()
    project = ForeignKeyField(Project, backref='images')
    path = CharField(default='')
    crc = CharField(default='')
    added = TimestampField()
