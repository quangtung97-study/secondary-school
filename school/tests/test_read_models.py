import unittest
from unittest import TestCase
from school.read_models import new_user, check_password


class ReadModels(TestCase):
    def test_check_password(self):
        user = new_user(
            "",
            "$2b$12$rWuHFkxmKZkLE1lfBLsWnOEhLXdh7gxLh4K50fkBnpsbY65JUdzOe",
            ""
        )

        self.assertFalse(check_password(None, ""))
        self.assertFalse(check_password(None, None))
        self.assertFalse(check_password(user, None))
        self.assertFalse(check_password(user, "tung"))
        self.assertTrue(check_password(user, "admin"))


if __name__ == '__main__':
    unittest.main()
