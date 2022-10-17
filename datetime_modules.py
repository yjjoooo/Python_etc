import datetime

# now formater input format
def now(format):
    return datetime.datetime.now().strftime(format)