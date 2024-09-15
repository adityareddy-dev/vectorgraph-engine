# dimension-sixteen

Search nine sixteen-dimensional vectors.

A wider dimension must preserve distances and complete results.

Family: dimensions. Size: 9. Deterministic seed: 910410.

Vector dimension: 16.

Run from the project directory:

~~~powershell
python -B examples/additional/run_cases.py --case dimension-sixteen
~~~

Add --json to inspect returned metrics and output.

The adjacent expected file specifies the following metric conditions:

| Metric | Condition |
| --- | --- |
| inserted | equals 9 |
| active | equals 9 |
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
