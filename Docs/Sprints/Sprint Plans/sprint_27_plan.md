---
number: 27
title: "Scale Up to 10-Minute Podcast Chunks"
goal: "Generate and commit 10-minute transcript chunks to prove scalability beyond 30-second proof-of-concept."
focus_minutes: 90
loc_budget: 100
test_pattern: "test_ten_minute"
template_version: 1.2 (2025-06-09)
require_golden_path: false
coverage_min: 80
dep_script: scripts/ci/check_new_deps.sh
---

# Sprint 27 · Scale Up to 10-Minute Podcast Chunks

## 1 · Sprint Goal & Alignment
**Goal:** Generate and commit 10-minute transcript chunks to prove scalability beyond 30-second proof-of-concept.

**Product Vision Alignment:** 
> Sprint 26 proved our transcription pipeline works with real audio. Now we need to demonstrate it can handle meaningful chunks that would be useful for actual analysis and summarization - the core MVP value proposition.

---

## 2 · Tasks & Acceptance Criteria

### Pre-flight (must pass before Task 1)
- [ ] `python scripts/env_check.py` ✅
- [ ] Last `ci.yml` run is green.
- [ ] Template version is `1.2 (2025-06-09)`.

### Task Table (Rule of Three)
*Propose at most 3 tasks. If more are needed, the sprint scope is too large.*

| # | Task | Key Acceptance Criteria (Enforced by CI) |
|---|---|---|
| 1 | **Extend chunk_and_transcribe.py for 10-minute clips** | A passing test that validates 10-minute HTTP range requests using `pytest -k test_ten_minute_range` |
| 2 | **Generate 10-minute transcript from Shift Key** | Successfully create `transcripts/shift_key/latest_10min.json` with substantial content (>500 words) |
| 3 | **Add runtime validation for transcript quality** | Implement and test validation that ensures transcript contains meaningful content, not just silence or errors |

---

## 3 · New or Changed Interfaces
<!-- Append new rows; do not edit previous sprint entries -->
| Interface / Component | Change Description | Contract (Inputs / Outputs) |
|---|---|---|
| `scripts/chunk_and_transcribe.py` | Add 10-minute chunk support | **Input:** `--duration 600`, **Output:** transcript JSON with 10-minute content |
| `src/validation/transcript_validator.py` | New transcript quality validation | **Input:** transcript dict, **Output:** bool (valid/invalid) |

---

## 4 · 🎯 SUCCESS METRICS (CI-ENFORCED)

*   **CI Badge:** ![CI](https://github.com/pa5tabear/SpiceflowNavigator/actions/workflows/ci.yml/badge.svg?branch=sprint-27)
*   **LOC Budget:** `scripts/ci/check_loc_budget.sh 100` must pass.
*   **New Dependencies:** `scripts/ci/check_new_deps.sh` must pass.
*   **Test Execution & Coverage:** `pytest --cov=src --cov-fail-under=80 -k test_ten_minute` must pass.
*   **Linter:** `ruff format --check` and `ruff --fail-level error` must pass.

---

## 5. Post-Sprint Mandates & Anti-Fabrication

### 🔒 Guard-Rails
*   All rules in [`Docs/PROCESS/guardrails.md`](../../PROCESS/guardrails.md) apply by reference.
*   ---
*   **🚨 CRITICAL: DO NOT COMMIT BINARY FILES (.mp3, .wav, etc.) 🚨**
*   **YOUR PULL REQUEST WILL BE REJECTED IF IT CONTAINS BINARY ASSETS.**
*   **You MUST use fixtures already present in the repository or add new text-based stubs.**
*   ---

### ✍️ Codex Self-Reflection & Commit Rules
*   A root cause analysis (RCA) and reflection markdown file **is mandatory**.
*   Commit messages must start with `feat(sprint27):` or `fix(sprint27):`.

### ✨ Golden Path Script
*   The Golden Path script is **not required** for this sprint.

## 🚨 CODEX PROMPT TEMPLATE

### For All Development Tasks:
```
# CONTEXT
Building on Sprint 26's success with 30-second transcripts, scaling up to 10-minute chunks for real-world utility

# TASK
1. Add failing test in tests/[location] that expects 10-minute chunk functionality
2. Implement chunking logic to handle 10-minute HTTP ranges
3. Generate real 10-minute transcript from Shift Key podcast

# CONSTRAINTS
⚠️ Use real audio from RSS feed - no mock content for final transcript
⚠️ If RUNPOD_ENDPOINT not set, code must raise RuntimeError
⚠️ Implement transcript validation to ensure quality output
⚠️ Update docs only after tests pass

# ACCEPTANCE (CI will enforce)
- [ ] pytest -q => all green
- [ ] Real 10-minute transcript committed to transcripts/shift_key/
- [ ] Transcript contains >500 words of meaningful content
- [ ] No fabricated or sample data - use real podcast audio
```

## 🔒 ANTI-FABRICATION ENFORCEMENT

### Before Starting Sprint:
1. **Run diagnostic check**: `python scripts/ai_honesty_lint.py`
2. **Verify CI status**: Check GitHub Actions badge
3. **Confirm test baseline**: Run `pytest -q` to ensure clean starting state

### During Sprint:
1. **Write tests first**: No implementation without failing tests
2. **Use real audio sources**: HTTP range requests from actual RSS feeds
3. **Validate transcript quality**: Ensure substantial, meaningful content

### After Sprint:
1. **Manual red-team review**: Verify transcript contains real podcast content
2. **Golden path attempt**: Try end-to-end validation (document results)
3. **CI verification**: Confirm all automated checks pass
4. **Documentation honesty**: Update only with proven functionality

## 📊 FINAL CHECKLIST

### Sprint Completion Criteria (All Must Pass):
- [ ] All tests pass in CI (`pytest -q` green)
- [ ] Real 10-minute transcript file committed and contains >500 words
- [ ] No fabrication detected (`scripts/ai_honesty_lint.py` clean)
- [ ] Transcript validation logic implemented and tested
- [ ] Documentation updated with proven functionality only
- [ ] CI badges show passing status
- [ ] No merge conflicts with main branch
- [ ] Branch protection rules satisfied

### Sprint Failure Conditions (Any Fails Sprint):
- [ ] Tests fail in CI
- [ ] Transcript is fabricated, empty, or <500 words
- [ ] Claims made without test backing
- [ ] Sample data created instead of real transcripts
- [ ] Documentation updated before tests pass
- [ ] Validation checks bypassed

## 🎉 CELEBRATION CRITERIA

**Sprint success is measured by:**
- ✅ CI badge showing green
- ✅ Real 10-minute transcript demonstrating scalability
- ✅ Test coverage for chunking logic
- ✅ Quality validation preventing poor transcripts
- ✅ Honest progress documentation

**NOT by:**
- ❌ Chat transcripts claiming success
- ❌ Documentation promises
- ❌ Mock or sample transcript data
- ❌ Bypassing quality validation checks

**Template Version**: 1.2 (2025-06-09)
**Purpose**: Scale proven capability to useful chunk sizes
**Enforcement**: CI pipeline + transcript quality validation
**Success Metric**: Real 10-minute transcript with >500 words 