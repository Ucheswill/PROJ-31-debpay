# Generated by Django 4.0.5 on 2022-08-07 21:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Debtor', '0005_alter_debtor_student_class'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='debtor',
            name='full_name',
        ),
        migrations.AlterField(
            model_name='deptors_profile',
            name='debtor',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='Debtor.debtor'),
        ),
    ]
