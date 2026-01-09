#
# This is a special case migration that merges the upstream DjNRO branch's
# migrations with our own local migrations. It needs to be updated whenever
# there are new migrations in either branch (caused by e.g. rebasing or by
# new local changes being added). It should always be the last migration in
# the migration history. To make migrations apply cleanly it may be necessary
# to reverse and reapply this migration after updating it. To do this, run:
#
# /srv/djnro/.venv/bin/python /srv/djnro/manage.py migrate --noinput edumanage 0103
# /srv/djnro/.venv/bin/python /srv/djnro/manage.py migrate --noinput edumanage
#
# subsituting the 0103 above with whatever the latest local migration is.
#
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        # This depedency should be the latest migration from the upstream branch
        ('edumanage', '0014_remove_obsolete_registration_profile_table'),
        # This dependency should be the latest local migration
        ('edumanage', '0103_nro_has_tested'),
    ]

    operations = [
    ]
