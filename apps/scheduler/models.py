from django.db import models


class Person(models.Model):
    roles = [
            ("LR", "Lecturer"),
            ("RR", "Reviewer"),
            ("WR", "Writer"),
            ("LS", "Supporter"),
            ("NE", "")
        ]
    name = models.CharField(max_length = 100,  unique = True)
    short_name = models.CharField(max_length = 100,  unique = True)
    email = models.CharField(max_length = 100,  unique = True)
    role = models.CharField(
            max_length = 2,
            choices = roles,
            null = True,
            default = "NE",
        )

    def __str__(self) -> str:
        return self.short_name


class Aviability(models.Model):
    ini = models.DateField()
    end = models.DateField()
    who = models.ForeignKey(Person,to_field = "id",
                             related_name = "aviabilities",
                             on_delete = models.SET_DEFAULT,
                             default = None, null = True)

    def __str__(self) -> str:
        return  "  ::  " + str(self.ini) + "  ->  " + str(self.end)
