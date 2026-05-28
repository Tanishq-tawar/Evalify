from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_rename_created_at_connectionrequest_timestamp_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='startup',
            name='logo',
            field=models.ImageField(blank=True, null=True, upload_to='startup_logos/'),
        ),
    ]
