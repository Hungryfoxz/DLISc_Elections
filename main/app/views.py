from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from .models import Register, Voted, Candidate, Positions
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.decorators import login_required
import random

voting_status = False
result_status = False
print(voting_status)
print(result_status)

# ! =======================================================================================================================
@login_required
def voting_status(request):
    if request.method == "GET":
        global voting_status
        voting_status = not voting_status
        if voting_status == True:
            return HttpResponse('ON')
        else:
            return HttpResponse('OFF')

@login_required
def voting_status_updates(request):
    if request.method == "GET":
        global voting_status 
        if voting_status == True:
            return HttpResponse('ON')
        else:
            return HttpResponse('OFF')


#! ===================== Result Updates ================== 
@login_required
def result_status(request):
    if request.method == "GET":
        global result_status
        result_status = not result_status
        if result_status == True:
            return HttpResponse('Show')
        else:
            return HttpResponse('Hide')

@login_required
def result_status_updates(request):
    if request.method == "GET":
        global result_status 
        if result_status == True:
            return HttpResponse('Show')
        else:
            return HttpResponse('Hide')


# ! =======================================================================================================================
def index(request):
    return render(request, 'index.html')


# ! =======================================================================================================================
@csrf_protect
def register(request):
    if request.method == "POST":
        email = request.POST.get('email')
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        roll_no = request.POST.get('roll_no')
        #checking user inputs..
        if (email == "" or name == "" or phone == "" or roll_no == "" ):
            return HttpResponse('<p>All fields are not filled properly.</p>')
        else:
        #creating the object..<registration>..
            if Register.objects.filter(email=email).exists():
                return HttpResponse('<p>Already registered.</p>')
            else:
                # try:
                #     validate_email(email)
                # except ValidationError as e:
                #     return HttpResponse('<p>Use a verified email.</p>')
                # else:
                registration = Register(email=email, phone=phone, name=name, roll_no=roll_no, otp=random.randint(1111,9999))
                registration.save()
                return HttpResponse('<p>Successfully registered.</p>')
    
    return render(request, 'index.html')



# ! ======================================================================================================================
def vote(request):

    def is_present(userEmail):
        if Register.objects.filter(email=userEmail).exists():
            # Then check if it also exits in the volted students table..
            if Voted.objects.filter(email=userEmail).exists():
                # if it is present in the list of Voted students ie models.Logged 
                # then return error message "You have already voted..."
                return 0
                # return zero means that the user has alredy voted
            else:
                '''got the email to the object...already..
                 now creating the instance...of the retrieved object 
                 and linking it to the database with the model.Logged(email=userEmail)
                 email_instance = Logged(email=userEmail)
                 save this instance...
                 email_instance.save()'''
                if Register.objects.filter(phone=userPassword).exists():
                    return 1
                else:
                    return 3
                # return 1 suggests that user has not voted yet...

        else:
            return 2
            # return 2 => that the userEmail is not found in the database..ie he is not registered..
            



    #_Getting the requst as POST from the form...
    if request.method == "POST" :
        userEmail = request.POST.get('email')
        userPassword = request.POST.get('phone')

        if voting_status == False:
            messages.warning(request, 'Voting is not available !!!' )
            return redirect(vote) 

        else:
        #check the input string for the userEmail..
            if( userEmail != ''):
                check = is_present(userEmail)
                if(check == 0):
                    messages.warning(request, 'Looks like you have already voted once !!!' )
                    return redirect(index)
                
                elif(check == 1):              
                    for position in Positions.objects.only('name'):
                                                                # it will check for the position in the Positions table..
                        choices = request.POST.get(str(position))
                                                                # this will get the id of the selected person from the request..
                        if Candidate.objects.filter(pk=choices).exists():
                            instance = Candidate.objects.get(pk=choices)
                                                                # this statement will create an instance to the primary key related to the candidate
                            instance.votes += 1
                                                                # this statement will add a vote the instance linking to that particular name...
                            instance.save()
                            # this will finally save the vote to the database for the respected field..
                        else:
                            continue
                    stu_data = Register.objects.get(email=userEmail)
                    print(stu_data)
                    voter_data = Voted(email=userEmail,details=stu_data)
                    voter_data.save()
                    messages.success(request, 'Your response has been saved successfully...')
                    return redirect(index)

                else:
                    # for 2 and 3 ::
                    messages.warning(request, 'Unable to find your email in the Database !!!')
                    return redirect(vote)    
            else:
                messages.warning(request, '*You have not entered you email correctly. Please try to submit again with your e-mail.')
                return redirect(vote)


    #_rendering this data as template....to the html from the models models.Candidate and models.Position..
    candidates = Candidate.objects.all()
    position = Positions.objects.all().order_by('priority')
    return render(request, 'vote.html',{'candidates': candidates,'positions':position})


# ! ====================================================================================================================
def result(request):
    global result_status
    if result_status == True:
        print(result_status)
        candidates = Candidate.objects.all()
        positions = Positions.objects.all().order_by('priority')
        total_votes = Voted.objects.count()
        # ? === Progress bar Calculation...
        return render(request, 'result.html', {'candidates': candidates,'positions':positions, 'voted': total_votes })
    else:
        return render(request, './components/waiting.html')


# ! ====================================================================================================================
def update(request):
    candidates = Candidate.objects.all()
    positions = Positions.objects.all().order_by('priority')
    total_votes = Voted.objects.count()
    messages.success(request, 'Your response has been saved successfully...')
    return render(request, './components/results.html', {'candidates': candidates,'positions':positions, 'voted': total_votes })



# ! ===================================================================================================================
'''def email(request):
    print("Email")
    userEmail = request.POST.get('email')

    if userEmail !='':
        if Register.objects.filter(email=userEmail).exists():
            if Voted.objects.filter(email=userEmail).exists():
                return HttpResponse('<p>You have already voted once.</p>')
            else:
                instance = Register.objects.get(email=userEmail)
                print(instance)
                send_mail(
                    'Email Verification OTP',
                    f'Your OTP for email verification is : {instance.otp}',
                    settings.EMAIL_HOST_USER,
                    [email],
                    fail_silently = False,
                )
                return HttpResponse('<p>OTP sent to email successfully.</p>')
        else:
            return HttpResponse('<p>Email not found</p>')

    print(userEmail)
    return HttpResponse('<p>Enter a valid email.</p>')'''


# ! ===================================================================================================================
'''def verify(request):
    print("Verified")
    pass'''


