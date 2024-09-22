# uniform-four

Search fewer vectors than the requested top-five count.

Every query must return exactly four active neighbors.

Family: uniform. Size: 4. Deterministic seed: 910402.

Run from the project directory:

~~~powershell
python -B examples/additional/run_cases.py --case uniform-four
~~~

Add --json to inspect returned metrics and output.

The adjacent expected file specifies the following metric conditions:

| Metric | Condition |
| --- | --- |
| inserted | equals 4 |
| active | equals 4 |
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
