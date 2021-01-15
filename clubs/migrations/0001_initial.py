# Generated by Django 3.1.4 on 2021-01-13 20:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Administration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Advisor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userId', models.CharField(max_length=150, unique=True)),
                ('first_name', models.CharField(blank=True, max_length=150)),
                ('last_name', models.CharField(blank=True, max_length=150)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('profile_pic', models.ImageField(blank=True, default='profile1.png', null=True, upload_to='')),
                ('department', models.CharField(blank=True, max_length=150)),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Club',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('club_name', models.CharField(max_length=150)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('club_pic', models.ImageField(blank=True, default='profile1.png', null=True, upload_to='')),
                ('administration', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='clubs.administration')),
                ('advisor', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='clubs.advisor')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userId', models.CharField(max_length=150, unique=True)),
                ('first_name', models.CharField(blank=True, max_length=150)),
                ('last_name', models.CharField(blank=True, max_length=150)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('profile_pic', models.ImageField(blank=True, default='profile1.png', null=True, upload_to='')),
                ('department', models.CharField(blank=True, max_length=150)),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Survey',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('end_date', models.DateTimeField(blank=True, null=True)),
                ('question', models.TextField(blank=True, null=True)),
                ('yes', models.BooleanField(blank=True, null=True)),
                ('no', models.BooleanField(blank=True, null=True)),
                ('club', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='clubs.club')),
                ('publisher', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='clubs.student')),
            ],
        ),
        migrations.CreateModel(
            name='Posts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('content', models.TextField(blank=True, null=True)),
                ('club', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='clubs.club')),
                ('publisher', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='clubs.student')),
            ],
        ),
        migrations.CreateModel(
            name='MessageDialog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(blank=True, null=True)),
                ('start_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('receiver', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='receivers', related_query_name='receiver', to='clubs.student')),
                ('sender', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='senders', related_query_name='sender', to='clubs.student')),
            ],
        ),
        migrations.CreateModel(
            name='Discussion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic', models.CharField(blank=True, max_length=50)),
                ('content', models.TextField(blank=True, null=True)),
                ('start_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('club', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='clubs.club')),
                ('publisher', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='clubs.student')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('discussion', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='clubs.discussion')),
                ('person', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='clubs.student')),
            ],
        ),
        migrations.CreateModel(
            name='ClubStudent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('club', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='clubs.club')),
                ('student', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='clubs.student')),
            ],
        ),
        migrations.CreateModel(
            name='Announcement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=50)),
                ('content', models.TextField(blank=True, null=True)),
                ('start_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('club', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='clubs.club')),
                ('publisher', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='clubs.student')),
            ],
        ),
        migrations.AddField(
            model_name='administration',
            name='accountant',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='accountant', related_query_name='accountant', to='clubs.student'),
        ),
        migrations.AddField(
            model_name='administration',
            name='advisor',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='advisor', related_query_name='advisor', to='clubs.advisor'),
        ),
        migrations.AddField(
            model_name='administration',
            name='agent',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='agent', related_query_name='agent', to='clubs.student'),
        ),
        migrations.AddField(
            model_name='administration',
            name='president',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='president', related_query_name='president', to='clubs.student'),
        ),
        migrations.AddField(
            model_name='administration',
            name='secretary',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='secretary', related_query_name='secretary', to='clubs.student'),
        ),
        migrations.AddField(
            model_name='administration',
            name='vicePresident',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='vicePresident', related_query_name='vicePresident', to='clubs.student'),
        ),
    ]
