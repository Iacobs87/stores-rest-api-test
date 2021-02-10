from models.user import UserModel
from tests.unit.unit_base_test import UnitBaseTest

class UserTest(UnitBaseTest):
    def test_create_user(self):
        user = UserModel('test', 'abcd')

        self.assertEqual(user.username, 'test', 'User name is not the expected one:')
        self.assertEqual(user.password, 'abcd', 'Password is not the expected one')