from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0039_remove_homepage_legacy_fields'),
    ]

    operations = [
        migrations.AddField(
            model_name='claritypage',
            name='cta_button_link',
            field=models.CharField(
                blank=True,
                help_text='CTA button link URL (defaults to the FREE TRAINING page)',
                max_length=500,
            ),
        ),
        migrations.AddField(
            model_name='claritypage',
            name='cta_button_text',
            field=models.CharField(
                blank=True,
                default='Launch the FREE 3-Concept Challenge →',
                help_text='CTA button text',
                max_length=200,
            ),
        ),
        migrations.AddField(
            model_name='claritypage',
            name='cta_description',
            field=models.TextField(
                blank=True,
                default='The best way to evaluate any learning system is to experience it yourself.\n\nTake our FREE 3-Concept Challenge and discover how Ekalavya transforms understanding into confident explanation.',
                help_text='CTA section description',
            ),
        ),
        migrations.AddField(
            model_name='claritypage',
            name='cta_subtitle',
            field=models.CharField(
                blank=True,
                default='🎯 Experience CLARITY Before You Enroll',
                help_text='CTA section subtitle',
                max_length=200,
            ),
        ),
        migrations.AddField(
            model_name='claritypage',
            name='cta_title',
            field=models.CharField(
                blank=True,
                default='🟢 Test Before You Trust',
                help_text='CTA section title',
                max_length=200,
            ),
        ),
        migrations.AddField(
            model_name='claritypage',
            name='section1_image',
            field=models.ImageField(
                blank=True,
                null=True,
                help_text='Image displayed in Section 1',
                upload_to='clarity/',
            ),
        ),
        migrations.AddField(
            model_name='claritypage',
            name='section2_image',
            field=models.ImageField(
                blank=True,
                null=True,
                help_text='Image displayed in Section 2',
                upload_to='clarity/',
            ),
        ),
    ]
