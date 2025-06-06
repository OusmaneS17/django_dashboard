# Generated by Django 5.2 on 2025-05-01 22:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard_app', '0004_portefeuille_axe'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='projet',
            name='cout',
        ),
        migrations.RemoveField(
            model_name='projet',
            name='date_lancement',
        ),
        migrations.RemoveField(
            model_name='projet',
            name='duree_mois',
        ),
        migrations.RemoveField(
            model_name='projet',
            name='financement_ppp',
        ),
        migrations.RemoveField(
            model_name='projet',
            name='financement_prive',
        ),
        migrations.RemoveField(
            model_name='projet',
            name='financement_public',
        ),
        migrations.RemoveField(
            model_name='projet',
            name='partenaire_pad',
        ),
        migrations.AddField(
            model_name='composante',
            name='cout',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True),
        ),
        migrations.AddField(
            model_name='composante',
            name='date_lancement',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='composante',
            name='duree_mois',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='composante',
            name='financement_ppp',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True),
        ),
        migrations.AddField(
            model_name='composante',
            name='financement_prive',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True),
        ),
        migrations.AddField(
            model_name='composante',
            name='financement_public',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True),
        ),
        migrations.AddField(
            model_name='composante',
            name='partenaire_pad',
            field=models.TextField(blank=True, null=True),
        ),
    ]
