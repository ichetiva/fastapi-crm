import os
from pathlib import Path

from dotenv import load_dotenv

env_path = Path(__file__).parent.parent / '.env'
load_dotenv(dotenv_path=env_path)

DATABASE_URI = 'postgresql://{user}:{password}@{host}/{database}'.format(
    user=os.getenv('POSTGRESQL_USER'),
    password=os.getenv('POSTGRESQL_PASSWORD'),
    host=os.getenv('POSTGRESQL_HOST'),
    database=os.getenv('POSTGRESQL_NAME'),
)

MAIL_CONFIG = {
    'username': os.getenv('MAIL_USERNAME'),
    'password': os.getenv('MAIL_PASSWORD'),
    'from': os.getenv('MAIL_FROM'),
    'port': os.getenv('MAIL_PORT'),
    'server': os.getenv('MAIL_SERVER'),
    'from_name': os.getenv('MAIL_USERNAME'),
}

DOMAIN = 'http://localhost:8080/'
