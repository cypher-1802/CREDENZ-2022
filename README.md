# Credenz
This is a website built in Django for round 2 of an event called **"Reverse Coding"** for the annual tech fest of PISB called Credenz. 

The event has the following format:

    i) Participant is given a set of questions according to the criteria whether he or she is a junior or senior. 
    
    ii) Each question has an input box and an output box. The participant has to provide a single input based on the instructions given just above these boxes and press run.
       
       Doing so will provide an output for the given input, which the participant has to use to figure out the problem statement.
       
    iii) Once the participant has figured out the problem statement, he or she has to code it, and run the code in editor provided in the website.
    
    iv) The participant will be redirected to the submission page where the result of his/her submission will be displayed. 
    
    v) The participant can view the leaderboard which is updated after every submission. 
    
To setup the website first clone this branch on your local linux device and then create a environment and follow the following commands on your terminal:
- source [environment name]/bin/activate
- pip3 install -r requirements.txt
After the requirements have been setup, run the following commands on your terminal:
- cd RC-2022
- sudo bash seccomp.sh 
- cd .. 
Make sure to run this commands in virtual environment previously created.
Running seccomp.sh will setup libseccomp in your environment, this is neccesary for sandboxing ( blocking requests that affect the server while running code of a user ).


To run the local server, run the following commands on your terminal:
- cd RC-2022
- python3 manage.py createsuperuser
Follow the instructions that appear on the terminal to create a superuser and get admin access.
- python3 manage.py runserver

Go to the local host link provided in the terminal, and type /san_saf at the end of the url.
Use your superuser account created before to login into admin. Click on set_time, and set start time and end time. After saving, reload the server
and go back to the local host link (before adding the san_saf part) and login through your superuser credentials.
