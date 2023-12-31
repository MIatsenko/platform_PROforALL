# Generated by Django 4.2.3 on 2023-07-13 13:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main_app', '0002_lesson_course'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_of_payment', models.DateField(auto_now_add=True, verbose_name='дата оплаты')),
                ('payment_amount', models.IntegerField(verbose_name='сумма оплаты')),
                ('payment_method', models.CharField(choices=[('CASH', 'наличные'), ('TRANSFER_TO_ACCOUNT', 'перевод на счет')], max_length=50, verbose_name='способ оплаты')),
                ('paid_course', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main_app.course', verbose_name='оплаченный курс')),
                ('paid_lesson', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main_app.lesson', verbose_name='оплаченный урок')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='пользователь')),
            ],
            options={
                'verbose_name': 'способ оплаты',
                'verbose_name_plural': 'способы оплаты',
            },
        ),
    ]
