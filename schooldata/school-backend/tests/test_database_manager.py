from src.database_manager import SchoolDB
from django.test import TestCase


class DatabaseTestCase(TestCase):
    def test_store_data_in_db():
        SchoolDB.store_data_in_db(name="Isa", last_name="Garvi", subject="Math 3", year="2019-2020", mark=9.0)

        print(SchoolDB.Student.objects.all())
