from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import edumanage.models


class Migration(migrations.Migration):

    dependencies = [
        ('edumanage', '0012_venue_info_select'),
        ('edumanage', '0102_eap_versions'),
    ]

    operations = [
        migrations.AddField(
            model_name='serviceloc',
            name='nro_has_tested',
            field=models.DateField(blank=True, null=True),
        ),
    ]
