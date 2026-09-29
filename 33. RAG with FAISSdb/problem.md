# Choose FAISS if you have the following needs

Extreme speed requirements: Need maximum throughput for vector retrieval (e.g., millions to tens of millions of vectors, millisecond-level latency)

Deep R&D or custom development: Want full control over the underlying indexing algorithms (IVF, HNSW, PQ, etc.), not afraid to write code to manage storage and ID mappings yourself

Just need an "engine": Your application already has a database (like PostgreSQL, SQLite), and you only want to embed a high-performance similarity search module

# What I was doing wrong & how to fix it

---

## ❌ Problem 1: Import ran the whole build pipeline

**What I did:**

```python
from pdf_create_vector import vector_store, embeddings
```

**Why it's wrong:**

- Importing a file runs **all top-level code** in it
- `pdf_create_vector.py` had: read PDF → split → embed via API → build FAISS → save to disk
- So every time I ran the agent, it **rebuilt the entire vector DB** — wasted API calls, wasted time, wasted money
- Then I immediately did `load_local(...)` — loading the DB I just built. Literally did the work twice.

**Mental rule:** *Import = execute. If a file does work at top level, importing it does that work.*

---

## ❌ Problem 2: `load_dotenv()` called twice

**What I did:**

- Called it in `pdf_agent.py`
- Imported `pdf_create_vector` which also called it

**Why it's wrong:**

- Redundant (harmless, but sloppy)
- Import already triggers the other file's `load_dotenv()`

---

## ❌ Problem 3: Mixed two jobs in one file

**What I did:**

- `pdf_create_vector.py` both **builds** the DB *and* **exposes** it as a module

**Why it's wrong:**

- Build = run once (script)
- Expose = import anytime (module)
- Mixing them means I can't import without rebuilding

---

## ❌ Problem 4: `load_local` used on existing instance

```python
vector_store.load_local(...)   # mutates instance
```

**Better form:**

```python
vector_store = FAISS.load_local(...)   # returns new store
```

Idiomatic. Class method, not instance method.

---

## ❌ Problem 5: `temperature=1` for a RAG Q&A bot

- High temp = creative, drifts from context
- For "answer only from context" → use `0` to `0.3`

---

## ❌ Problem 6: Inconsistent DB folder path

- `./vectorsdb` in some files, `./VectorDB` in others
- Agent loads from a path the builder didn't save to → silent failure

---

## ✅ Solution — Option B (separate concerns)

## Three files, one job each

| File | Job | Run when |
|---|---|---|
| `build_vector.py` | Read PDF → chunk → embed → save to disk | **Once**, manually |
| `embeddings.py` | Just create & export the `embeddings` object | Imported |
| `agent.py` | Import `embeddings`, **load** store, chat loop | Every run |

---

## Key principles to remember

1. **Build ≠ Load.** Build once. Load always.
2. **Import = execute.** Never let import trigger heavy work.
3. **One job per file.** Build script ≠ module ≠ agent.
4. **`if __name__ == "__main__":`** guards script-only code.
5. **Config in one place.** Path + model name → constant or env var.
6. **Import only what's cheap.** `embeddings` is cheap. `vector_store` (fresh build) is not.
7. **`load_local` returns a store.** Assign it, don't call it on an instance.
8. **RAG temp low.** `0`–`0.3`.

---

## The flow after fix

```
build_vector.py  →  runs once  →  saves to ./vectorsdb
                                        ↓
agent.py  →  imports embeddings  →  loads ./vectorsdb  →  chat
```

Agent never rebuilds. Only loads. Build is a separate, deliberate action.

---

## One-line recall

> **Build once in a script, load always in the agent, never let import do heavy work.**
