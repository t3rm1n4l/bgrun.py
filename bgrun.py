#!/usr/bin/env python

import os
import fcntl,sys

def bgrun(command):
    """
    Execute a command [arglist] and send it to the background
    Returns pid
    """
    pipe = os.pipe()
    pid = os.fork()
    if pid:
        os.close(pipe[1])
        fd = os.fdopen(pipe[0])
        pid = fd.read(10)
        os.wait()
        return pid
    else:
        pid2 = os.fork()

        if pid2:
            os.close(pipe[0])
            fd = os.fdopen(pipe[1],'w')
            fd.write("%-10d" %pid2)
            fd.flush()
            fd.close()
            os._exit(0)
        else:
            os.execvp(command[0], command)

if __name__ == "__main__":
    print "pid is", bgrun(["./test.sh"])
