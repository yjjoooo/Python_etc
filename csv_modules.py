import logging
import traceback
import pandas as pd
import os

# logger
def log(msg):
    logging.info(msg)

def log_warn(msg):
    logging.warning(msg)

def log_err(msg):
    logging.error(msg)

# csv reader (UP plz!)
def read_csv(path):
    try:
        log('#### Read CSV \"{}\"'.format(path))
        return pd.read_csv(path)
    except RuntimeWarning as w:
        log_warn(w)
    except:
        log_err('############ Read CSV \"{}\" Error'.format(path))
        log(traceback.format_exc())

# csv saver
def save_csv(df, path):
    try:
        log('#### Save CSV \"{}\"'.format(path))
        
        file_name, extension = os.path.splitext(path)
        
        save_count = 0
        while True:
            if os.path.exists(path):
                log('######## CSV \"{}\" Already Exist'.format(path))
                save_count += 1
                path = '{}_{}{}'.format(file_name, save_count, extension)
            else:
                break
            
        log('######## Save CSV \"{}\" as \"{}\"'.format(file_name + extension, path))
        df.to_csv(path, encoding = 'UTF-8', index = False)
    except RuntimeWarning as w:
        log_warn(w)
    except:
        log_err('############ Save CSV \"{}\" Error'.format(path))
        log(traceback.format_exc())

# big csv reader
def read_big_csv(path, chunksize):
    try:
        log('#### Read CSV \"{}\"'.format(path))
        return pd.read_csv(path, chunksize = chunksize)
    except RuntimeWarning as w:
        log_warn(w)
    except:
        log_err('############ Read CSV \"{}\" Error'.format(path))
        log(traceback.format_exc())

# big csv saver
def save_big_csv(df, path, index):
    try:
        log('#### Save CSV {0: >3} {}'.format('({})'.format(index), path))
        
        if index == 0:
            df.to_csv(path, encoding = 'UTF-8', index = False)
        elif index > 0:
            df.to_csv(path, encoding = 'UTF-8', index = False, header = False, mode = 'a')
        else:
            log_err('######## Please Check CSV Index \"{}\"'.format(path))
    except RuntimeWarning as w:
        log_warn(w)
    except:
        log('############ Save CSV {0: >3} \"{}\" Error'.format('({})'.format(index), path))
        log(traceback.format_exc())