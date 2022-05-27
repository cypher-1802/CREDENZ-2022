import sys
from pyseccomp import *


def seccomp_filter():
    f = SyscallFilter(defaction=KILL)
    
    f.add_rule(ALLOW, "read", Arg(0, EQ, sys.stdin.fileno()))
    f.add_rule(ALLOW, "write", Arg(0, EQ, sys.stdout.fileno()))
    f.add_rule(ALLOW, "write", Arg(0, EQ, sys.stderr.fileno()))
    f.add_rule(ALLOW, "fstat")   #obtain information about an open file
    f.add_rule(ALLOW, 'ioctl')   #input output system call
    f.add_rule(ALLOW, "exit_group")  #termiates all thread
    f.add_rule(ALLOW, "exit")    #terminates calling thread
    f.add_rule(ALLOW, "read")
    f.add_rule(ALLOW, "open")
    f.add_rule(ALLOW, "openat")   #open a file relative to a directory file descriptor 
    f.add_rule(ALLOW, "lseek")   #changes the positions of the read/write pointer within the file
    f.add_rule(ALLOW, "close")
    f.add_rule(ALLOW, "mmap")    #map files or devices into memory
    f.add_rule(ALLOW, "mprotect")    #set protection on a region of memory
    f.add_rule(ALLOW, "sigaltstack") #set and/or get signal stack context
    f.add_rule(ALLOW, "rt_sigaction")
    f.add_rule(ALLOW, "sigreturn")   #return from signal handler
    f.add_rule(ALLOW, "execve")  #execute program
    f.add_rule(ALLOW, "execveat")    #execute program relative to a directory file descriptor
    f.add_rule(ALLOW, "fcntl")
    # f.add_rule(ALLOW, "futex")
    # f.add_rule(ALLOW, "lstat") # Upon successful completion, lstat() shall return 0. Otherwise, it shall return -1 and set errno to indicate the error.

    f.add_rule(ALLOW, "brk") #change size of data segment
    f.add_rule(ALLOW, "munmap")  #unmap files or devices into memory
    f.add_rule(ALLOW, "access")  #determines whether the calling process has access permission to a file

    f.load()
    

seccomp_filter()

#xor of i, i+1, i+2 prime nos
#senior F
def SieveOfEratosthenes(n):
    prime = [True for i in range(n + 1)]
    p = 2
    while (p * p <= n):
        if (prime[p] == True):
            for i in range(p ** 2, n + 1, p):
                prime[i] = False
        p += 1
    prime[0] = False
    prime[1] = False

    nums = []
    for i in range(n):
        if(prime[i]):
            nums.append(i)
    return nums


prime_no = SieveOfEratosthenes(8000)

seq = []

for i in range(1005):
    seq.append(prime_no[i] ^ prime_no[i+1] ^ prime_no[i+2])

n = input()
if(n.isdigit()):
    n=int(n)
    if(n>=1 and n<=1000):
        print(seq[n-1])
    else:
        print("Number Out of Range")
else:
    print("Invalid input")