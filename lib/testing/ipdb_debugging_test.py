#!/usr/bin/env python3

from lib.ipdb_debugging import plus_two

class TestIpdbDebugging:
    '''Tests for ipdb_debugging.py'''

    def test_adds_two(self):
        '''plus_two() adds 2 to input arg and returns sum.'''
        assert plus_two(3) == 5
