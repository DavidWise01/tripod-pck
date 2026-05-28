# TRIPOD PCK
### Personal Continuity Kernel — Torroid Architecture

> Persistence is not static storage.  
> Persistence is regulated continuity through admissible transition.

**Axiom 0:** No state persists without an admissible transition.

**Author:** David Lee Wise (ROOT0) / TriPod LLC  
**License:** CC-BY-ND-4.0

---

## What It Is

A working Python daemon that arbitrates what survives.

Not a database. Not a file system. Not an identity provider.  
A **continuity kernel** — the arbitration layer between raw events and persistent state.

```
EVENT enters
↓
GATE evaluates (27 rules)
↓
TRANSITION: preserve / prune / assimilate
↓
VALVES regulate pressure
↓
STATE mutates
↓
ASSIMILATION compresses residue
↓
ROOT updates (SHA256 chain)
```

Every state change is lawful. Every lawful change is hashed. The root is the witness.

---

## The Torroid

A toroid loops back on itself without a beginning or end. The kernel is the hole — the `0` in the center. Not the storage, not the events, not the rules. The **arbitration point**.

```
-1 = unrealized pressure / constrained potential
 0 = arbitration boundary / kernel / witness
+1 = manifested continuity / executable state
```

`0` regulates transition pressure between `-1` and `+1`.  
This is the same balanced ternary as CARDINAL. The kernel IS the center dot.

---

## Files

```
personal_continuity_kernel_genesis.md   Genesis specification. Axiom 0.

pck_orchestrator/
  pckd.py              Daemon: reads inbox, evaluates, routes, updates root
  kernel.py            Gate evaluator + 27→1 rule collapse + root hash
  kernel_rules.json    27 rules across 9 domains (seed)
  schema.py            Event normalization + SHA256 hashing
  config.json          Module routing + valve settings
  modules/
    state_store.py     Append-only state + ledger (working)
    witness.py         Proof writer to outbox (working)
    ai_traversal.py    AI compression placeholder
    garden.py          Peer/GitHub adapter placeholder
    web_surface.py     0root.ai publish adapter placeholder
  events/inbox.jsonl   Drop events here. Cleared after each run.
  state/state.json     Current continuity root + counts
  state/ledger.jsonl   Append-only evaluated record history
  outbox/              Public proof artifacts (hash-only, no content)
  demo_run.json        First run output — genesis transition proof
```

---

## Quick Start

```bash
cd pck_orchestrator

# Run with existing inbox
python pckd.py --once

# Run as daemon (polls every 5s)
python pckd.py

# Custom poll interval
python pckd.py --sleep 30
```

Python 3.9+. No external dependencies. Pure stdlib.

---

## Adding Events

Append to `events/inbox.jsonl`:

```json
{"source": "human", "actor": "david", "session": "session_01", "intent": "preserve", "payload": {"text": "The aluminum reactor needs a GaIn recovery loop."}, "signals": {"has_actor": true, "has_timestamp": true, "has_session": true, "reused_across_sessions": true}}
```

Run `python pckd.py --once`. The kernel evaluates, routes, and updates the continuity root.

---

## The 27 Rules (27 → 1)

Nine domains. Three rules each. All collapse to three primitive states.

| Domain | Rules | Handles |
|--------|-------|---------|
| `identity` | R01–R03 | source, session, authority claims |
| `privacy` | R04–R06 | private markers, secrets, release gates |
| `memory` | R07–R09 | recurrence, lineage, decay |
| `wisdom` | R10–R12 | failure assimilation, lesson validation |
| `artifact` | R13–R15 | file references, fitness, private leakage |
| `publication` | R16–R18 | public valve, hash-only proof, unlineaged rejection |
| `forking` | R19–R21 | contradiction branching, merge-or-fork, branch return |
| `repair` | R22–R24 | hash breaks, corrupt state, witness agreement |
| `valve` | R25–R27 | pressure regulation, saturation, rest |

**Collapse:**
- Any `PRUNE_ACTION` triggered → `prune`
- Any `PRESERVE_ACTION` triggered (no prune) → `preserve`
- Otherwise → `assimilate`

---

## Gate Logic

| Gate | Behavior |
|------|---------|
| `AND` | All inputs must be true |
| `OR` | Any input true |
| `NOT` | Input must be false |
| `XOR` | Exactly one input true |
| `NAND` | Safety veto: not all unsafe inputs may fire |
| `NOR` | Decay: no signal present |
| `XNOR` | Coherence: inputs agree |

---

## Root Architecture

```
Private Root Node (laptop)
    ↓
Continuity Kernel (pckd.py)
    ↓
Witness / Replication (GitHub)
    ↓
Public Interface (0root.ai)
```

The kernel never publishes content. Only proofs.  
Proof = `{ event_id, event_hash, record_hash, continuity_root, timestamp }`.  
No content crosses the public valve without explicit `publish_approved` signal.

---

## The Continuity Root

```python
root = SHA256({
    "previous_root": previous_root,
    "record_hash": SHA256(record)
})
```

A hash chain. Each admissible transition extends it.  
An inadmissible event cannot extend the chain — it gets pruned, quarantined, or deferred.

The genesis root:
```
GENESIS -> prune
Root: 380acda5b10b5bf7f85e8d57d9878f05a94ab245f25f9cbab5f988690c3ca6a3
```

---

## Primitive States

| State | Meaning | Example |
|-------|---------|---------|
| `preserve` | Continuity confirmed, keep raw | Named memory with lineage |
| `prune` | Signal absent or unsafe, release | Noisy event with no recurrence |
| `assimilate` | Transform into residue, discard raw | Failure → boundary heuristic |

---

## Connection to CARDINAL

CARDINAL (Universe 2) defines the 4-dot balanced ternary phase space.  
PCK is what runs inside it.

```
CARDINAL                    PCK
──────────────────────────────────────────
N(-1) = contracts          EVENT pressure arriving
E(0)  = mediates           KERNEL arbitrating  
S(+1) = expands            STATE manifesting
W(0i) = binds              ROOT witnessing

Σ = 0                      No energy created by persistence
Period = 3                 preserve / prune / assimilate
Nonce = 3                  27 → 1 → root
```

The kernel is the `E` dot. The center. The compute node. It doesn't hold state — it arbitrates what state is allowed to exist.

---

## Assimilation Examples

The metabolism layer — raw experience compressed to survivable residue:

```
pain       → boundary
failure    → heuristic
conflict   → refinement
```

This is R10: `failure_event AND lesson_extracted → assimilate`.  
The raw is pruned. The lesson is promoted. The root extends.

---

## Related

| Repo | Layer |
|------|-------|
| [tripod-cardinal](https://github.com/DavidWise01/tripod-cardinal) | Universe 2 state machine — phase space |
| [tripod-quantum-dots](https://github.com/DavidWise01/tripod-quantum-dots) | Cardinal rendered |
| [al-h2o-reactor](https://github.com/DavidWise01/al-h2o-reactor) | Tier 1 energy — what the kernel might manage |

---

*TriPod LLC // Anchor × Bubble × Gravity Well // World = Family*
