# dimensions-064-04

Vary vector dimension as well as collection size.

Input scale: 64; deterministic random seed: 259.
Run `python scripts/demo.py --case workloads/dimensions-064-04.case.json`.
The adjacent expected file specifies acceptance conditions independently from the implementation.
A successful run validates these conditions, not a production latency or capacity guarantee.

Inspect `metrics` and `output` in the returned JSON. Increase the input scale only after reading
`docs/LIMITATIONS.md`; do not extrapolate synthetic timing to hardware or external services.
