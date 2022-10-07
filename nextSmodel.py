# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Anketa(models.Model):
    fullname = models.CharField(max_length=255)
    email = models.CharField(max_length=255, blank=True, null=True)
    phone_number = models.CharField(unique=True, max_length=11)
    telegram_id = models.BigIntegerField(unique=True)

    class Meta:
        managed = False
        db_table = 'anketa'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class BasicApp1(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=100)
    description = models.TextField()
    character = models.TextField()
    instruction = models.TextField()
    views = models.TextField()
    conutry = models.CharField(max_length=128)

    class Meta:
        managed = False
        db_table = 'basic_app_лекарства1'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class ElonIshJoyiKerak(models.Model):
    ismi = models.CharField(max_length=255)
    yoshi = models.CharField(max_length=255)
    texnologiya = models.CharField(max_length=255)
    aloqa = models.CharField(max_length=255)
    hudud = models.CharField(max_length=255)
    narxi = models.CharField(max_length=255)
    kasbi = models.CharField(max_length=255)
    murojaat_vaqti = models.CharField(max_length=255)
    maqsad = models.CharField(max_length=255)
    telegram_id = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'elon_ish_joyi_kerak'


class ElonSherik(models.Model):
    ismi = models.CharField(max_length=255)
    yoshi = models.CharField(max_length=255)
    texnologiya = models.CharField(max_length=255)
    aloqa = models.CharField(max_length=255)
    hudud = models.CharField(max_length=255)
    narxi = models.CharField(max_length=255)
    kasbi = models.CharField(max_length=255)
    murojaat_vaqti = models.CharField(max_length=255)
    maqsad = models.CharField(max_length=255)
    telegram_id = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'elon_sherik'


class ElonShogird(models.Model):
    ismi = models.CharField(max_length=255)
    yoshi = models.CharField(max_length=255)
    texnologiya = models.CharField(max_length=255)
    aloqa = models.CharField(max_length=255)
    hudud = models.CharField(max_length=255)
    narxi = models.CharField(max_length=255)
    kasbi = models.CharField(max_length=255)
    murojaat_vaqti = models.CharField(max_length=255)
    maqsad = models.CharField(max_length=255)
    telegram_id = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'elon_shogird'


class ElonUstozKerak(models.Model):
    ismi = models.CharField(max_length=255)
    yoshi = models.CharField(max_length=255)
    texnologiya = models.CharField(max_length=255)
    aloqa = models.CharField(max_length=255)
    hudud = models.CharField(max_length=255)
    narxi = models.CharField(max_length=255)
    kasbi = models.CharField(max_length=255)
    murojaat_vaqti = models.CharField(max_length=255)
    maqsad = models.CharField(max_length=255)
    telegram_id = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'elon_ustoz_kerak'


class ElonXodim(models.Model):
    idora_nomi = models.CharField(max_length=255)
    texnologiya = models.CharField(max_length=255)
    aloqa = models.CharField(max_length=255)
    hudud = models.CharField(max_length=255)
    masul_ismi = models.CharField(max_length=255)
    murojaat_vaqti = models.CharField(max_length=255)
    ish_vaqti = models.CharField(max_length=255)
    narxi = models.CharField(max_length=255)
    qoshimcha_malumot = models.CharField(max_length=255)
    telegram_id = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'elon_xodim'


class Users(models.Model):
    full_name = models.CharField(max_length=255)
    username = models.CharField(max_length=255, blank=True, null=True)
    telegram_id = models.BigIntegerField(unique=True)

    class Meta:
        managed = False
        db_table = 'users'
