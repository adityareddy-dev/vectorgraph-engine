import sys, unittest, json, math, tempfile
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'src'))
from syslab.core import run_case
from syslab.common import validate_case,check,dumps,atomic_json,finite_numbers
from syslab.cli import evaluate,cases
from syslab.hnsw import HNSW
class SearchTests(unittest.TestCase):
    def test_known_neighbors(self):
        h=HNSW(2)
        for i in range(10):h.add(str(i),[i,0])
        self.assertEqual(h.search([3.1,0],1,10)[0][0],'3')
    def test_dense_duplicates_keep_bridges(self):
        h=HNSW(2,m=4,ef_construction=16)
        for i in range(40):h.add('duplicate-'+str(i),[0,0])
        for i in range(8):h.add('distinct-'+str(i),[i+1,0])
        self.assertEqual(h.search([8.1,0],1,32)[0][0],'distinct-7')
    def test_empty_and_invalid(self):
        h=HNSW(2);self.assertEqual(h.search([0,0]),[])
        with self.assertRaises(ValueError):h.add('x',[0,float('nan')])
