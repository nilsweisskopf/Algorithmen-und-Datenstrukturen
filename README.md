# Projects SS25

Academic projects from the course **Algorithmen & Datenstrukturen**
B.Sc. Informatik – Albert-Ludwigs-Universität Freiburg
Summer Semester 2025 · ~Nils Weißkopf

---

## Repository Structure

```
Projects SS25/
├── DataStructures/       # SearchTree, HashMap, Priority Queue
└── SortingAlgorithms/    # MergeSort, QuickSort, InsertionSort, BubbleSort, OneSort
```

---

## DataStructures

Implementations of fundamental data structures in Python.

| Project | Description |
|---|---|
| `SearchTree` | Binary Search Tree with recursive lookup |
| `HashMap` | Hash map with collision handling |
| `PriorityQueue` | Priority Queue based on heap structure |

---

## SortingAlgorithms

Implementations of classic sorting algorithms in Python, including runtime analysis.

| Algorithm | Description |
|---|---|
| `MergeSort` | Divide and conquer sorting |
| `QuickSort` | Partition-based recursive sorting |
| `InsertionSort` | Insertion-based sorting |
| `BubbleSort` | Adjacent element comparison sort |
| `OneSort` | Sorting for binary sequences |

---

## Technologies

- **Language:** Python 3
- **Testing:** `doctest`
- **Style:** `flake8`
- **Build:** `make`

---

## Running the Projects

Each project can be run and tested individually:

```bash
# Run tests
make test

# Check code style
make checkstyle

# Clean build artifacts
make clean
```

---

## About

These projects were developed as part of the **Algorithms & Data Structures** course
at the University of Freiburg (SS25).
