# Create your models here.
from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)


class MyUserManager(BaseUserManager):
    def create_user(self, email, date_of_birth, user_name, password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            date_of_birth=date_of_birth,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, date_of_birth, password):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            email,
            password=password,
            date_of_birth=date_of_birth,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user
class Message(models.Model):
    title = models.CharField(max_length=50, blank=True, null=False)
    content = models.TextField(blank=False)
    created_date = models.DateField(auto_now_add=True, null=False)
    senderUser = models.CharField(max_length=50, blank=True, null=False)
    receiveUser = models.CharField(max_length=50, blank=True, null=False)

class MyUser(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    date_of_birth = models.DateField()
    user_name = models.CharField(max_length=50, blank=False, null=False, default="")
    is_authority = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    userImg = models.ImageField(upload_to = 'test/%m/%d', default = 'test/None/no-img.jpg')

    objects = MyUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['date_of_birth']

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin

class UnknownBoard(models.Model):
    title = models.CharField(max_length=50, blank=True, null=False)
    makerUser = models.CharField(max_length=50, blank=True, null=False)
    password = models.CharField(max_length=50, blank=True, null=False)
    created_date = models.DateField(auto_now_add=True, null=False)
    content = models.TextField(blank=False)
    hit_count = models.IntegerField(default=0)

class UnknowCommnet(models.Model):
    user = models.CharField(max_length=50, blank=True, null=False)
    content = models.CharField(max_length=100, blank=True, null=False)
    created_date = models.DateField(auto_now_add=True, null=False)


class GGulTipBoard(models.Model):
    title = models.CharField(max_length=50, blank=True, null=False)
    user = models.CharField(max_length=50, blank=True, null=False)
    created_date = models.DateField(auto_now_add=True, null=False)
    content = models.TextField(blank=False)
    fileContent = models.FileField(upload_to = 'boardFile/%m/%d', default=None, blank=True, null=True);
    professor = models.CharField(max_length=50, blank=True, null=False)
    hit_count = models.IntegerField(default=0)

class ReportBoard(models.Model):
    title = models.CharField(max_length=50, blank=True, null=False)
    user = models.CharField(max_length=50, blank=True, null=False)
    created_date = models.DateField(auto_now_add=True, null=False)
    content = models.TextField(blank=False)
    fileContent = models.FileField(upload_to = 'boardFile/%m/%d', default=None, blank=True, null=True);
    professor = models.CharField(max_length=50, blank=True, null=False)
    hit_count = models.IntegerField(default=0)
