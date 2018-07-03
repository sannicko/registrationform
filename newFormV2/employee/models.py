from django.db import models
from users.models import *
from django.utils.translation import ugettext_lazy as _
from django.core.validators import RegexValidator
class Employee(models.Model):
	
	# friend = models.ForeignKey(ApplicationUser,related_name="friendship_set",Blank=True)
	# current_user = models.ForeignKey(ApplicationUser, related_name="owner", Blank=True)
	# is_activeFriend = models.BooleanField(_('active'), default=True, help_text=_('Whether friend is Active Or Not'))
	
	Martial_status = (
		('M', 'Married'),
		('S', 'Single'),
	)

	BOOL_CHOICES = (('y', 'Yes'), ('N', 'No'))

	first_name =  models.CharField(null=True,max_length=500)
	last_name =  models.CharField(null=True,max_length=500)
	email_address = models.CharField(null=True,blank = True,max_length=200)
	Martial_status = models.CharField(max_length=1, choices=Martial_status, null=True)

	home_address1 = models.CharField(null=True,max_length=1000)
	home_address2 = models.CharField(null=True,max_length=1000)

	city =  models.CharField(null=True,max_length=100)
	state =  models.CharField(null=True,max_length=100)

	form_date = models.DateField(null=True,max_length=100,blank = True)
	
	dateOFBirth = models.DateField(null=True,max_length=100,blank = True)
	#phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
	
	phoneNumber = models.CharField(max_length=17, blank=True,null=True)
	socialSecurityNumber = models.CharField(max_length=70, blank=True)

	no_year_experience = models.IntegerField(max_length=20, blank=True,null=True)
	emergency_contact_firstName = models.CharField(null=True,max_length=500)
	emergency_contact_lastName = models.CharField(null=True,max_length=500)
	emergency_contact_phoneNumber = models.CharField(max_length=17, blank=True,null=True)
	emergency_contact_relation  = models.CharField(max_length=17, blank=True,null=True)

	ceiling_mechanic  = models.BooleanField(default=False)
	framing_mechanic = models.BooleanField(default=False)
	drywall_hanger = models.BooleanField(default=False)
	drywall_finisher = models.BooleanField(default=False)
	general_larborer = models.BooleanField(default=False)
	painter_tradesman = models.BooleanField(default=False)
	plaster_tradesman =  models.BooleanField(default=False)

	masonry_bricklayer = models.BooleanField(default=False)
	masonry_blocklayer = models.BooleanField(default=False)
	carpenter = models.BooleanField(default=False)
	concrete_forming = models.BooleanField(default=False)
	concrete_finisher = models.BooleanField(default=False)
	osha_manager = models.BooleanField(default = False)
	project_manager = models.BooleanField(default = False)

	#experience 
	is_ladder_user = models.BooleanField(default=False)
	is_wheelbrrow_user = models.BooleanField(default=False)
	is_general_hand_tools = models.BooleanField(default=False)
	is_walking_slits = models.BooleanField(default=False)
	is_electric_screw_gun = models.BooleanField(default=False)
	is_electric_chop_saw = models.BooleanField(default=False)
	is_power_nail_gun =  models.BooleanField(default=False)
	is_wallboard_hoist = models.BooleanField(default=False)
	is_scissor_lift = models.BooleanField(default=False)
	is_boom_lift = models.BooleanField(default=False)
	is_bucket_truck_lift = models.BooleanField(default=False)
	is_new_skill = models.BooleanField(default=False)

	is_osha10 = models.BooleanField(default=False)
	is_osha30 = models.BooleanField(default=False)
	is_osha_training_manager= models.BooleanField(default=False)
	is_power_tool_certified = models.BooleanField(default=False)
	is_hiltl = models.BooleanField(default=False)
	is_ladder_user_certified = models.BooleanField(default=False)
	is_scissor_lift_certified = models.BooleanField(default=False)
	is_broom_lift_certified = models.BooleanField(default=False)
	convicted_or_not = models.CharField(max_length=1, choices=BOOL_CHOICES,blank=False,default='N')
	allowed_in_usa = models.CharField(max_length=1, choices=BOOL_CHOICES,blank=False,default='N')


	created = models.DateTimeField(auto_now_add=True, editable=False)
	
	def __str__(self):
		return str(self.first_name)