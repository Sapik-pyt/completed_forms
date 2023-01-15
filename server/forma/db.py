from tinydb import TinyDB


def get_db():
    db = TinyDB('db.json').table('forms')
    return db
