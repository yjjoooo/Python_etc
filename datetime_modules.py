import logging
import datetime

# logger
def log_err(msg):
    logging.error(msg)

# now formater input format
def now(format):
    return datetime.datetime.now().strftime(format)

# runtime calculater input '%Y-%m-%d %H:%M:%S' format datetime return dictionary
def calculate_runtime(start_datetime, end_datetime, unit):
    try:
        start_datetime = datetime.datetime.strptime(start_datetime, '%Y-%m-%d %H:%M:%S')
    except:
        log_err('############ Parameter \"start_datetime\" Error')
        
    try:
        end_datetime = datetime.datetime.strptime(end_datetime, '%Y-%m-%d %H:%M:%S')
    except:
        log_err('############ Parameter \"end_datetime\" Error')
    
    if unit not in ['s', 'm', 'h']:
        log_err('############ Paremeter \"unit\" Error')
    
    start_hour = start_datetime.hour
    start_minute = start_datetime.minute
    start_second = start_datetime.second
    end_hour = end_datetime.hour
    end_minute = end_datetime.minute
    end_second = end_datetime.second
    
    time_diff_days = (end_datetime - start_datetime).days
    
    run_time_dict = {}
    for i in range(0, 24):
        run_time_dict[i] = time_diff_days * 3600
    
    if start_hour == end_hour:
        run_time_dict[start_hour] += (end_minute - start_minute) * 60 + end_second - start_second
    if start_hour < end_hour:
        for i in range(start_hour + 1, end_hour):
            run_time_dict[i] += 3600
        run_time_dict[start_hour] += (60 - start_minute) * 60 - start_second
        run_time_dict[end_hour] += end_minute * 60 + end_second
    if start_hour > end_hour:
        for i in [x for x in list(range(0, 24)) if x not in list(range(end_hour, start_hour + 1))]:
            run_time_dict[i] += 3600
        run_time_dict[start_hour] += (60 - start_minute) * 60 - start_second
        run_time_dict[end_hour] += end_minute * 60 + start_second
    
    seconds_sum = 0
    for key, val in run_time_dict.items():
        seconds_sum += val
    
    if (end_datetime - start_datetime).days * 24 * 3600 + (end_datetime - start_datetime).seconds != seconds_sum:
        log_err('############ Calculate Run Time Error')

    if unit == 's':
        return run_time_dict
    elif unit == 'm':
        for i in range(0, 24):
            run_time_dict[i] = int(run_time_dict[i] / 60)
        return run_time_dict
    elif unit == 'h':
        for i in range(0, 24):
            run_time_dict[i] = int(run_time_dict[i] / 3600)
        return run_time_dict