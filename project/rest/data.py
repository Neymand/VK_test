from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import database_exists, create_database

from settings import postgresql as settings

def get_engine(user, password, host, port, db):
    url = f'postgresql://{user}:{password}@{host}:{port}/{db}'
    if not database_exists(url):
        create_database(url)
    engine = create_engine(url, pool_size=50, echo=False)
    return engine

engine = get_engine(settings['pguser'],
                    settings['pgpassword'],
                    settings['pghost'],
                    settings['pgport'],
                    settings['pgdb'])

engine.url

def get_engine_from_settings():
    keys = ['pguser', 'pgpassword', 'pghost', 'pgport', 'pgdb']
    if not all(key in keys for key in settings.keys()):
        raise Exception('Bad config file')

    return get_engine(settings['pguser'],
                    settings['pgpassword'],
                    settings['pghost'],
                    settings['pgport'],
                    settings['pgdb'])


def get_session():
    engine = get_engine_from_settings()
    session = sessionmaker(bind=engine) ()
    return session

session = get_session()





