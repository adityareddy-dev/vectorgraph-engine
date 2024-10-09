import hashlib,json,ast
from .common import dumps,atomic_json
from .hnsw import HNSW
from .distances import validate_vector

def save(index,path):
    payload={'version':1,'dimension':index.dimension,'m':index.m,'ef':index.ef,'vectors':index.vectors,'levels':index.levels,'layers':{str(l):{i:sorted(n) for i,n in nodes.items()} for l,nodes in index.layers.items()},'deleted':sorted(index.deleted),'entry':index.entry,'max_level':index.max_level,'rng_state':repr(index.rng.getstate())}
    atomic_json(path,{'payload':payload,'sha256':hashlib.sha256(dumps(payload).encode()).hexdigest()})
def load(path):
    envelope=json.loads(path.read_text());p=envelope['payload']
    if hashlib.sha256(dumps(p).encode()).hexdigest()!=envelope['sha256']:raise ValueError('index checksum mismatch')
    if p['version']!=1:raise ValueError('unsupported index version')
    index=HNSW(p['dimension'],p['m'],p['ef']);index.vectors={i:validate_vector(v,p['dimension']) for i,v in p['vectors'].items()};index.levels=p['levels'];index.layers={int(l):{i:set(neighbors) for i,neighbors in nodes.items()} for l,nodes in p['layers'].items()};index.deleted=set(p['deleted']);index.entry=p['entry'];index.max_level=p['max_level']
    if not index.deleted<=index.vectors.keys() or (index.entry is not None and index.entry not in index.vectors):raise ValueError('invalid graph references')
    for level,nodes in index.layers.items():
        limit=index.m*2 if level==0 else index.m
        for identity,neighbors in nodes.items():
            if identity not in index.vectors or not neighbors<=nodes.keys() or len(neighbors)>limit:raise ValueError('invalid graph edges')
    index.rng.setstate(ast.literal_eval(p['rng_state']));return index
