from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser



# =============
#  Super User
# =============
# This is for creating the super user.  Use Comand Prompt to do this.  Navigate
# to project folder and use "python manage.py createsuperuser".  Follow the
# directions.  This user can use the site and has access to 127.0.0.1:8000/admin.
class MyAccountManager(BaseUserManager):
    def create_user(self,email,first_name,last_name,username,birth_date, password=None):
        if not email:
            raise ValueError("Users must provide a vaild Email")
        if not first_name:
            raise ValueError("Users must provide a first name")
        if not last_name:
            raise ValueError("Users must provide a last name")
        if not username:
            raise ValueError("Users must provide a username")
        if not birth_date:
            raise ValueError("Users must provide a date of birth")

        user = self.model(
                email=self.normalize_email(email),
                first_name=first_name,
                last_name=last_name,
                username=username,
                birth_date=birth_date,
            )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self,email,first_name,last_name,username,birth_date, password=None):
        user = self.create_user(
                email=self.normalize_email(email),
                first_name=first_name,
                last_name=last_name,
                username=username,
                birth_date=birth_date,
                password=password,
            )

        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user



# ==========
#    User
# ==========
# This is for creating a normal user with normal privileges.  This you must have
# forms and templates built and you use the site methods.
class Account(AbstractBaseUser):
    first_name = models.CharField(verbose_name='first name', max_length=50)
    last_name = models.CharField(verbose_name='last name', max_length=50)
    email = models.EmailField(verbose_name='email', max_length=250, unique=True)
    birth_date = models.DateField(verbose_name='birth date', auto_now=False, auto_now_add=False, blank=False)
    user_image = models.ImageField(verbose_name='picture', upload_to='user_img', null=True, blank=True)

    bio = models.TextField(max_length=500, blank=True)
    hobbies = models.CharField(verbose_name='hobbies', max_length=500, blank=True)
    favorite_tv = models.CharField(verbose_name='favorite tv', max_length=500, blank=True)
    favorite_books = models.CharField(verbose_name='favorite books', max_length=500, blank=True)
    work = models.CharField(verbose_name='employment', max_length=500, blank=True)
    schools = models.CharField(verbose_name='studies', max_length=500, blank=True)

    username = models.CharField(max_length=50, unique=True)
    date_joined = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    last_login = models.DateTimeField(verbose_name='last login', auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name','last_name','username','birth_date']

    objects = MyAccountManager()

    class Meta:
        ordering = ('first_name','last_name', 'email')

    def __str__(self):
        return self.first_name + ' ' + self.last_name

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_lable):
        return True
