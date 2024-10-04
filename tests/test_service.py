import sys, unittest, json, math, tempfile
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'src'))
from syslab.core import run_case
from syslab.common import validate_case,check,dumps,atomic_json,finite_numbers
from syslab.cli import evaluate,cases
from syslab.service import VectorService
class ServiceTests(unittest.TestCase):
    def test_delete(self):
        s=VectorService(2);s.execute({'op':'insert','id':'a','vector':[1,2]});s.execute({'op':'delete','id':'a'});self.assertEqual(s.execute({'op':'search','vector':[1,2]})['neighbors'],[])
    def test_unknown(self):
        with self.assertRaises(ValueError):VectorService(2).execute({'op':'bad'})
