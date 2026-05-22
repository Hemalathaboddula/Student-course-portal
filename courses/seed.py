def seed_data():
    from courses.models import Course

    if Course.objects.exists():
        print("Data already exists")
        return

    Course.objects.create(
        title="Python for Beginners",
        instructor="Green Chameleon",
        rating=4.0
    )

    Course.objects.create(
        title="AWS",
        instructor="Stephane Maarek",
        rating=4.0
    )

    Course.objects.create(
        title="Java Spring Boot",
        instructor="Navin Reddy",
        rating=4.0
    )

    print("✅ Sample courses created!")
