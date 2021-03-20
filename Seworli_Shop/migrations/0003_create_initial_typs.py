from django.db import migrations



def create_typapp(apps ,schema_editor):
    Typapp = apps.get_model('Seworli_Shop', 'Typapp')
    Typapp.objects.create(name='Reflexe')
    Typapp.objects.create(name='Hybride')
    Typapp.objects.create(name='Bridge')
    Typapp.objects.create(name='Compact')

def create_typlens(apps ,schema_editor):
    Typlens = apps.get_model('Seworli_Shop', 'Typlens')
    Typlens.objects.create(name='Panasonic-leica')
    Typlens.objects.create(name='Panasonic-lumix')
    Typlens.objects.create(name='Tamron')
    Typlens.objects.create(name='Canon')
    Typlens.objects.create(name='Fujifilm')
    Typlens.objects.create(name='Nikon')
    Typlens.objects.create(name='Sigma')
    Typlens.objects.create(name='Sony')
    Typlens.objects.create(name='Zeiss')

class Migration(migrations.Migration):

    dependencies = [
        ('Seworli_Shop', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_typapp),
        migrations.RunPython(create_typlens),

    ]
