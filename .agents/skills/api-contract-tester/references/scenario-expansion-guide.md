# Scenario Expansion Guide

Catalog rows (e.g. `FUNC-012`) are **design prompts**, not executed tests. Before reporting PASS:

1. **Select** scenarios that match release scope and risk (document N/A with reason).
2. **Decompose** each selected row into atomic test cases with unique IDs (`FUNC-012a`, `FUNC-012b`, …).
3. **Apply variants** where relevant:
   - Valid and invalid inputs
   - Min/max/boundary values
   - Repeat and double-submit
   - Interrupt/cancel mid-flow
   - Concurrent or multi-user access (if applicable)
4. **Define an independent oracle** (expected result not copied from implementation comments alone).
5. **Capture evidence**: command, log excerpt, screenshot reference, API response (redacted), DB/file state.
6. **Record status** in the execution matrix; use NOT TESTED or BLOCKED if not run.

Document expansions in the test design table—do not rely on the catalog row alone.
