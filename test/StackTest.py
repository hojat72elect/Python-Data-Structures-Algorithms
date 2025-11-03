import unittest
from src.Stack import Stack

class StackTest(unittest.TestCase):

    def setUp(self):
        self.sut = Stack()

    def test_push(self):
        self.sut.push(1)
        self.assertEqual(self.sut.getSize(), 1)
        self.sut.push(2)
        self.assertEqual(self.sut.getSize(), 2)
        self.assertEqual(self.sut.peek(), 2)

    def test_is_empty(self):
        self.assertTrue(self.sut.isEmpty())
        self.sut.push(1)
        self.assertFalse(self.sut.isEmpty())

    def test_pop(self):
        self.sut.push(1)
        self.sut.push(2)
        self.assertEqual(self.sut.pop(), 2)
        self.assertEqual(self.sut.getSize(), 1)
        self.assertEqual(self.sut.pop(), 1)
        self.assertEqual(self.sut.getSize(), 0)
        self.assertTrue(self.sut.isEmpty())

    def test_pop_empty_stack(self):
        with self.assertRaises(IndexError):
            self.sut.pop()

    def test_peek(self):
        self.sut.push(1)
        self.assertEqual(self.sut.peek(), 1)
        self.sut.push(2)
        self.assertEqual(self.sut.peek(), 2)
        self.assertEqual(self.sut.getSize(), 2)

    def test_peek_empty_stack(self):
        self.assertIsNone(self.sut.peek())

    def test_size(self):
        self.assertEqual(self.sut.getSize(), 0)
        self.sut.push(1)
        self.assertEqual(self.sut.getSize(), 1)
        self.sut.push(2)
        self.assertEqual(self.sut.getSize(), 2)
        self.sut.pop()
        self.assertEqual(self.sut.getSize(), 1)
        self.sut.pop()
        self.assertEqual(self.sut.getSize(), 0)

    def test_str(self):
        self.assertEqual(str(self.sut), "Stack is empty")
        self.sut.push(1)
        self.assertEqual(str(self.sut), "--- Top ---\n| 1\n--- Bottom ---")
        self.sut.push(2)
        self.assertEqual(str(self.sut), "--- Top ---\n| 2\n| 1\n--- Bottom ---")
