# delete-096-05

Exclude tombstones from results while retaining graph navigation.

Input scale: 96; deterministic random seed: 198.
Run `python scripts/demo.py --case workloads/delete-096-05.case.json`.
The adjacent expected file specifies acceptance conditions independently from the implementation.
A successful run validates these conditions, not a production latency or capacity guarantee.

Inspect `metrics` and `output` in the returned JSON. Increase the input scale only after reading
`docs/LIMITATIONS.md`; do not extrapolate synthetic timing to hardware or external services.
