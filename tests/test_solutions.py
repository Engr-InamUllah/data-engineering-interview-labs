import unittest
from python.solutions import deduplicate_latest,sessionize
class SolutionsTest(unittest.TestCase):
 def test_latest(self):self.assertEqual(deduplicate_latest([{"id":1,"u":1},{"id":1,"u":2}],"id","u")[0]["u"],2)
 def test_sessions(self):self.assertEqual(sessionize([0,100,2000]),[1,1,2])
if __name__=="__main__":unittest.main()