# Importing like this cause we should follow "do not import unnecessary fields".
from django.db.models import (
    Model,
    CharField,
    TextField,
    DateField,
    EmailField,
    PositiveIntegerField,
    ForeignKey
)
from phonenumber_field.modelfields import PhoneNumberField
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFit

# local
from company.models import Department
from .validators import salary_validator
from .constants import DEPARTMENT_CHOICES
from .utils import get_largest_choice


class Employee(Model):
    # personal info related fields
    first_name = CharField(max_length=150)
    last_name = CharField(max_length=100, blank=True)
    email = EmailField(unique=True, error_messages={"unique": "Employee with this email already exists."})
    mobile = PhoneNumberField(region="BD", max_length=14, unique=True)
    date_of_birth = DateField()
    photo = ProcessedImageField(upload_to="employee/photo", processors=[ResizeToFit(220, 310)], format="png", options={'quality': 50}, null=True)

    # employment related fields
    date_of_joining = DateField()
    department = CharField(max_length=len(get_largest_choice(DEPARTMENT_CHOICES)), choices=DEPARTMENT_CHOICES)
    designation = CharField(max_length=100)
    salary = PositiveIntegerField(validators=[salary_validator])
    date_of_leave = DateField(null=True, blank=True, help_text="Date at which employee leaved that company permanently")
    responsibilities = TextField(blank=True, help_text="Actual job responsibilities of that employee")

    class Meta:
        verbose_name_plural = "Employee List"

    @property
    def full_name(self):
        """ Return first_name with last_name combined. """

        return f"{self.first_name} {self.last_name}".strip()
    
    @property
    def still_employee(self) -> bool:
        """ Flag to indicated that, this employee still works for that company or leaved permanently. """

        still_employee = True
        if self.date_of_leave:
            still_employee = False

        return still_employee
    
    def __str__(self) -> str:
        return self.full_name
    
    def save(self, **kwargs):
        if "date_of_leave" in kwargs:
            if not kwargs["date_of_leave"] > self.date_of_joining:
                kwargs["date_of_leave"] = None

        super().save(**kwargs)
