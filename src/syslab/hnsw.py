import heapq,math,random
from .distances import validate_vector,squared_l2
class HNSW:
    def __init__(self,dimension,m=8,ef_construction=32,seed=1):
        if dimension<1 or m<2 or ef_construction<m:raise ValueError('invalid index parameters')
        self.dimension,self.m,self.ef=dimension,m,ef_construction;self.rng=random.Random(seed);self.vectors={};self.levels={};self.layers={};self.deleted=set();self.entry=None;self.max_level=-1
    def distance(self,query,identity):return squared_l2(query,self.vectors[identity])
    def greedy(self,query,entry,level):
        current=entry;distance=self.distance(query,current)
        while True:
            better=current
            for peer in sorted(self.layers[level].get(current,())):
                score=self.distance(query,peer)
                if score<distance:better=peer;distance=score
            if better==current:return current
            current=better
    def search_layer(self,query,entries,ef,level):
        visited=set(entries);candidates=[];best=[]
        for identity in entries:
            dist=self.distance(query,identity);heapq.heappush(candidates,(dist,identity));heapq.heappush(best,(-dist,identity))
        while candidates:
            distance,current=heapq.heappop(candidates)
            if len(best)>=ef and distance>-best[0][0]:break
            for peer in sorted(self.layers[level].get(current,())):
                if peer in visited:continue
                visited.add(peer);dist=self.distance(query,peer)
                if len(best)<ef or dist<-best[0][0]:
                    heapq.heappush(candidates,(dist,peer));heapq.heappush(best,(-dist,peer))
                    if len(best)>ef:heapq.heappop(best)
        return sorted((-dist,identity) for dist,identity in best)
    def select(self,query,candidates,limit):
        selected=[];remaining=[]
        for distance,identity in sorted(candidates):
            diverse=True
            for peer in selected:
                separation=squared_l2(self.vectors[identity],self.vectors[peer])
                if separation<distance or (separation==0 and distance==0):
                    diverse=False;break
            if diverse:selected.append(identity)
            else:remaining.append(identity)
            if len(selected)==limit:return selected
        return (selected+remaining)[:limit]
    def add(self,identity,vector):
        if not isinstance(identity,str) or not identity or identity in self.vectors:raise ValueError('unique nonempty string ID required')
        vector=validate_vector(vector,self.dimension);level=min(16,int(-math.log(max(self.rng.random(),1e-12))/math.log(self.m)))
        self.vectors[identity]=vector;self.levels[identity]=level
        for layer in range(level+1):self.layers.setdefault(layer,{})[identity]=set()
        if self.entry is None:self.entry=identity;self.max_level=level;return
        entry=self.entry
        for layer in range(self.max_level,level,-1):entry=self.greedy(vector,entry,layer)
        for layer in range(min(level,self.max_level),-1,-1):
            candidates=self.search_layer(vector,[entry],self.ef,layer);limit=self.m*2 if layer==0 else self.m
            chosen=self.select(vector,candidates,limit);self.layers[layer][identity].update(chosen)
            for peer in chosen:
                self.layers[layer][peer].add(identity)
                if len(self.layers[layer][peer])>limit:
                    options=[(self.distance(self.vectors[peer],other),other) for other in self.layers[layer][peer]]
                    self.layers[layer][peer]=set(self.select(self.vectors[peer],options,limit))
            if candidates:entry=candidates[0][1]
        if level>self.max_level:self.entry=identity;self.max_level=level
    def search(self,query,k=5,ef=32):
        query=validate_vector(query,self.dimension)
        if k<1 or ef<k:raise ValueError('require ef >= k >= 1')
        if self.entry is None:return []
        entry=self.entry
        for level in range(self.max_level,0,-1):entry=self.greedy(query,entry,level)
        # Tombstones remain navigable; increase candidate budget to avoid under-filled results.
        candidates=self.search_layer(query,[entry],max(ef,k+len(self.deleted)),0)
        return [(identity,distance) for distance,identity in candidates if identity not in self.deleted][:k]
    def exact(self,query,k=5):
        query=validate_vector(query,self.dimension)
        return [(i,d) for d,i in sorted((self.distance(query,i),i) for i in self.vectors if i not in self.deleted)[:k]]
    def delete(self,identity):
        if identity not in self.vectors:raise KeyError(identity)
        self.deleted.add(identity)
