import logging
import os
import traceback

# logger
def log(msg):
    logging.info(msg)

# script start logger
def script_start():
    log('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
    log('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
    log('@@@@                                                                                  @@@@')
    log('@@@@    ___            _     _                                      _     _           @@@@')
    log('@@@@   / _ \          | |   | |                      _             (_)   (_)          @@@@')
    log('@@@@  / /_\ \  _   _  | |_  | |__     ___    _ __   (_)   _   _     _     _    ___    @@@@')
    log('@@@@  |  _  | | | | | | __| |  _ \   / _ \  |  __|       | | | |   | |   | |  / _ \   @@@@')
    log('@@@@  | | | | | |_| | | |_  | | | | | (_) | | |      _   | |_| |   | |   | | | (_) |  @@@@')
    log('@@@@  \_| |_/  \__ _|  \__| |_| |_|  \___/  |_|     (_)   \__  |   | |   | |  \___/   @@@@')
    log('@@@@                                                       __/ |  _/ |  _/ |          @@@@')
    log('@@@@                                                      |___/  |__/  |__/           @@@@')
    log('@@@@                                                                                  @@@@')
    log('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
    log('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')

# file reader as list with full path
def read_file_list(path):
    try:
        log('#### Read Path {}'.format(path))
        file_list = list([])
        
        for dir_path, _, file_name in os.walk(path):
            for f in file_name:
                try:
                    file_list.append(os.path.abspath(os.path.join(dir_path, f)))
                except:
                    log('######## Read File \'{}\' Error'.format(file_name))
                    log('######## {}'.format(traceback.format_exc()))
                
        return file_list
    except:
        log('######## Read File List Error')
        log('######## {}'.format(traceback.format_exc()))

# directory creater
def create_dir(path):
    try:
        log('#### Create Directory')
        if not os.path.exists(path):
            os.makedirs(path)
        else:
            log('######## Directory \'{}\' Already Exist'.format(path))
    except:
        log('######## Create Directory \'{}\' Error'.format(path))
        log(traceback.format_exc())