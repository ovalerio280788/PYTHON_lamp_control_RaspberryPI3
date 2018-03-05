import datetime


def print_timestamp(type="info", message=""):
    time = datetime.datetime.now()
    print("{0} -- [ {1} ] -- {2}".format(time, type, message))
