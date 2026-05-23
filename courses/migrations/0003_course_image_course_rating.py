from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_course_course_link_student'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='course_images/'),
        ),
        migrations.AddField(
            model_name='course',
            name='rating',
            field=models.FloatField(default=4.0),
        ),
    ]
