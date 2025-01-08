from django.db import models

class Resume(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    dream_position = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    location = models.CharField(max_length=255)
    salary = models.CharField(max_length=50) # format undecided
    age = models.IntegerField() 
    languages = models.CharField(max_length=255)
    skills = models.TextField()
    
    # JSONField to store education details
    education = models.JSONField(blank=True, null=True)
    # Expected format:
    # [
    #     {
    #         "level": "Bachelors",
    #         "institution": "Oin College",
    #         "major": "Computer Science",
    #         "period": "2019 - Current"
    #     },
    #     {
    #         "level": "Graduate",
    #         "institution": "Harvard University",
    #         "major": "Data Science",
    #         "period": "2022-2024"
    #     }
    # ]

    # JSONField to store work experiences
    work_experiences = models.JSONField(blank=True, null=True)
    # Expected format:
    # [
    #     {
    #         "company_name": "Oin Auto",
    #         "role": "Software Engineer",
    #         "work_period": "05/2024 - 09/2024",
    #         "job_description": "Worked on developing web applications"
    #     },
    #     {
    #         "company_name": "Netflix",
    #         "role": "UI/UX Designer",
    #         "work_period": "01/2023 - 09/2024",
    #         "job_description": "Led the team to develop innovative solutions"
    #     }
    # ]

    # Timestamp fields
    create_time = models.DateTimeField(auto_now_add=True)
    modify_time = models.DateTimeField(auto_now=True)
    delete_time = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.name} - {self.dream_position}"
