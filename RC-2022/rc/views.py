import os
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import *
from django.contrib.auth.decorators import login_required
from rc.decorators import timer
from sandbox import views
from django.db.models import Q
from datetime import datetime
import re
from django.http import JsonResponse
from django.core.paginator import Paginator

signals = {
    1: "CTE",
    2: "CTE",
    127: "CTE",
    132: "RE",
    133: "RE",
    134: "RE",
    136: "RE",
    137: "TLE",
    138: "MLE",
    139: "RE",
    158: "TLE",
    152: "TLE",
    159: "MLE",
    153: "MLE",
}
def handler404(request,*args):
    return redirect('rc-home')
def handler403(request,*args):
    return render(request,"rick.html")
@login_required
@timer
def home(request):
    obj = SetTime.objects.get(pk=1) #for timer copy these 3 lines
    time = obj.final_time   #for timer copy these 3 lines
    mytime = str(time)  #for timer copy these 3 lines
    return render(request, "Rc-Home.html",{"time":mytime})  ##for timer give mytimer in all pages otherwise only those pages will show correct timer which have above 3 lines included


# def leaderboard(request):
#     if request.user.is_authenticated:
#         data = []
#         for user in RcPlayer.objects.order_by("-total_score"):
#             data.append(user)
#         return render(request, "Rc-leaderboard.html", {"data": data})
@login_required
@timer
def leaderboard(request):
    tester = RcPlayer.objects.get(user=request.user)
    if request.user.is_authenticated:
        data = []
        rank=0
        counter=0
        for user in RcPlayer.objects.filter(junior=tester.junior).order_by("-total_score", "time"):
            data.append(user)
            rank+=1
            if(user==tester):
                counter=rank
                mydata=data
        p=Paginator(mydata,10) #here change (mydata,2) to (mydata,10) to see list of 10 leaders 
        page_num=request.GET.get('page',1)
        
        try:
            page=p.page(page_num)
        except EmptyPage:
            page = p.page(1)
        obj = SetTime.objects.get(pk=1) #for timer copy these 3 lines
        time = obj.final_time   #for timer copy these 3 lines
        mytime = str(time)  #for timer copy these 3 lines            
        percent = round(tester.total_score/6, 2)
        return render(request, "Rc-leaderboard.html", {"data": data,"rank":counter,"name":tester.user.username,"percent":percent, "score":tester.total_score,"items":page, "num":p,"time":mytime})

    return JsonResponse({'key':s,'lang':lang},status=200)

@login_required
@timer
def contest(request):
    tester = RcPlayer.objects.get(user=request.user)
    ques = RcQuestion.objects.filter(Q(junior=tester.junior) | Q(junior=None))
    l_status = []
    for que in ques:
        status = RcSubmission.objects.filter(q_id=que, p_id=tester)
        if len(status) > 0:
            status = status.order_by("-score")
            status = status[0].status
            l_status.append(status)
        else:
            status = "Not Attempted"
            l_status.append(status)
    mylist = zip(ques, l_status)
    obj = SetTime.objects.get(pk=1) #for timer copy these 3 lines
    time = obj.final_time   #for timer copy these 3 lines
    mytime = str(time)  #for timer copy these 3 lines
    return render(request, "Rc-contest.html", {"mylist": mylist,"time":mytime})


@login_required
@timer
def question(request, pk):
    ques = RcQuestion.objects.get(pk=pk)
    tester = RcPlayer.objects.get(user=request.user)
    obj = SetTime.objects.get(pk=1) #for timer copy these 3 lines
    time = obj.final_time   #for timer copy these 3 lines
    mytime = str(time)  #for timer copy these 3 lines  
    return render(request, "Rc-question.html", {"ques": ques,"score": tester.total_score,"time":mytime})

@login_required
@timer
def mysubmission(request, pk):
    l1 = []
    for i in RcSubmission.objects.all().filter(
        p_id=RcPlayer.objects.get(user=request.user), q_id=pk
    ).order_by("-time"):
        l1.append(i)
    tester=RcPlayer.objects.get(user=request.user)
    obj = SetTime.objects.get(pk=1) #for timer copy these 3 lines
    time = obj.final_time   #for timer copy these 3 lines
    mytime = str(time)  #for timer copy these 3 lines  
    dummy=pk
    bool=True
    if(tester.junior==False):
        dummy-=2
        bool=False
    return render(request, "Rc-mysub.html", {"data": [l1,dummy],"bool":bool,"time":mytime})


def get_upload_path(instance):
    return "User_Data/{0}".format(instance)


@login_required
@timer
def RC(request, pk):
    que = RcQuestion.objects.get(pk=pk)
    tester = RcPlayer.objects.get(user=request.user)
    # if request.method == "POST":
    if que.junior == tester.junior or que.junior == None:
        intake = request.POST["Rc_input"]
        result = ""
        s = "User_Data/{0}/Rc_input.txt".format(tester.user.username)
        with open(s, "w+") as inp:
            inp.write(intake)
        with open(s, "r") as inp:
            views.get_code(que.code, request.user.username, que.language)
            views.execute(request.user.username, inp, que.language,1,100000000)
            f2 = open(
                "sandbox/submissions/{}/result.txt".format(tester.user.username),
                "r",
            )
            result = f2.read()
            f2.close()
        return JsonResponse({"output":result},status=200)
    else:
        return redirect("rc-contest")
    # else:
        # return render(request, "Rc-question.html", {"ques": que})

@login_required
@timer
def buffer(request,pk):
    print("buff")
    l1 = []
    lang=""
    for i in RcSubmission.objects.filter(p_id=RcPlayer.objects.get(user=request.user), q_id=pk).order_by("-time"):
        l1.append(i)
        break
    if(len(l1)==0):
        s=""
    else:
        s=l1[0].code
        lang=l1[0].language
    return JsonResponse({'key':s,'lang':lang},status=200)

def san_saf_error(error,language):

    if language == "py":
        try:
            pattern = re.sub(r'(["])([a-zA-Z0-9_.+-;,]+)(["])','"prog.py"',error)
            find = re.compile(r'line [\d]+')
            num = str(int(((find.findall(pattern))[0].split())[1]) - 39)
            error = re.sub(find,"line "+num, pattern)
        except:
            pass
    elif language=="cpp":
        try:
            error = re.sub(r'U([a-zA-Z0-9_.+-;,]+)([:])','prog.cpp:',error)
        except:
            pass
    else:
        try:
            error = re.sub(r'U([a-zA-Z0-9_.+-;,]+)([:])','prog.c:',error)
        except:
            pass

    return error


@login_required
@timer
def rc_sub(request, pk):
    que = RcQuestion.objects.get(pk=pk)
    tester = RcPlayer.objects.get(user=request.user)
    tc_count = 0
    correct_tcs = 0
    code = ""
    language = request.POST.get("language")
    s = ""
    if request.method == "POST":
        if que.junior == tester.junior or que.junior == None:
            code = request.POST["input"]
            views.get_code(code, request.user.username, language)
            cases = []
            check = True
            display_error = ""
            for tc in Rctestcase.objects.filter(q_id=pk):
                tc_count += 1
                error_code = views.execute(request.user.username, tc.tc_input, language,que.time_limt,que.memory_limit)
                print(error_code)
                if error_code == 0:
                    stat = views.compare(request.user.username, tc.tc_output)
                    if stat:
                        cases.append("Passed")
                        correct_tcs += 1
                    else:
                        cases.append("Failed")
                else:
                    try:
                        if(error_code<0):
                            error_code=128-error_code
                        cases.append(signals[error_code])
                    except:
                        cases.append("Unknown Error")
                    if check:
                        display_error = cases[-1]
                        check = False
            scr = int((100 * correct_tcs) / tc_count)
            if(tester.junior==False):
                pk-=2
            update_bool=views.update_score(scr, pk, tester)
            if(tester.junior == False and update_bool == False and scr < 100):
                scr = 0
            if correct_tcs == tc_count:
                intake = RcSubmission(
                    q_id=que,
                    p_id=tester,
                    score=scr,
                    code=code,
                    status="AC",
                    language=language,
                )
                que.correct_submissions += 1
            elif error_code == 0:
                intake = RcSubmission(
                    q_id=que,
                    p_id=tester,
                    score=scr,
                    code=code,
                    status="WA",
                    language=language,
                )
            else:
                intake = RcSubmission(
                    q_id=que,
                    p_id=tester,
                    score=scr,
                    code=code,
                    status=display_error,
                    language=language,
                )
            intake.save()
            if(update_bool == 0):
                que.total_submissions += 1
                dec = (que.correct_submissions / que.total_submissions) * 100
                que.accuracy = round(dec, 2)
                que.save()
            f2 = open("sandbox/submissions/{}/error.txt".format(tester.user.username), "r")
            errors = f2.read()
            errors = san_saf_error(errors, language)        
            f2.close()

            obj = SetTime.objects.get(pk=1) #for timer copy these 3 lines
            time = obj.final_time   #for timer copy these 3 lines
            mytime = str(time)  #for timer copy these 3 lines  
            if(display_error == ""):
                display_error = "Wrong Answer"
            if correct_tcs == tc_count:
                return render(
                    request,
                    "Rc-submission.html",
                    {"result": "All Correct", "testcase": cases,"score":scr,"pk":pk,"time":mytime},
                )
            return render(
                request,
                "Rc-submission.html",
                {"result":display_error , "testcase": cases, "error": errors,"score":scr,"pk":pk,"time":mytime},
            )
        return redirect("rc-contest")

    obj = SetTime.objects.get(pk=1) #for timer copy these 3 lines
    time = obj.final_time   #for timer copy these 3 lines
    mytime = str(time)  #for timer copy these 3 lines      
    return render(request, "Rc-question.html", {"ques": que,"time":mytime})

def login_page(request):

    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            try:
                nw = RcPlayer(junior=True, user=user)
                nw.save()
            except:
                pass
            login(request, user)
            path = get_upload_path(username)
            try:
                os.mkdir(path)
            except:
                pass
            try:
                os.mkdir('sandbox/submissions/{0}'.format(username))
            except:
                pass
            
            obj = SetTime.objects.get(pk=1)
            a = obj.start_time.astimezone()  # to get current timezone time.
            # final time should be constant
            start_time = datetime(
                year=a.year,
                month=a.month,
                day=a.day,
                hour=a.hour,
                minute=a.minute,
                second=a.second,
            )  # final time
            # seconds from epoch.
            start_time_timestamp = int(start_time.timestamp())
            date_now = datetime.today()
            date_now_timestamp = int(date_now.timestamp())
            time = obj.start_time.astimezone()  # time = obj.start_time #start time format 2022-02-08 18:30:19+05
            newtime = str(time)
            if date_now_timestamp >= start_time_timestamp:
                return redirect("rc-home")
            
            return render(request, "waiting.html",{"time":newtime})
        messages.error(request, "Invalid Credentials")
        return render(request, "login.html", {"error": "invalid username"})

    return render(request, "login.html")

@login_required
def logout_view(request):
    tester = RcPlayer.objects.get(user=request.user)
    data = []
    count = 0
    rank=0

    for user in RcPlayer.objects.filter(junior=tester.junior).order_by("-total_score", "time"):
        count += 1
        if count < 7:
            data.append(user)
        if(tester==user):
            rank=count
        if(rank>0 and count>5):
            break

    first=data.pop(0)
    second=data.pop(0)
    third=data.pop(0)
    attempted=0
    solved=0

    if(len(RcSubmission.objects.filter(p_id=RcPlayer.objects.get(user=request.user), q_id=1))):
        attempted+=1
        if(tester.ques1==100):
            solved+=1
    if(len(RcSubmission.objects.filter(p_id=RcPlayer.objects.get(user=request.user), q_id=2))):
        attempted+=1
        if(tester.ques2==100):
            solved+=1
    if(len(RcSubmission.objects.filter(p_id=RcPlayer.objects.get(user=request.user), q_id=3))):
        attempted+=1
        if(tester.ques3==100):
            solved+=1
    if(len(RcSubmission.objects.filter(p_id=RcPlayer.objects.get(user=request.user), q_id=4))):
        attempted+=1
        if(tester.ques4==100):
            solved+=1
    if(len(RcSubmission.objects.filter(p_id=RcPlayer.objects.get(user=request.user), q_id=5))):
        attempted+=1
        if(tester.ques5==100):
            solved+=1
    if(len(RcSubmission.objects.filter(p_id=RcPlayer.objects.get(user=request.user), q_id=6))):
        attempted+=1
        if(tester.ques6==100):
            solved+=1

    logout(request)
    return render(request, "result.html", {"first":first,"second":second,"third":third,"leaders": data,"rank":rank,"tester":tester,"attempt":attempted,"solved":solved})


# @login_required
# def logout_view(request):
#     logout(request)
#     data = []
#     count = 0
#     for user in RcPlayer.objects.order_by("-total_score"):
#         if count < 3:
#             data.append(user)
#             count += 1
#         else:
#             break
#     return render(request, "result.html", {"leaders": data})
