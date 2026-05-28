from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_startup_logo'),
    ]

    operations = [
        migrations.AddField(
            model_name='mentor',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='mentor_photos/'),
        ),
        migrations.AddField(
            model_name='investor',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='investor_photos/'),
        ),
    ]
