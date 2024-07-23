from flask import current_app
from pymongo import MongoClient
#yukledigim mongodb extension calistirmasi ve baglanilmasi
def get_db():
    if 'db' not in current_app.extensions:
        current_app.extensions['db'] = MongoClient('localhost', 27017).user_login_system
    return current_app.extensions['db']