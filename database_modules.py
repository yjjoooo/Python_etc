import logging
import traceback
import pandas as pd
from sqlalchemy import create_engine

# logger
def log(msg):
    logging.info(msg)

def log_warn(msg):
    logging.warning(msg)

def log_err(msg):
    logging.error(msg)
    
# database engine creater
def create_db_engine(db_info):
    try:
        log('#### Create Database Engine \"{}\"'.format(db_info))
        return create_engine(db_info)
    except RuntimeWarning as w:
        log_warn(w)
    except:
        log_err('############ Create Database Engine Error')
        log_err(traceback.format_exc())

# table selector from database
def select_table(engine, table_name):
    try:
        log('#### Select Table : \"{}\"'.format(table_name))
        df = pd.read_sql(
            sql = 'select * from {}'.format(table_name),
            con = engine,
        )

        return df
    except RuntimeWarning as w:
        log_warn(w)
    except:
        log_err('############ Read Table \"{}\" Error'.format(table_name))
        log_err(traceback.format_exc())

# dataframe inserter to database
def insert_to_table(engine, table_name, df):
    try:
        log('#### Insert To Table \"{}\"'.format(table_name))
        df.to_sql(
            name = table_name,
            con = engine,
            if_exists = 'append',
            index = False,
        )
    except RuntimeWarning as w:
        log_warn(w)
    except:
        log_err('############ Insert To Table \"{}\" Error'.format(table_name))
        log_err(traceback.format_exc())