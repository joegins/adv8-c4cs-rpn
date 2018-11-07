#!/usr/bin/env python3
import unittest

import rpn

class TestBasics(unittest.TestCase):
    def test_add(self):
        result = rpn.calculate("1 1 +")
        print(Fore.RED + '1 1 +')
        print(Fore.GREEN, result)
        self.assertEqual(2, result)
    def test_subtract(self):
        result = rpn.calculate("5 3 -")
        print(Fore.RED + '5 3 -')
        print(Fore.GREEN, result)
        self.assertEqual(2, result)
    def test_multiply(self):
        result = rpn.calculate("5 3 *")
        print(Fore.RED + ' 5 3 *')
        print(Fore.GREEN, result)
        self.assertEqual(15, result)
    def test_divide(self):
        result = rpn.calculate("6 3 /")
        print(Fore.RED + '6 3 / ')
        print(Fore.GREEN, result)
        self.assertEqual(2, result)
    def test_carat(self):
        result = rpn.calculate("3 3 ^")
        print(Fore.RED + '3 3 ^')
        print(Fore.GREEN, result)
    	self.assertEqual(27, result)
