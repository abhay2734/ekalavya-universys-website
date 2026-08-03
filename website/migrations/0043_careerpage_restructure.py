from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0042_add_capability_page_new_fields'),
    ]

    operations = [
        migrations.AddField(
            model_name='careerpage',
            name='page_title',
            field=models.CharField(blank=True, help_text='Large title displayed in Section 1 of the CAREER page', max_length=200),
        ),
        migrations.AddField(
            model_name='careerpage',
            name='description',
            field=models.TextField(blank=True, help_text='Description content displayed in the Description Card section'),
        ),
        migrations.AddField(
            model_name='careerpage',
            name='career_path_image',
            field=models.ImageField(blank=True, help_text='Career Path image displayed in Section 4', null=True, upload_to='career/'),
        ),
        migrations.AddField(
            model_name='careerpage',
            name='specializations_section_title',
            field=models.CharField(blank=True, help_text='Section title for the Career Specializations section', max_length=200),
        ),
        migrations.AddField(
            model_name='careerpage',
            name='specializations_section_subtitle',
            field=models.CharField(blank=True, help_text='Section subtitle for the Career Specializations section', max_length=200),
        ),
        migrations.AddField(
            model_name='careerpage',
            name='specialization_list',
            field=models.TextField(blank=True, help_text='Career specializations - one per line'),
        ),
        migrations.AddField(
            model_name='careerpage',
            name='closing_statement',
            field=models.TextField(blank=True, help_text='Closing statement displayed below the specialization list'),
        ),
        migrations.AddField(
            model_name='careerpage',
            name='expert_reviews_title',
            field=models.CharField(blank=True, help_text='Title for the Expert Reviews CTA section', max_length=200),
        ),
        migrations.AddField(
            model_name='careerpage',
            name='expert_reviews_subtitle',
            field=models.TextField(blank=True, help_text='Subtitle for the Expert Reviews CTA section'),
        ),
        migrations.AddField(
            model_name='careerpage',
            name='expert_reviews_button_text',
            field=models.CharField(blank=True, help_text='Button text for the Expert Reviews CTA', max_length=100),
        ),
    ]