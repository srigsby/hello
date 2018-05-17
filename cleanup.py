import subprocess, random, time
from datetime import datetime, timedelta

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


subprocess.run(['rm', '[1-9]*'])
subprocess.run(['git', 'add', '-u'])
addCommit(int(datetime.now().timestamp()))
subprocess.run(['git', 'push'])