#! /usr/bin/python3

import subprocess
import random
import datetime, time
# bashCommand = "touch TEST"
# process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
# output, error = process.communicate()
# print(output)

def unix(yr, m, d):
    d = datetime.date(yr, m, d)
    unix_timestamp = int(time.mktime(d.timetuple()))
    twelve_hrs = 12 * 60**2
    return unix_timestamp + twelve_hrs


def addCommit(timestamp):
    nonce = random.randrange(16**10)
    touch = "touch " + str(nonce)
    add = "git add ."
    # commit = "git commit --date={0} -0800".format(timestamp)
    commit = 'git commit --date={0} -m {0}'.format(timestamp)
    # push = "git push"
    run = [touch, add, commit]
    for cmd in run:
        subprocess.Popen(cmd.split())
        time.sleep(2)

def cleanUpPush():
    push = "git push"
    subprocess.Popen(push.split())


def topLeft():
    """ return top left date (pixel) in the github history bar """
    """ presupposition: top left date is the monday before the date we are currently in one year ago """
    now = time.gmtime()
    yr_ago = now.tm_year - 1
    mo = now.tm_mon
    day = now.tm_mday
    return unix(yr_ago, mo, day)


a_hr = 60**2
a_day = 24 * a_hr
a_wk = 7 * a_day

def datesToColor(topLeft):
    """ return list of dates (unix timestamps) that need colorin """
    def fiv_vert(date):
        return [date, date + a_day, date + 2*a_day, date + 3*a_day, date + 4*a_day]

    def two_horiz(date):
        return [date, date + a_wk]

    def capital_H(date):
        capital_H = []
        capital_H += fiv_vert(date)
        capital_H += two_horiz(date + 2*a_day + a_wk)
        capital_H += fiv_vert(date + 3*a_wk)
        capital_H = set(capital_H)
        capital_H = list(capital_H)
        return capital_H

    def capital_E(date):
        offset = date + 6*a_wk
        vert = fiv_vert(offset)
        horiz = two_horiz(offset + a_wk) + two_horiz(offset + 2*a_day + a_wk) + two_horiz(offset + 4*a_day + a_wk)
        capital_E = vert + horiz
        capital_E = set(capital_E)
        capital_E = list(capital_E)
        return capital_E

    def capital_L(date):
        offset = date + 11*a_wk
        capital_L = []
        capital_L += fiv_vert(offset)
        capital_L += two_horiz(offset + 4*a_day + a_wk)
        capital_L = set(capital_L)
        capital_L = list(capital_L)
        return capital_L

    def capital_L2(date):
        offset = date + 16*a_wk
        capital_L = []
        capital_L += fiv_vert(offset)
        capital_L += two_horiz(offset + 4*a_day + a_wk)
        capital_L = set(capital_L)
        capital_L = list(capital_L)
        return capital_L

    def capital_O(date):
        offset = date + 21*a_wk
        capital_O = []
        capital_O += fiv_vert(offset) + fiv_vert(offset + 3*a_wk)
        capital_O += two_horiz(offset + a_wk) + two_horiz(offset + a_wk + 4*a_day)
        capital_O = set(capital_O)
        capital_O = list(capital_O)
        return capital_O

    dates =  capital_H(topLeft) + capital_E(topLeft) + capital_L(topLeft) + capital_L2(topLeft) +capital_O(topLeft)

    return dates


def color(dates):
    for date in dates:
        for x in range(random.randint(12,22)):
            addCommit(date)
    cleanUpPush()

color(datesToColor(topLeft()))
