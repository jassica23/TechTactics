from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lfa_app', '0004_lfa_stakeholders'),
    ]

    operations = [
        migrations.AddField(
            model_name='lfa',
            name='indicators',
            field=models.TextField(blank=True, null=True),
        ),
    ]
