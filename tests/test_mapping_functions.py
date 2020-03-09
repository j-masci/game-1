import unittest
from .. mapping_functions import *

print("test mapping functions py")


class Test(unittest.TestCase):

    def TestBlah(self):
        self.assertEqual(90, maybe_round_up(90, 100, 5))
