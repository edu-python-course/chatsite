from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('chatroom', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='chatroommessagemodel',
            options={
                'ordering': ('-created_at',), 'verbose_name': 'message',
                'verbose_name_plural': 'messages'
            },
        ),
    ]
