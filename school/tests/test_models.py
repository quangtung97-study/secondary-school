import unittest
from unittest import TestCase
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
        self.assertEqual(user['privilegeName'], 'saodo')

        user = write_models.new_user("tung", "quangtung", "abc")
        self.assertIsNone(user)

    def test_get_new_user_after_change_password_success(self):
        old_user = write_models.new_user("tung", "quangtung", "loptruong")
        new_user = write_models.get_new_user_after_change_password(
            old_user=old_user,
            old_password="quangtung",
            new_password="ngan",
            re_enter_new_password="ngan"
        )
        self.assertEqual(new_user['username'], "tung")
        self.assertTrue(write_models.check_password(new_user, "ngan"))

    def test_get_new_user_after_change_password_fail_wrong_old_password(self):
        old_user = write_models.new_user("tung", "quangtung", "loptruong")
        new_user = write_models.get_new_user_after_change_password(
            old_user=old_user,
            old_password="trang",
            new_password="ngan",
            re_enter_new_password="ngan"
        )
        self.assertIsNone(new_user)

    def test_get_new_user_after_change_password_not_same_new_password(self):
        old_user = write_models.new_user("tung", "quangtung", "loptruong")
        new_user = write_models.get_new_user_after_change_password(
            old_user=old_user,
            old_password="quangtung",
            new_password="ngan",
            re_enter_new_password="tung"
        )
        self.assertIsNone(new_user)


if __name__ == '__main__':
    unittest.main()
