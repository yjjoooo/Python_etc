import logging
import traceback
import pandas as pd
from sqlalchemy import create_engine
import urllib

# DATABASE 정보 세팅
DATABASE = {
    'dbms' : 'postgresql',
    'username' : 'user',
    'password' : urllib.parse.quote('password', safe=''), # 비밀번호 특수문자 대비
    'host' : 'host',
    'port' : '5432',
    'database' : 'db',
}

DB_INFO = '{}://{}:{}@{}:{}/{}'.format(DATABASE['dbms'], DATABASE['username'], DATABASE['password'], DATABASE['host'], DATABASE['port'], DATABASE['database'])
    
# DATABASE 엔진 생성
def create_db_engine(db_info):
    try:
        logging.info('#### Create Database Engine \"{}\"'.format(db_info))
        return create_engine(db_info)
    except RuntimeWarning as w:
        logging.warning(w)
    except:
        logging.error('############ Create Database Engine Error')
        logging.error(traceback.format_exc())

# DATABASE SELECT * FROM 테이블
def select_table(engine, table_name):
    try:
        logging.info('#### Select Table : \"{}\"'.format(table_name))
        df = pd.read_sql(
            sql = 'select * from {}'.format(table_name),
            con = engine,
        )

        return df
    except RuntimeWarning as w:
        logging.warning(w)
    except:
        logging.error('############ Read Table \"{}\" Error'.format(table_name))
        logging.error(traceback.format_exc())

# DATABASE INSERT TO TABLE 테이블
def insert_to_table(engine, table_name, df):
    try:
        logging.info('#### Insert To Table \"{}\"'.format(table_name))
        df.to_sql(
            name = table_name,
            con = engine,
            if_exists = 'append',
            index = False,
        )
    except RuntimeWarning as w:
        logging.warning(w)
    except:
        logging.error('############ Insert To Table \"{}\" Error'.format(table_name))
        logging.error(traceback.format_exc())