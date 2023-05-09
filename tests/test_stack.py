"""Здесь надо написать тесты с использованием unittest для модуля stack."""
import unittest

from src.stack import Stack


class TestStack(unittest.TestCase):
    def setUp(self):
        self.stack = Stack()

    def test_push(self):
        self.stack.push(1)
        self.assertEqual(self.stack.top.data, 1)
        self.stack.push(2)
        self.assertEqual(self.stack.top.data, 2)

    def test_pop(self):
        self.assertIsNone(self.stack.pop())
        self.stack.push(1)
        self.stack.push(2)


if __name__ == '__main__':
    unittest.main()
