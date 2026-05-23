from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0003_course_image_course_rating'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='category',
            field=models.CharField(choices=[('python', 'Python'), ('aws', 'AWS'), ('ai', 'AI')], default='python', max_length=20),
        ),
        migrations.AlterField(
            model_name='course',
            name='course_link',
            field=models.URLField(),
        ),
    ]
