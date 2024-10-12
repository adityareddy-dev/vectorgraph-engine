# uniform-single

Search an index with one vector.

Top-five queries return the only active vector.

Family: uniform. Size: 1. Deterministic seed: 910401.

Run from the project directory:

~~~powershell
python -B examples/additional/run_cases.py --case uniform-single
~~~

Add --json to inspect returned metrics and output.

The adjacent expected file specifies the following metric conditions:

| Metric | Condition |
| --- | --- |
| inserted | equals 1 |
| active | equals 1 |
| queries | equals 8 |
| distances_correct | equals true |
| deleted_excluded | equals true |
| bounded_degree | equals true |
| complete_results | equals true |
| restored_equal | equals true |
| recall_at_5 | equals 1 |
| within_exact_radius | equals 1 |

Scope: Small local synthetic indexes and temporary persistence.

These inputs are synthetic. See [project limitations](../../docs/LIMITATIONS.md).
