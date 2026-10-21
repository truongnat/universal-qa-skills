# Scenario Expansion Guide

Catalog rows (e.g. `FUNC-012`) are **design prompts**, not executed tests. Before reporting PASS:

1. **Select** scenarios that match release scope and risk (document N/A with reason). Link each to a **risk ID** (`risk-based-testing.md`).
2. **Decompose** each selected row into atomic test cases with unique IDs (`FUNC-012a`, `FUNC-012b`, …). Name the **technique** (e.g. BVA, state transition, exploratory charter).
3. **Apply variants** where relevant:
   - Valid and invalid inputs
   - Min/max/boundary values
   - Repeat and double-submit
   - Interrupt/cancel mid-flow
   - Concurrent or multi-user access (if applicable)
4. **Define an independent oracle** (FEW HICCUPPS may *suggest* issues; confirm with spec, contract, or domain rule before CONFIRMED).
5. **Capture evidence**: command, log excerpt, screenshot reference, API response (redacted), DB/file state.
6. **Record status** in the execution matrix; use NOT TESTED or BLOCKED if not run.

Document expansions in the test design table—do not rely on the catalog row alone.
