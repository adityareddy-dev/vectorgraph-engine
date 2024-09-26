# delete-two

Delete one vector from a two-vector index.

Return the remaining vector and exclude the deleted identifier.

Family: delete. Size: 2. Deterministic seed: 910405.

Run from the project directory:

~~~powershell
python -B examples/additional/run_cases.py --case delete-two
~~~

Add --json to inspect returned metrics and output.

The adjacent expected file specifies the following metric conditions:

| Metric | Condition |
| --- | --- |
| inserted | equals 2 |
| active | equals 1 |
| queries | equals 8 |
| distances_correct | equals true |
| deleted_excluded | equals true |
| bounded_degree | equals true |
| complete_results | equals true |
| restored_equal | equals true |
| recall_at_5 | min 0, max 1 |
| within_exact_radius | min 0, max 1 |

Scope: Small local synthetic indexes and temporary persistence.

These inputs are synthetic. See [project limitations](../../docs/LIMITATIONS.md).
