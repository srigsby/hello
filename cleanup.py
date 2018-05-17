# import subprocess, random, time
# from datetime import datetime, timedelta
import hello

# def addCommit(timestamp, commit_msg=None):
#     nonce = random.randrange(16**10)
#     touch = "touch " + str(nonce)
#     add = "git add ."
#     if commit_msg != None:
#         commit = 'git commit --date={0} -m {1}'.format(timestamp, commit_msg)
#     else:
#         commit = 'git commit --date={0} -m {0}'.format(timestamp)
#     # push = "git push"
#     run = [touch, add, commit]
#     for cmd in run:
#         subprocess.Popen(cmd.split())
#         time.sleep(2)


hello.subprocess.run(['rm', '[1-9]*'])
hello.subprocess.run(['git', 'add', '-u'])
hello.addCommit(int(hello.datetime.now().timestamp()), 'hello')
hello.subprocess.run(['git', 'push'])