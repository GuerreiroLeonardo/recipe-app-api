from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


class UserManager(BaseUserManager):

    def create_user(self,email,password= None, **extra_fields):  #password = none possibility to create a user that is inactive
                                                                #**extra_fields - take any of the extra func that are passed in and pass it
                                                                # into extra_fields, everytime we add new fields to our user we can add ad hock
                                                                # as we add them to our model.
        '''creates and saves a new user'''
        if not email:
            raise ValueError('Users must have an email address')
        user = self.model(email=self.normalize_email(email),**extra_fields) #we can access the model that the manager is for just typing self.model
        user.set_password(password)
        user.save(using=self._db) #made to support multiple databases
        
        return user

    def create_superuser(self, email, password):
        '''creates and saves a new superuser'''
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user

class User(AbstractBaseUser, PermissionsMixin):
    '''custom user model that supports using email instead of username'''
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'