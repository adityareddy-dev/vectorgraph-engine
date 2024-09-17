import sys, unittest, json, math, tempfile
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'src'))
from syslab.core import run_case
from syslab.common import validate_case,check,dumps,atomic_json,finite_numbers
from syslab.cli import evaluate,cases
from syslab.hnsw import HNSW
class InsertTests(unittest.TestCase):
    def test_unique_id(self):
        h=HNSW(2);h.add('a',[0,0])
        with self.assertRaises(ValueError):h.add('a',[1,1])
    def test_degree_bound(self):
        h=HNSW(2,m=3,ef_construction=12)
        for i in range(60):h.add(str(i),[i%7,i])
        self.assertTrue(all(len(e)<=3*(2 if l==0 else 1) for l,n in h.layers.items() for e in n.values()))
