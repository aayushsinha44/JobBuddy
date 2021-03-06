# Generated by Django 2.1.7 on 2019-03-13 11:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='CandidateJobStatusModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('1', 'No freelancer tagged'), ('2', 'freelancer authorisation pending'), ('3', '')], max_length=100)),
                ('candidate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.CandidateModel')),
            ],
        ),
        migrations.CreateModel(
            name='FreelancerJobTakeAwayModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('freelancer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.FreelancerModel')),
            ],
        ),
        migrations.CreateModel(
            name='JobAnswerModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.TextField()),
                ('candidate_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.CandidateModel')),
            ],
        ),
        migrations.CreateModel(
            name='JobModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_title', models.CharField(max_length=100)),
                ('job_type', models.CharField(choices=[('FT', 'Full Time'), ('IN', 'Intern'), ('PT', 'Part Time'), ('CN', 'Contract')], max_length=100)),
                ('job_qualification', models.TextField()),
                ('job_location', models.CharField(max_length=255)),
                ('salary_range_min', models.BigIntegerField(blank=True, null=True)),
                ('salary_range_max', models.BigIntegerField(blank=True, null=True)),
                ('work_experience_min', models.BigIntegerField(blank=True, null=True)),
                ('work_experience_max', models.BigIntegerField(blank=True, null=True)),
                ('no_of_opening', models.BigIntegerField(blank=True, null=True)),
                ('job_description', models.TextField()),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.CompanyModel')),
                ('recruiter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.RecruiterModel')),
            ],
        ),
        migrations.CreateModel(
            name='JobQuestionModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=255)),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jobs.JobModel')),
            ],
        ),
        migrations.AddField(
            model_name='jobanswermodel',
            name='job_question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jobs.JobQuestionModel'),
        ),
        migrations.AddField(
            model_name='freelancerjobtakeawaymodel',
            name='job',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jobs.JobModel'),
        ),
    ]
