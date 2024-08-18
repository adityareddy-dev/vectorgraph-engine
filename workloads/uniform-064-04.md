# uniform-064-04

Index uniformly sampled vectors and compare nearest neighbors to brute force.

Input scale: 64; deterministic random seed: 104.
Run `python scripts/demo.py --case workloads/uniform-064-04.case.json`.
The adjacent expected file specifies acceptance conditions independently from the implementation.
A successful run validates these conditions, not a production latency or capacity guarantee.

Inspect `metrics` and `output` in the returned JSON. Increase the input scale only after reading
`docs/LIMITATIONS.md`; do not extrapolate synthetic timing to hardware or external services.
