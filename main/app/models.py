from django.db import models

# Create your models here.
#Model for the Feedback of the people..
class Register(models.Model):
    email = models.CharField(max_length=40)
    name = models.CharField(max_length=60)
    phone = models.CharField(max_length=10)
    roll_no = models.CharField(max_length=5)
    otp = models.IntegerField(null=True, blank=True )

    def __str__(self):
        return 'Roll No : {} | Name : {} | OTP : {}'.format(self.roll_no, self.name, self.otp)
    
    class Meta:
        verbose_name_plural = "Registration"


                                                                                                             # VOTED 
#[++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++]
#Checking who have voted..
class Voted(models.Model):
    email = models.CharField(max_length=60)
    details = models.ForeignKey(Register, on_delete=models.CASCADE)

    def __str__(self):
        return 'Email : {} | Details : {} '.format(self.email, self.details)

    class Meta:
        verbose_name_plural = "Voted Student List"
                                                                                                             # POSITIONS 
#[++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++]

#creating the positions table..
class Positions(models.Model):
    name = models.CharField(max_length=80)
    priority = models.IntegerField(unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Voter Position List"

                                                                                                            # CANDIDATE
#[+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++]
#creating the candidates table....
class Candidate(models.Model):
    name = models.CharField(max_length=80)
    bio = models.TextField(max_length=300)
    position = models.ForeignKey(Positions, on_delete=models.CASCADE)
    votes = models.IntegerField(default=0)
    image = models.ImageField(upload_to ='static/profiles/', height_field=None, width_field=None,default="static/profiles/default.png",null=True, blank=True)

    def __str__(self):
        return 'Name : {} | Postion : {} | Votes : {}'.format(self.name,self.position,self.votes)

    class Meta:
        verbose_name_plural = "Candidate List"