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

#n + nth pi's digit + nth e's digit
e="2.71828 18284 59045 23536 02874 71352 66249 77572 47093 69995 95749 66967 62772 40766 30353 54759 45713 82178 52516 64274 27466 39193 20030 59921 81741 35966 29043 57290 03342 95260 59563 07381 32328 62794 34907 63233 82988 07531 95251 01901 15738 34187 93070 21540 89149 93488 41675 09244 76146 06680 82264 80016 84774 11853 74234 54424 37107 53907 77449 92069 55170 27618 38606 26133 13845 83000 75204 49338 26560 29760 67371 13200 70932 87091 27443 74704 72306 96977 20931 01416 92836 81902 55151 08657 46377 21112 52389 78442 50569 53696 77078 54499 69967 94686 44549 05987 93163 68892 30098 79312 77361 78215 42499 92295 76351 48220 82698 95193 66803 31825 28869 39849 64651 05820 93923 98294 88793 32036 25094 43117 30123 81970 68416 14039 70198 37679 32068 32823 76464 80429 53118 02328 78250 98194 55815 30175 67173 61332 06981 12509 96181 88159 30416 90351 59888 85193 45807 27386 67385 89422 87922 84998 92086 80582 57492 79610 48419 84443 63463 24496 84875 60233 62482 70419 78623 20900 21609 90235 30436 99418 49146 31409 34317 38143 64054 62531 52096 18369 08887 07016 76839 64243 78140 59271 45635 49061 30310 72085 10383 75051 01157 47704 17189 86106 87396 96552 12671 54688 95703 50354 02123"
s="3.1415926535 8979323846 2643383279 5028841971 6939937510 5820974944 5923078164 0628620899 8628034825 3421170679 8214808651 3282306647 0938446095 5058223172 5359408128 4811174502 8410270193 8521105559 6446229489 5493038196 4428810975 6659334461 2847564823 3786783165 2712019091 4564856692 3460348610 4543266482 1339360726 0249141273 7245870066 0631558817 4881520920 9628292540 9171536436 7892590360 0113305305 4882046652 1384146951 9415116094 3305727036 5759591953 0921861173 8193261179 3105118548 0744623799 6274956735 1885752724 8912279381 8301194912 9833673362 4406566430 8602139494 6395224737 1907021798 6094370277 0539217176 2931767523 8467481846 7669405132 0005681271 4526356082 7785771342 7577896091 7363717872 1468440901 2249534301 4654958537 1050792279 6892589235 4201995611 2129021960 8640344181 5981362977 4771309960 5187072113 4999999837 2978049951 0597317328 1609631859 5024459455 3469083026 4252230825 3344685035 2619311881 7101000313 7838752886 5875332083 8142061717 7669147303 5982534904 2875546873 1159562863 8823537875 9375195778 1857780532 1712268066 1300192787 6611195909 2164201989 "

#question Senior E
new_e = ""

for i in e:
    if i.isdigit():
        new_e += i

new_pi = ""

for i in s:
    if i.isdigit():
        new_pi += i

seq = []

for i in range(1, 1001):
    seq.append(i + int(new_e[i-1]) + int(new_pi[i-1]))

n=input()
if n.isdigit():
    n=int(n)
    if(n>=1 and n<=1000):
        print(seq[n-1])
    else:
        print("Number Out of Range")
else:
    print("Invalid input")