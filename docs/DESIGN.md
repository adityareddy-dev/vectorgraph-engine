# Design

Use squared L2 throughout; results expose squared distance explicitly. Measure recall against an exhaustive scan. Workloads require at least .8 recall except duplicate vectors, where an exact-distance-radius gate accepts alternative tied neighbors. Keep tombstones traversable to preserve reachability.
