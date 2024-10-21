import sys, unittest, json, math, tempfile
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'src'))
from syslab.core import run_case
from syslab.common import validate_case,check,dumps,atomic_json,finite_numbers
from syslab.cli import evaluate,cases
from syslab.hnsw import HNSW
from syslab.persistence import save,load
class PersistenceTests(unittest.TestCase):
    def test_roundtrip(self):
        with tempfile.TemporaryDirectory() as tmp:
            h=HNSW(2);h.add('a',[1,2]);p=Path(tmp)/'index';save(h,p);copy=load(p);self.assertEqual(h.search([1,2]),copy.search([1,2]))
    def test_corruption(self):
        with tempfile.TemporaryDirectory() as tmp:
            h=HNSW(2);h.add('a',[1,2]);p=Path(tmp)/'index';save(h,p);v=json.loads(p.read_text());v['payload']['vectors']['a'][0]=4;p.write_text(json.dumps(v))
            with self.assertRaises(ValueError):load(p)
