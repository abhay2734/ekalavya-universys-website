from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0034_ekalavyalandingsection'),
    ]

    operations = [
        migrations.AddField(
            model_name='ekalavyalandingsection',
            name='thumbnail',
            field=models.ImageField(help_text='Section thumbnail image', upload_to='ekalavya/landing/thumbnails/'),
        ),
    ]