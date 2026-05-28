# PCK Orchestrator v0.1

A thin unifier for separate persistence modules.

## Purpose

The Personal Continuity Kernel daemon (`pckd.py`) stitches separate modules into one continuity loop:

```text
incoming event
→ kernel gate evaluation
→ module routing
→ state update
→ root hash update
→ optional witness/public outbox
```

The kernel does not generate meaning. It arbitrates transitions.

## Files

```text
pckd.py                  daemon/event loop
kernel.py                kernel evaluator + root hash
kernel_rules.json        27 -> 1 rule seed
schema.py                event + state schema helpers
config.json              routing and valve config
modules/
  state_store.py         local append-only state
  witness.py             GitHub/public proof placeholder
  ai_traversal.py        AI compression placeholder
  web_surface.py         public interface placeholder
  garden.py              peer/garden placeholder
events/inbox.jsonl       append events here
state/state.json         current continuity state
state/ledger.jsonl       append-only evaluated records
outbox/                  publishable artifacts/proofs
```

## Run

```bash
python pckd.py --once
```

Add events to `events/inbox.jsonl`, then run again.

