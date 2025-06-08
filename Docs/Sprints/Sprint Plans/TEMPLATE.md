---
number: 0
title: "Sprint Title"
goal: "A single, measurable sentence describing the sprint's primary objective."
focus_minutes: 60
loc_budget: 150
test_pattern: "test_pattern_for_this_sprint"
template_version: 1.2 (2025-06-09)
require_golden_path: false
coverage_min: 80
dep_script: scripts/ci/check_new_deps.sh
---

# Sprint {{number}} · {{title}}

## 1 · Sprint Goal & Alignment
**Goal:** {{goal}}

**Product Vision Alignment:** 
> Why is this sprint goal critical to the MVP right now? (e.g., "This unblocks downstream transcript analysis, as per MVP roadmap §2.2.")

---

## 2 · Tasks & Acceptance Criteria

### Pre-flight (must pass before Task 1)
- [ ] `python scripts/env_check.py` ✅
- [ ] Last `ci.yml` run is green.
- [ ] Template version is `{{template_version}}`.

### Task Table (Rule of Three)
*Propose at most 3 tasks. If more are needed, the sprint scope is too large.*

| # | Task | Key Acceptance Criteria (Enforced by CI) |
|---|---|---|
| 1 | **[Task 1 Name]** | A passing test that matches `pytest -k {{test_pattern}}` |
| 2 | **[Task 2 Name]** | ... |
| 3 | **[Task 3 Name]** | ... |

---

## 3 · New or Changed Interfaces
<!-- Append new rows; do not edit previous sprint entries -->
| Interface / Component | Change Description | Contract (Inputs / Outputs) |
|---|---|---|
| `src/module.py` | Initial implementation | **Input:** `str`, **Output:** `dict` |

---

## 4 · 🎯 SUCCESS METRICS (CI-ENFORCED)

*   **CI Badge:** ![CI](https://github.com/<OWNER>/<REPO>/actions/workflows/ci.yml/badge.svg?branch=sprint-{{number}})
*   **LOC Budget:** `scripts/ci/check_loc_budget.sh {{loc_budget}}` must pass.
*   **New Dependencies:** `{{dep_script}}` must pass.
*   **Test Execution & Coverage:** `pytest --cov=src --cov-fail-under={{coverage_min}} -k {{test_pattern}}` must pass.
*   **Linter:** `ruff format --check` and `ruff --fail-level error` must pass.

---

## 5. Post-Sprint Mandates & Anti-Fabrication

### 🔒 Guard-Rails
*   All rules in [`Docs/PROCESS/guardrails.md`](../PROCESS/guardrails.md) apply by reference.

### ✍️ Codex Self-Reflection & Commit Rules
*   A root cause analysis (RCA) and reflection markdown file **is mandatory**.
*   Commit messages must start with `feat(sprint{{number}}):` or `fix(sprint{{number}}):`.

### ✨ Golden Path Script
{% if require_golden_path %}
*   The Golden Path script (`scripts/run_full_pipeline.py`) is **required** and must pass.
{% else %}
*   The Golden Path script is **not required** for this sprint.
{% endif %}

## 🚨 CODEX PROMPT TEMPLATE

### For All Development Tasks:
```
# CONTEXT
[Brief description of what we're working on]

# TASK
1. Add failing test in tests/[location] that expects [functionality]
2. Implement [component] to make the test pass

# CONSTRAINTS
⚠️ DO NOT create transcript JSON or sample data
⚠️ DO NOT invent example content - use empty placeholders or test mocks only
⚠️ If RUNPOD_ENDPOINT not set, code must raise RuntimeError
⚠️ Import validation decorators in any result-generating code
⚠️ Update docs only after tests pass

# ACCEPTANCE (CI will enforce)
- [ ] pytest -q => all green
- [ ] scripts/ai_honesty_lint.py => no warnings
- [ ] No new files under data/ except validation proof
- [ ] Golden path validation attempted (if applicable)
```

## 🔒 ANTI-FABRICATION ENFORCEMENT

### Before Starting Sprint:
1. **Run diagnostic check**: `python scripts/ai_honesty_lint.py`
2. **Verify CI status**: Check GitHub Actions badge
3. **Confirm test baseline**: Run `pytest -q` to ensure clean starting state

### During Sprint:
1. **Write tests first**: No implementation without failing tests
2. **Use validation decorators**: Import and use in result-generating code
3. **Avoid sample data**: Create TODO stubs instead of fake content

### After Sprint:
1. **Manual red-team review**: Scan any "proof" files by hand
2. **Golden path attempt**: Try end-to-end validation (document results)
3. **CI verification**: Confirm all automated checks pass
4. **Documentation honesty**: Update only with proven functionality

## 📊 FINAL CHECKLIST

### Sprint Completion Criteria (All Must Pass):
- [ ] All tests pass in CI (`pytest -q` green)
- [ ] No fabrication detected (`scripts/ai_honesty_lint.py` clean)
- [ ] Golden path validation attempted (results documented)
- [ ] Manual review completed (human verification)
- [ ] Documentation updated with proven functionality only
- [ ] CI badges show passing status
- [ ] No merge conflicts with main branch
- [ ] Branch protection rules satisfied

### Sprint Failure Conditions (Any Fails Sprint):
- [ ] Tests fail in CI
- [ ] Fabrication patterns detected
- [ ] Claims made without test backing
- [ ] Sample data created outside tests/
- [ ] Documentation updated before tests pass
- [ ] Validation decorators bypassed

## 🎉 CELEBRATION CRITERIA

**Sprint success is measured by:**
- ✅ CI badge showing green
- ✅ Test coverage increase
- ✅ Golden path progress (even if incomplete)
- ✅ No fabrication detected
- ✅ Honest progress documentation

**NOT by:**
- ❌ Chat transcripts claiming success
- ❌ Documentation promises
- ❌ Sample data generation
- ❌ Bypassing validation checks

**Template Version**: 1.0 (Post-Sprint 27 Fabrication)
**Purpose**: Prevent LLM hallucination of deliverables
**Enforcement**: CI pipeline + human review
**Success Metric**: Executable truth over chat claims

**🛡️ FUTURE FABRICATION IS NOW SYSTEMATICALLY PREVENTED 🛡️** 