from django.test import TestCase
from school import read_models
from school import write_models


class ReadModels(TestCase):
    def test_check_password(self):
        user = read_models.new_user(
            "",
            "$2b$12$rWuHFkxmKZkLE1lfBLsWnOEhLXdh7gxLh4K50fkBnpsbY65JUdzOe",
            ""
        )

        self.assertFalse(read_models.check_password(None, ""))
        self.assertFalse(read_models.check_password(None, None))
        self.assertFalse(read_models.check_password(user, None))
        self.assertFalse(read_models.check_password(user, "tung"))
        self.assertTrue(read_models.check_password(user, "admin"))


class WriteModels(TestCase):
    def test_new_user(self):
        user = write_models.new_user("tung", "quangtung", "saodo")
        self.assertEqual(user['username'], 'tung')
        self.assertTrue(write_models.check_password(user, "quangtung"))
        self.assertEqual(user['privilegeId'], 2)

        user = write_models.new_user("tung", "quangtung", "abc")
        self.assertIsNone(user)
