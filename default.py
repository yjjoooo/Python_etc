#!/usr/bin/python
# -*- coding : utf-8 -*-
'''
 @author : yjjo
'''
''' install '''

''' import '''
import sys
import python_modules as pm
import logging
from logging.config import dictConfig
import datetime
import traceback
import os

''' log '''
script_name = sys.argv[0]
file_list_getcwd = pm.read_file_list(os.getcwd())
script_abs_path = [x for x in file_list_getcwd if x.endswith(script_name)][0].rsplit('/', maxsplit = 1)[0].rsplit('\\', maxsplit = 1)[0]

pm.create_dir(os.path.join(script_abs_path, 'logs'))

def log(msg):
    logging.info(msg)

dictConfig({
    'version': 1,
    'formatters': {
        'default': {
            'format': '[%(asctime)s] %(levelname)s --- %(message)s',
        }
    },
    'handlers': {
        'file': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename': os.path.join(script_abs_path, 'logs', '{}_{}.log'.format(script_name.rsplit('.', maxsplit = 1)[0], datetime.datetime.now().strftime('%Y%m%d'))),
            'formatter': 'default',
        },
    },
    'root': {
        'level': 'INFO',
        'handlers': ['file']
    }
})

''' main function'''
def main():
    try:
        pm.script_start()
    except:
        log('######## Main Funtion Error')
        log('######## {}'.format(traceback.format_exc()))
    
''' functions '''

''' main '''
if __name__ == '__main__':
    # 시간 계산
    start_time = datetime.datetime.now()

    ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

    main()

    ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    
    log('#### ================================================')
    log('#### Run Time {}'.format(str(datetime.datetime.now() - start_time)))
    log('#### ================================================')