import random,tempfile
from pathlib import Path
from .common import validate_case
from .hnsw import HNSW
from .persistence import save,load
FAMILIES=('uniform','clusters','duplicates','delete','restore','dimensions')
def run_case(case):
    validate_case(case)
    if case['family'] not in FAMILIES:raise ValueError('unknown vector family')
    rng=random.Random(case['seed']);dimension=case.get('dimension',8);index=HNSW(dimension,seed=case['seed']);n=case['size'];family=case['family']
    for i in range(n):
        vector=[rng.gauss((i%3)*3, .3) if family=='clusters' else rng.uniform(-1,1) for _ in range(dimension)]
        if family=='duplicates' and i%3==0:vector=[.5]*dimension
        index.add(f'v{i:04d}',vector)
    if family=='delete':
        for i in range(0,n,5):index.delete(f'v{i:04d}')
    restored=True
    if family=='restore':
        with tempfile.TemporaryDirectory() as tmp:
            path=Path(tmp)/'index.json';save(index,path);copy=load(path);restored=copy.vectors==index.vectors and copy.layers==index.layers;index=copy
    recalls=[];results=[];distances_valid=True;not_deleted=True;exact_radius_hits=0;returned=0;complete=True
    for j in range(8):
        query=[rng.uniform(-1,1) for _ in range(dimension)];approx=index.search(query,5,64);exact=index.exact(query,5)
        complete=complete and len(approx)==min(5,len(index.vectors)-len(index.deleted))
        exact_radius_hits+=sum(d<=exact[-1][1]+1e-9 for i,d in approx);returned+=len(approx)
        a={i for i,d in approx};e={i for i,d in exact};recalls.append(len(a&e)/len(e));results.append(approx)
        distances_valid=distances_valid and all(abs(index.distance(query,i)-d)<1e-9 for i,d in approx);not_deleted=not_deleted and not(a&index.deleted)
    bounded=all(len(edges)<=index.m*(2 if level==0 else 1) for level,nodes in index.layers.items() for edges in nodes.values())
    return {'metrics':{'inserted':n,'active':n-len(index.deleted),'queries':8,'recall_at_5':sum(recalls)/len(recalls),'within_exact_radius':exact_radius_hits/returned if returned else 0.,'distances_correct':distances_valid,'deleted_excluded':not_deleted,'bounded_degree':bounded,'complete_results':complete,'restored_equal':restored,'max_level':index.max_level},'output':results[:2]}
