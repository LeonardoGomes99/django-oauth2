# Generated by Django 4.1.7 on 2023-03-13 20:19

import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Escritorio',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('ativo', models.BooleanField(blank=True, null=True)),
                ('bairro', models.CharField(blank=True, max_length=192, null=True)),
                ('cep', models.CharField(blank=True, max_length=12, null=True)),
                ('cidade', models.CharField(blank=True, max_length=32, null=True)),
                ('cnpj', models.CharField(blank=True, max_length=24, null=True, unique=True)),
                ('complemento', models.CharField(blank=True, max_length=64, null=True)),
                ('dataCadastro', models.DateTimeField(db_column='data_cadastro', null=True)),
                ('email', models.CharField(blank=True, max_length=64, null=True, unique=True)),
                ('imagem', models.TextField(blank=True, null=True)),
                ('inscricaoEstadual', models.CharField(blank=True, db_column='inscricao_estadual', max_length=255, null=True)),
                ('logradouro', models.CharField(blank=True, max_length=64, null=True)),
                ('matricula', models.CharField(blank=True, max_length=12, null=True)),
                ('nomeFantasia', models.CharField(blank=True, db_column='nome_fantasia', max_length=64, null=True)),
                ('numero', models.CharField(blank=True, max_length=8, null=True)),
                ('telefone', models.CharField(blank=True, max_length=14, null=True)),
                ('uf', models.CharField(blank=True, max_length=3, null=True)),
                ('ufInscricao', models.CharField(blank=True, db_column='uf_inscricao', max_length=255, null=True)),
            ],
            options={
                'db_table': 'tb_escritorio',
            },
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('nomeCompleto', models.CharField(blank=True, db_column='nome_completo', max_length=255, null=True)),
                ('nomeFantasia', models.CharField(blank=True, db_column='nome_fantasia', max_length=255, null=True)),
                ('nomeUsuario', models.CharField(blank=True, db_column='nome_usuario', max_length=255, null=True)),
                ('ativo', models.BooleanField(default=True)),
                ('bairro', models.CharField(blank=True, max_length=255, null=True)),
                ('celular', models.CharField(blank=True, max_length=255, null=True)),
                ('cep', models.CharField(blank=True, max_length=255, null=True)),
                ('cidade', models.CharField(blank=True, max_length=255, null=True)),
                ('cpf', models.CharField(blank=True, max_length=255, null=True)),
                ('dataNascimento', models.DateTimeField(blank=True, db_column='data_nascimento', null=True)),
                ('imgEsc', models.CharField(blank=True, db_column='img_esc', max_length=255, null=True)),
                ('logradouro', models.CharField(blank=True, max_length=255, null=True)),
                ('matricula', models.CharField(blank=True, max_length=255, null=True)),
                ('numero', models.CharField(blank=True, max_length=255, null=True)),
                ('sexo', models.CharField(blank=True, max_length=255, null=True)),
                ('telefone', models.CharField(blank=True, max_length=255, null=True)),
                ('uf', models.CharField(blank=True, max_length=255, null=True)),
                ('escritorioId', models.ForeignKey(db_column='escritorio_id', null=True, on_delete=django.db.models.deletion.CASCADE, to='authentication.escritorio')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'db_table': 'tb_user',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]