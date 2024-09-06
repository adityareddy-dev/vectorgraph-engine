from .hnsw import HNSW
class VectorService:
    def __init__(self,dimension):self.index=HNSW(dimension)
    def execute(self,request):
        op=request.get('op')
        if op=='insert':self.index.add(request['id'],request['vector']);return {'inserted':request['id']}
        if op=='search':return {'neighbors':self.index.search(request['vector'],request.get('k',5),request.get('ef',32))}
        if op=='delete':self.index.delete(request['id']);return {'deleted':request['id']}
        raise ValueError('unsupported vector operation')
