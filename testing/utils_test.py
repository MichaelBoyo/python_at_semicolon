import unittest
import utils


class MyTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        print("runs before all")

    @classmethod
    def tearDownClass(cls) -> None:
        print("runs after all")

    def test_for_error(self):
        with self.assertRaises(TypeError):
            utils.add("4", 3)

        self.assertRaises(TypeError, utils.add, "4", 2)

    def setUp(self) -> None:
        print("runs before each")

    def tearDown(self) -> None:
        print("runs after each")

    def test_something(self):
        self.assertEqual(True, True)

    def test_add(self):
        self.assertEqual(5, utils.add(3, 2))

    def test_list(self):
        self.assertListEqual([1, 4, 9], utils.square_list([1, 2, 3]))


if __name__ == '__main__':
    unittest.main()
