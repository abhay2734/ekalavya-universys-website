from django.db import migrations


def update_clarity_content(apps, schema_editor):
    # Legacy data migration placeholder. The main_content HTML field was later
    # replaced by discrete structured fields, so no content is migrated here.
    pass


def revert_clarity_content(apps, schema_editor):
    pass


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0014_homepage_redesign'),
    ]

    operations = [
        migrations.RunPython(update_clarity_content, revert_clarity_content),
    ]
