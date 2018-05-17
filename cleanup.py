import hello

hello.subprocess.run(['rm', '[1-9]*'])
hello.subprocess.run(['git', 'add', '-u'])
hello.addCommit(int(hello.datetime.now().timestamp()), 'hello')
hello.subprocess.run(['git', 'push'])