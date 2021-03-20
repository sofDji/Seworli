from django.db import migrations



def create_types(apps ,schema_editor):
    Types = apps.get_model('accounts', 'Types')
    Types.objects.create(name='Aérien' , color='#343a40²')
    Types.objects.create(name='Architecture' , color='#343a40²')
    Types.objects.create(name='Célébrité' , color='#343a40²')
    Types.objects.create(name='Fashion' , color='#343a40')
    Types.objects.create(name='Culinaire' , color='#343a40')
    Types.objects.create(name='Industrielle' , color='#343a40')
    Types.objects.create(name='Journalisme' , color='#343a40')
    Types.objects.create(name='Landscape' , color='#343a40')
    Types.objects.create(name='Macro' , color='#343a40')
    Types.objects.create(name='Mariage' , color='#343a40')
    Types.objects.create(name='Nature' , color='#343a40')
    Types.objects.create(name='Portrait' , color='#343a40')
    Types.objects.create(name='Publicité' , color='#343a40')
    Types.objects.create(name='sous l\'eau' , color='#343a40')
    Types.objects.create(name='Voyage' , color='#343a40')



class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_types),
    ]
