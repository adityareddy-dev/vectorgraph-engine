# Additional scenarios for hnsw-vector-database

Ten runnable scenarios cover small inputs, odd sizes, and behavior boundaries in the existing reference implementation.

This directory contains 10 input JSON files, 10 metric-oracle JSON files, 10 scenario notes, this guide, and the runner (32 files).

Run from the project directory with Python 3.10 or later and the dependencies already listed in requirements.txt.

~~~powershell
python -B examples/additional/run_cases.py --list
python -B examples/additional/run_cases.py
python -B examples/additional/run_cases.py --case uniform-single --json
~~~

The runner exits with zero only when all selected scenarios pass. --json includes metrics and output or a failure reason for each scenario.

Each .case.json is paired with a .expected.json containing equality checks or numeric bounds for the existing syslab.common.check helper.
Scenario notes explain the selected boundaries. Fixed seeds make inputs repeatable; expected files contain assertions rather than recorded timings.

| Scenario | Family | Size | Purpose |
| --- | --- | --- | --- |
| uniform-single | uniform | 1 | Search an index with one vector. |
| uniform-four | uniform | 4 | Search fewer vectors than the requested top-five count. |
| clusters-seven | clusters | 7 | Search seven vectors in three synthetic clusters. |
| duplicates-nine | duplicates | 9 | Search an index with repeated vectors. |
| delete-two | delete | 2 | Delete one vector from a two-vector index. |
| delete-seven | delete | 7 | Delete every fifth identifier from seven vectors. |
| restore-three | restore | 3 | Save and restore a three-vector index. |
| restore-seventeen | restore | 17 | Restore a seventeen-vector index. |
| dimension-one | dimensions | 5 | Search five one-dimensional vectors. |
| dimension-sixteen | dimensions | 9 | Search nine sixteen-dimensional vectors. |

Scope: Small local synthetic indexes and temporary persistence.

Supplemental inputs have their own runner, so the existing workload discovery and its 36-case suite retain their current behavior.
Bytecode generation is disabled. Reports go to standard output; storage and model artifacts use the reference code's temporary directories.

See [limitations](../../docs/LIMITATIONS.md) and [running instructions](../../docs/RUNNING.md).
