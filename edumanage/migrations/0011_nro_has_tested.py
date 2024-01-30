from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import edumanage.models


class Migration(migrations.Migration):

    dependencies = [
        ('edumanage', '0011_edb21_server_schema'),
    ]

    operations = [
        migrations.AddField(
            model_name='serviceloc',
            name='nro_has_tested',
            field=models.DateField(blank=True, null=True),
        ),
    ]