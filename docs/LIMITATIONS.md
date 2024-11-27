# Limitations

Python reference, not a million-vector production database. No embedding model, concurrency control, compressed vectors or live gRPC transport. proto schema is a design artifact only. Graph links may become asymmetric after per-node degree pruning. Deleted nodes remain in memory; rebuilding is needed for reclamation. Checksums are not authenticity signatures.
