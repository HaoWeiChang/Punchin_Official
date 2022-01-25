from datetime import datetime, timedelta


def time_format(timestamp):
    '''處理Line timestamp'''
    timestamp /= 1000
    punchin = datetime.fromtimestamp(timestamp)
    punchin_format = punchin.strftime('%Y/%m/%d %H:%M:%S')
    '''將下班時間文字化'''
    getoff = punchin + timedelta(hours=9)
    getoff_format = getoff.strftime('%Y/%m/%d %H:%M:%S')
    return punchin_format, getoff_format
