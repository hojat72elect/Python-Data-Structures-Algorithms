import unittest
from src.Stack import Stack

class StackTest(unittest.TestCase):

    def setUp(self):
        self.stack = Stack()

    def test_push(self):
        self.stack.push(1)
        self.assertEqual(self.stack.getSize(), 1)
        self.stack.push(2)
        self.assertEqual(self.stack.getSize(), 2)
        self.assertEqual(self.stack.peek(), 2)

    def test_is_empty(self):
        self.assertTrue(self.stack.isEmpty())
        self.stack.push(1)
        self.assertFalse(self.stack.isEmpty())

    def test_pop(self):
        self.stack.push(1)
        self.stack.push(2)
        self.assertEqual(self.stack.pop(), 2)
        self.assertEqual(self.stack.getSize(), 1)
        self.assertEqual(self.stack.pop(), 1)
        self.assertEqual(self.stack.getSize(), 0)
        self.assertTrue(self.stack.isEmpty())

    def test_pop_empty_stack(self):
        with self.assertRaises(IndexError):
            self.stack.pop()

    def test_peek(self):
        self.stack.push(1)
        self.assertEqual(self.stack.peek(), 1)
        self.stack.push(2)
        self.assertEqual(self.stack.peek(), 2)
        self.assertEqual(self.stack.getSize(), 2)

    def test_peek_empty_stack(self):
        self.assertIsNone(self.stack.peek())

    def test_size(self):
        self.assertEqual(self.stack.getSize(), 0)
        self.stack.push(1)
        self.assertEqual(self.stack.getSize(), 1)
        self.stack.push(2)
        self.assertEqual(self.stack.getSize(), 2)
        self.stack.pop()
        self.assertEqual(self.stack.getSize(), 1)
        self.stack.pop()
        self.assertEqual(self.stack.getSize(), 0)

    def test_str(self):
        self.assertEqual(str(self.stack), "Stack is empty")
        self.stack.push(1)
        self.assertEqual(str(self.stack), "--- Top ---\n| 1\n--- Bottom ---")
        self.stack.push(2)
        self.assertEqual(str(self.stack), "--- Top ---\n| 2\n| 1\n--- Bottom ---")
