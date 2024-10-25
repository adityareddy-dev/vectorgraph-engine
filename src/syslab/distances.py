import math

def validate_vector(vector,dimension):
    if len(vector)!=dimension or dimension<1 or any(not isinstance(x,(int,float)) or not math.isfinite(x) for x in vector):raise ValueError('vector dimension or values invalid')
    return [float(x) for x in vector]
def squared_l2(a,b):return sum((x-y)**2 for x,y in zip(a,b))
def cosine(a,b):
    na=math.sqrt(sum(x*x for x in a));nb=math.sqrt(sum(x*x for x in b))
    if na==0 or nb==0:raise ValueError('cosine requires nonzero vectors')
    return 1-sum(x*y for x,y in zip(a,b))/(na*nb)
