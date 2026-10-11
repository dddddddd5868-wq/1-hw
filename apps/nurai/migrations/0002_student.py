from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nurai', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Nurai',
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Имя')),
                ('age', models.IntegerField(verbose_name='Возраст')),
                ('city', models.CharField(max_length=100, verbose_name='Город')),
                ('email', models.EmailField(verbose_name='Email')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
            ],
            options={
                'verbose_name': 'Студент',
                'verbose_name_plural': 'Студенты',
            },
        ),
    ]
