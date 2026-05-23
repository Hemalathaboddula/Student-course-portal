from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0004_course_category_alter_course_course_link'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='image',
        ),
    ]
