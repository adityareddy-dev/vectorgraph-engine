# Architecture

VectorService → HNSW nodes/layers → ANN search. Exact search is an independent distance-scan oracle. JSON persistence saves vectors, edges, levels and RNG state.
