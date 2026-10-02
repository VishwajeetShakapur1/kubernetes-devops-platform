import unittest
import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).parents[1]/"order-service"))
import app
class TestOrder(unittest.TestCase):
    def test_counters_exist(self):
        self.assertGreaterEqual(app.REQUESTS,0)
        self.assertGreaterEqual(app.ERRORS,0)
if __name__=="__main__":
    unittest.main()
