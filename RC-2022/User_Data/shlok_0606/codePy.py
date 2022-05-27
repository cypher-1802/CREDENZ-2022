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

#Senior D
s="3.1415926535 8979323846 2643383279 5028841971 6939937510 5820974944 5923078164 0628620899 8628034825 3421170679 8214808651 3282306647 0938446095 5058223172 5359408128 4811174502 8410270193 8521105559 6446229489 5493038196 4428810975 6659334461 2847564823 3786783165 2712019091 4564856692 3460348610 4543266482 1339360726 0249141273 7245870066 0631558817 4881520920 9628292540 9171536436 7892590360 0113305305 4882046652 1384146951 9415116094 3305727036 5759591953 0921861173 8193261179 3105118548 0744623799 6274956735 1885752724 8912279381 8301194912 9833673362 4406566430 8602139494 6395224737 1907021798 6094370277 0539217176 2931767523 8467481846 7669405132 0005681271 4526356082 7785771342 7577896091 7363717872 1468440901 2249534301 4654958537 1050792279 6892589235 4201995611 2129021960 8640344181 5981362977 4771309960 5187072113 4999999837 2978049951 0597317328 1609631859 5024459455 3469083026 4252230825 3344685035 2619311881 7101000313 7838752886 5875332083 8142061717 7669147303 5982534904 2875546873 1159562863 8823537875 9375195778 1857780532 1712268066 1300192787 6611195909 2164201989 "
lst=[1,2,4,8,16,32,64,128,256,512,1024]
big_string=""
for i in s:
    if(i.isdigit()):
        big_string+=i
n=input()
if(n.isdigit()):
    n=int(n)
    if(n>=1 and n<=1000):
        print(lst[int(big_string[n-1])])
    else:
        print("Number Out of Range")
else:
    print("Invalid input")