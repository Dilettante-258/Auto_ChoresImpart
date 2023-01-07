import datetime
import logging
import shelve
import Send
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
logging.info('Start of judge program')

now = datetime.datetime.now()
Be = datetime.datetime(2023, 2, 13)
def judgedate(Time):
    sdelta = datetime.timedelta(days=1)
    if (now > Time) and ((now - Time) < sdelta):
        logging.info('return True')
        return True
    else:
        logging.debug('There is no cleaning schedule')
    return False

#传递数据
shelfFile1 = shelve.open('roster_information')
shelfFile2 = shelve.open('duty_roster')

#第一次启动
if now < Be:
    logging.info('Ready to the impart.')
    for date in shelfFile2['duty_roster']:
        logging.info('Send the first mail to %s - %s...' % (list(shelfFile1['roster_information'])[0], list(shelfFile1['roster_information'].values())[0]))
        Send.sendfirstmail(list(shelfFile1['roster_information'])[0], list(shelfFile1['roster_information'].values())[0])


def inspect():
    for date in shelfFile2['duty_roster']:
        if judgedate(date):
            Send.sendmail(list(shelfFile1['roster_information'])[0], list(shelfFile1['roster_information'].values())[0])

inspect()
logging.info('Finished inspection.')
shelfFile1.close()
shelfFile2.close()

