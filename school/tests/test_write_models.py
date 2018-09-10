import unittest
from unittest import TestCase
from school.write_models import new_user, check_password
from school.write_models import get_new_user_after_change_password
from school.write_models import new_user_for_adding


class WriteModels(TestCase):
    def test_new_user(self):
        user = new_user("tung", "quangtung", "saodo")
        self.assertEqual(user['username'], 'tung')
        self.assertTrue(check_password(user, "quangtung"))
        self.assertEqual(user['privilegeName'], 'saodo')

        user = new_user("tung", "quangtung", "abc")
        self.assertIsNone(user)

    def test_get_new_user_after_change_password_success(self):
        olduser = new_user("tung", "quangtung", "loptruong")
        newuser = get_new_user_after_change_password(
            old_user=olduser,
            old_password="quangtung",
            new_password="ngan",
            re_enter_new_password="ngan"
        )
        self.assertEqual(newuser['username'], "tung")
        self.assertTrue(check_password(newuser, "ngan"))

    def test_get_new_user_after_change_password_fail_wrong_old_password(self):
        olduser = new_user("tung", "quangtung", "loptruong")
        newuser = get_new_user_after_change_password(
            old_user=olduser,
            old_password="trang",
            new_password="ngan",
            re_enter_new_password="ngan"
        )
        self.assertIsNone(newuser)

    def test_get_new_user_after_change_password_not_same_new_password(self):
        olduser = new_user("tung", "quangtung", "loptruong")
        newuser = get_new_user_after_change_password(
            old_user=olduser,
            old_password="quangtung",
            new_password="ngan",
            re_enter_new_password="tung"
        )
        self.assertIsNone(newuser)

    def test_new_user_for_adding(self):
        user = new_user_for_adding("tung", "quangtung", "tung", "saodo")
        self.assertIsNone(user)
        user = new_user_for_adding("tung", "quangtung", "quangtung", "admin")
        self.assertIsNone(user)
        user = new_user_for_adding("tung", "quangtung", "quangtung", "saodo")
        self.assertIsNotNone(user)


if __name__ == '__main__':
    unittest.main()
