import datetime
import logging
import shelve
import Send
import pprint
logging.basicConfig(filename='ProgramLog.txt', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
logging.info('Start of judge program')

now = datetime.datetime.now()

def judgedate(Time):
    reality = 0
    sdelta = datetime.timedelta(days=1)
    if now > Time and (now - Time) < sdelta:
        return True
    else:
        logging.debug('There is no cleaning schedule')
    return False

def inspect():
    shelfFile1 = shelve.open('roster_information')
    shelfFile2 = shelve.open('duty_roster')
    pprint.pprint(shelfFile2['duty_roster'])
    for date in shelfFile2['duty_roster']:
        if judgedate(date):
            Send.sendmail(list(shelfFile1['roster_information'])[0], list(shelfFile1['roster_information'].values())[0])
    shelfFile1.close()
    shelfFile2.close()

inspect()