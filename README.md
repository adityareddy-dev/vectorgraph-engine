# Vector Database with HNSW Indexing

A hierarchical graph ANN index implemented from scratch with exact-search comparison, tombstones and checksummed persistence.

## 1. Overview

Approximate nearest-neighbor search trades exact ranking for graph traversal cost. This from-scratch HNSW reference keeps insertion, pruning and query behavior visible, with exhaustive squared-L2 search as a baseline.

**Project type:** educational reference implementation. **Repository contents:** 165 non-empty source, test, configuration, workload and documentation files, including 36 synthetic workload scenarios.

## 2. Core Features — Why They Matter

- **Hierarchical index:** Assigns levels, navigates upper layers and searches with an ef-limited candidate queue.
- **Graph maintenance:** Diversifies/prunes neighbors during insertion and checks degree bounds.
- **Deletion and persistence:** Filters tombstoned IDs and saves checksummed graph state.
- **Exact-search evaluation:** Checks result distances, completeness, recall@5 and tied-vector radius behavior.

## 3. Tech Stack & Architecture

| Layer | Technology | Implementation status |
| --- | --- | --- |
| Execution | Python 3.10+ standard library | Runnable local ANN reference |
| Index and oracle | Custom HNSW graph and exhaustive squared-L2 scan | Implemented locally |
| Persistence and interface | Checksummed JSON state, service class and Protocol Buffers schema | Local service class; no live gRPC transport |

### How the components fit together

The local service class delegates index operations to HNSW layers. Approximate queries use graph navigation while exhaustive search supplies an independent baseline. Persistence records vectors, edges, levels and random-generator state.

| Component | Responsibility |
| --- | --- |
| [src/syslab/hnsw.py](src/syslab/hnsw.py) | Hierarchical insertion, graph pruning and search. |
| [src/syslab/distances.py](src/syslab/distances.py) | Distance calculations. |
| [src/syslab/persistence.py](src/syslab/persistence.py) | Checksummed index save/load. |
| [src/syslab/service.py](src/syslab/service.py) | Local operation service interface. |

See [Architecture](docs/ARCHITECTURE.md) and [Algorithms](docs/ALGORITHMS.md) for implementation notes.

### Scope and limitations

Python reference, not a million-vector production database. No embedding model, concurrency control, compressed vectors or live gRPC transport. proto schema is a design artifact only. Graph links may become asymmetric after per-node degree pruning. Deleted nodes remain in memory; rebuilding is needed for reclamation. Checksums are not authenticity signatures.

## 4. Getting Started / Installation

**Prerequisites:** Python 3.10+. The default reference uses Python's standard library. No API keys or external services are needed for the default sample.

Download/extract this project or clone its repository, then open a terminal in the `hnsw-vector-database` folder. Create an isolated environment:

```sh
python -m venv .venv
```

Activate it on Linux/macOS:

```sh
source .venv/bin/activate
```

Or on Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

Install the declared Python dependencies and run the demo:

```sh
python -m pip install -r requirements.txt
python scripts/demo.py
```

Check behavior and collect timings on your own machine:

```sh
python scripts/run_tests.py
python scripts/benchmark.py
```

The original bundle validation recorded **25 passing tests** for this project and **36 accepted workload scenarios**. These are local reference checks, not production or hardware benchmarks. See [Testing](docs/TESTING.md) and [Benchmark notes](docs/BENCHMARKS.md).

## 5. Usage Examples

### Run a reproducible workload

The bundled [sample request](examples/request.json) contains:

```json
{
  "dimension": 8,
  "family": "uniform",
  "id": "uniform-016-01",
  "seed": 101,
  "size": 16
}
```

Run the corresponding workload and check its independent acceptance conditions:

```sh
python scripts/demo.py --case workloads/uniform-016-01.case.json
```

Expected `metrics` excerpt from the verified local run; the complete JSON also includes `output`:

```json
{
  "metrics": {
    "active": 16,
    "bounded_degree": true,
    "complete_results": true,
    "deleted_excluded": true,
    "distances_correct": true,
    "inserted": 16,
    "max_level": 1,
    "queries": 8,
    "recall_at_5": 1.0,
    "restored_equal": true,
    "within_exact_radius": 1.0
  }
}
```

The example inserts 16 eight-dimensional vectors and runs eight queries, achieving recall@5=1.0 on that small workload. It does not predict recall, throughput or memory use on a large real embedding dataset.

The complete example is in [examples/response.json](examples/response.json). Floating-point last digits can vary across numeric environments.

### Explore through the local dashboard

```sh
python scripts/serve.py --port 8080
```

Open [http://127.0.0.1:8080](http://127.0.0.1:8080), select a workload and choose **Run and check**. The server listens on loopback and is intended for local inspection.

With the server running, a second terminal can call its workload inspection API:

```sh
curl "http://127.0.0.1:8080/api/run?id=uniform-016-01"
```

This endpoint executes the bundled workload; it is not a production domain API.

## 6. Your Contributions / Research Alignment

### Implementation evidence

The following work areas are present in this reference and can be reviewed directly:

| Work area in this reference | Repository evidence |
| --- | --- |
| Hierarchical index | [src/syslab/hnsw.py](src/syslab/hnsw.py) |
| Correctness and edge cases | [tests/](tests/) and [acceptance workloads](workloads/) |
| Reproducible evaluation | [scripts/demo.py](scripts/demo.py), [scripts/benchmark.py](scripts/benchmark.py), [testing notes](docs/TESTING.md) |

### Research alignment

The project connects information retrieval, graph algorithms and database implementation. It can support an MS research discussion about the relation between graph structure, query work, recall and storage cost.

**A question to investigate:** How do neighbor degree and search breadth change the recall/latency/memory tradeoff as vector count and dimensionality grow?

This question is a proposed extension, not a completed research result. Evaluate it with controlled inputs, independent correctness checks and measurements tied to a reproducible configuration.

### Personal contribution record

This reference was generated from the supplied project concept. Personal authorship or research contributions have not been verified. For an MS application, document only the modules you actually changed, the design choices you can explain, and experiments you ran; link those claims to commits or reproducible reports. See [Provenance](docs/PROVENANCE.md).

All bundled inputs are synthetic. The repository does not establish historical development dates, prior deployment or published research.
