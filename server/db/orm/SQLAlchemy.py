import os
from configparser import ConfigParser
from flask_sqlalchemy import SQLAlchemy

THIS_DIR = os.path.dirname(os.path.realpath(__file__))
DB_CONFIG_PATH = os.path.join(THIS_DIR, '..', 'config', 'postgreSQL.ini')
alchemist = SQLAlchemy()

def parse_config(config_path=DB_CONFIG_PATH, section='postgresql'):
    # create a parser
    parser = ConfigParser()

    # read the configuration
    parser.read(config_path)

    # get the section
    obj = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            obj[param[0]] = param[1]

    else:
        raise Exception(
            'Section {0} not found in the {1} file'.format(section, config_path))
    return obj


def get_postgres_url(config_path=DB_CONFIG_PATH):
    postgres_url = parse_config()
    url_base = 'postgresql+psycopg2://{user}:{pw}@{host}/{db}'.format(
        user=postgres_url['user'], pw=postgres_url['password'], host=postgres_url['host'], db=postgres_url['database'])
    return url_base
    # try:
    #     postgres_config = parse_config(
    #         config_path=config_path, section='postgresql')
    # except Exception as exc:
    #     print('Exception while parsing Postgres config')
    #     print(type(exc).__name__, str(exc))
    #     postgres_config = {
    #         'user': os.environ.get('POSTGRES_USER', 'postgres'),
    #         'password': os.environ.get('POSTGRES_PASSWORD', ''),
    #         'host': os.environ.get('POSTGRES_HOST', 'localhost'),
    #         'database': os.environ.get('POSTGRES_DATABASE', 'flask'),
    #     }
    # postgres_url = url_base.format(**postgres_config)
    # return postgres_url