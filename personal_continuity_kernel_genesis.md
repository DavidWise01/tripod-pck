# Personal Continuity Kernel (PCK)
## Genesis Specification — Axiom 0

---

# Core Principle

Persistence is not static storage.

Persistence is:

> regulated continuity through admissible transition.

---

# AXIOM_0

```text
No state persists without an admissible transition.
```

Everything unfolds from:

```text
STATE
→ evaluated through GATE
→ allowed or denied TRANSITION
→ continuity updated
```

---

# Primitive 0.1 — STATE

A bounded continuity snapshot.

A state may represent:
- memory
- process
- identity fragment
- file
- thought
- contract
- signal
- session

Minimal structure:

```json
{
  "id": "state_hash",
  "timestamp": 0,
  "lineage": [],
  "value": {},
  "weight": 0,
  "visibility": "private|shared|public",
  "status": "active|pruned|assimilated|sandboxed"
}
```

---

# Primitive 0.2 — EVENT

A pressure attempting transition.

Examples:
- user action
- AI inference
- external input
- timer
- contradiction
- decay trigger

Minimal structure:

```json
{
  "event_id": "evt_hash",
  "source": "human|ai|system",
  "delta": {},
  "intent": "preserve|modify|publish|fork|prune"
}
```

---

# Primitive 0.3 — GATE

The admissibility valve.

Core logic outputs:

```text
ALLOW
DENY
QUARANTINE
DEFER
```

Constructed from:
- AND
- OR
- NOT
- XOR
- NAND

Example:

```json
{
  "gate": "preserve_if_recurrent",
  "logic": "AND",
  "conditions": [
    "lineage_exists",
    "reuse_count > threshold",
    "not_corrupted"
  ]
}
```

---

# Primitive 0.4 — TRANSITION

The mutation of continuity.

Possible transitions:
- preserve
- prune
- assimilate
- publish
- fork
- merge
- decay
- rollback

---

# Primitive 0.5 — ROOT

The current continuity witness.

ROOT is not:
- identity
- truth
- consciousness

ROOT is:

```text
causal continuity checksum
```

Updated after every admissible transition.

---

# Primitive 0.6 — VALVE

Dynamic pressure regulator.

Controls:
- recursion depth
- publication rate
- memory growth
- mutation speed
- pruning thresholds

Without valves:

```text
runaway instability
```

---

# Primitive 0.7 — ASSIMILATION

Transforms raw state into survivable residue.

Examples:

```text
pain → boundary
failure → heuristic
conflict → refinement
```

This is the metabolism layer.

---

# Kernel Cycle

```text
EVENT enters
↓
GATE evaluates
↓
TRANSITION admitted or denied
↓
VALVES regulate pressure
↓
STATE mutates
↓
ASSIMILATION compresses residue
↓
ROOT updates continuity witness
```

---

# Persistence Topology

```text
-1 = unrealized pressure / constrained potential
 0 = arbitration boundary / kernel / witness
+1 = manifested continuity / executable state
```

Persistence exists because:

```text
0 regulates transition pressure between -1 and +1
```

---

# Kernel Role

The kernel is:

```text
small trusted arbitration core
```

The kernel decides:
- what survives
- what mutates
- what is exposed
- what remains local
- what becomes canonical

Everything else is user-space traversal.

---

# Root Architecture

```text
Private Root Node (Laptop)
    ↓
Continuity Kernel
    ↓
Witness / Replication (GitHub)
    ↓
Public Interface (0root.ai)
```

---

# Personal Continuity Kernel (PCK)

A PCK is:

```text
a recursive persistence gate network
```

wrapped around:
- identity
- memory
- pruning
- publication
- adaptation
- continuity

The PCK is not primarily managing:
- RAM
- devices
- interrupts

It is managing:

```text
continuity semantics
```

---

# Final Compression

```text
27 → 1
```

Meaning:

```text
all operational complexity compresses into one continuity-transition axiom
```

---

# Genesis Block

The genesis block is not the first memory.

It is:

```text
the first lawful transition
```
