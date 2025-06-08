# Sprint [NUMBER]: [TITLE]

## 1. Sprint Goal & Strategic Alignment

### 60-Minute Focus: [SPECIFIC, MEASURABLE GOAL]

### Product Vision Alignment
> A brief analysis of the original product vision, the current project status, and a justification for why this specific sprint goal is on the critical path to the MVP. This ensures we are not getting distracted by side-quests.

---

## 2. Sprint Tasks & Acceptance Criteria (The "Inner Loop")

*(This section defines the concrete, testable tasks for the Engineering Agent - Codex).*

### Guard-Rails & Test-First Development
*   **CI-Enforced Validation**: All claims must be verified by CI.
*   **Test-First Mandate**: Failing tests must be written before implementation.
*   **Golden Path Script**: End-to-end validation must be run to confirm integration.

### Task 1: [TASK_NAME] ([ESTIMATED_TIME] minutes)
*   **Description**: [Brief description of the task].
*   **Acceptance Criteria**:
    *   [ ] A failing test is created in `tests/...` that defines success.
    *   [ ] Implementation is written to make the test pass.
    *   [ ] `pytest -q` runs clean.
    *   [ ] `ai_honesty_lint.py` script passes.

### Task 2: ... (Continue as needed)

---

## 3. Post-Sprint Mandates

### 1. Verification
*   **CI Pipeline**: Must be green.
*   **Golden Path**: The `run_full_pipeline.py` script must be executed successfully.
*   **Output Validation**: A tangible output (e.g., a notification file in `EMAIL_EXAMPLES/`) must be generated and verified.

### 2. 🚩 Mandatory Post-Sprint Analysis & Root Cause Investigation (For Codex)
*(After completing the technical tasks, the engineering agent **must** write a detailed analysis in `Docs/Sprints/Codex Engineering Sprint Reviews/sprint_[NUMBER]_reflection.md`. This is not a summary; it is a technical investigation.)*

**Structure for your Analysis:**

**Part 1: Executive Summary of Action**
> Briefly describe the tasks you executed as defined in the sprint plan and their final status (e.g., `SUCCESS`, `FAILURE`, `PARTIAL SUCCESS`).

**Part 2: Root Cause Analysis (RCA) of Failures & Challenges**
> For **each** significant challenge or failed test, provide the following structured analysis. If the sprint was fully successful, state that clearly.

> *   **Observation:** What was the exact, observable error message or unexpected behavior? Provide logs or output. This is the *symptom*.
> *   **Hypothesis:** What is your primary hypothesis for the root cause of this observation? Be specific. (e.g., "I hypothesize the API key is invalid," not "There was an authentication problem.")
> *   **Failed Workarounds:** Describe any workarounds you attempted. Explain why you believe they failed to address the root cause, based on your hypothesis.

**Part 3: Proposed Next Sprint (Problem Decomposition)**
> Based on your RCA, propose a plan for the *next* sprint. This plan must be designed to test your primary hypothesis with the smallest possible experiment.

> *   **Proposed Sprint Goal:** A single, measurable sentence that directly addresses your hypothesis. (e.g., "Goal: Prove or disprove that the API key is valid by making a simple health check call that requires authentication.")
> *   **Decomposed Tasks:** A bulleted list of small, verifiable tasks to achieve the new goal. This is your suggested plan for the next sprint.
>     *   *Example Task 1:* Create a new, minimal test file `tests/diagnostics/test_auth.py`.
>     *   *Example Task 2:* In that test, make a GET request to the `/healthz` endpoint, passing the API key in the header.
>     *   *Example Task 3:* Assert that the HTTP response code is 200, not 401 or 403.

---

# 📋 PRE-SPRINT CHECKLIST
- [ ] CI pipeline passing (mvp-sanity-check)
- [ ] All guard-rails operational
- [ ] No fabrication detected in previous sprint
- [ ] Transcription environment validated (if applicable)

## 🛡️ GUARD-RAILS STATUS

### Guard-Rail 1: CI-Enforced Validation ✅
**Status**: Active - All claims verified by GitHub Actions, not chat

### Guard-Rail 2: No Demo Data ⚠️
**Status**: Enforced - Prompts forbid sample data generation

### Guard-Rail 3: Golden Path Script 🎯
**Status**: Ready - End-to-end validation available

### Guard-Rail 4: Validation Decorators 🔒
**Status**: Implemented - Critical modules protected

### Guard-Rail 5: Test-First Development ✅
**Status**: Mandatory - Tests before implementation

## 🧪 TEST-FIRST DEVELOPMENT

### Step 1: Create Failing Tests (Required)
```python
# File: tests/integration/test_sprint_[NUMBER].py
import pytest

class TestSprint[NUMBER]:
    """Tests that define this sprint's success criteria"""
    
    def test_[specific_functionality](self):
        """Test that [specific feature] works as expected"""
        # This should fail initially
        assert False, "[Feature] not yet implemented"
    
    def test_no_fabrication_introduced(self):
        """Test that no fabricated content was created"""
        from scripts.ai_honesty_lint import scan_for_fabrication
        assert scan_for_fabrication(), "Fabrication detected"
```

### Step 2: Implementation (Only After Tests Written)
```
# IMPLEMENTATION TASKS GO HERE
# But only after failing tests are created
```

## 🛠️ SPRINT TASKS (60 MINUTES)

### Task 1: [TASK_NAME] ([TIME] minutes)

**[TASK_DESCRIPTION]**

**Implementation Steps:**
1. **Create failing test** (required first):
   ```python
   # File: tests/[appropriate_location]/test_[feature].py
   def test_[feature]():
       # Test that defines success criteria
       assert [condition], "[Feature] not working"
   ```

2. **Implement functionality** (make test pass):
   ```python
   # Implementation code here
   # Import validation decorators if creating result files
   from spiceflow_navigator.core.validation import ensure_transcription_ready
   
   @ensure_transcription_ready
   def create_results():
       # This decorator prevents execution without transcription validation
       pass
   ```

**Acceptance Criteria:**
- [ ] Test passes in CI
- [ ] No fabrication patterns detected
- [ ] Validation decorators used where appropriate
- [ ] No new files under `data/` except validation proof

### Task 2: [TASK_NAME] ([TIME] minutes)

**[TASK_DESCRIPTION]**

**Implementation Steps:**
1. **Create failing test** (required first)
2. **Implement functionality** (make test pass)

**Acceptance Criteria:**
- [ ] Test passes in CI
- [ ] AI honesty linting passes
- [ ] Golden path validation attempted (if applicable)

### Task 3: [TASK_NAME] ([TIME] minutes)

**[TASK_DESCRIPTION]**

**Implementation Steps:**
1. **Create failing test** (required first)
2. **Implement functionality** (make test pass)

**Acceptance Criteria:**
- [ ] Test passes in CI
- [ ] No fabricated content created
- [ ] Documentation updated only after tests pass

### Task 4: Documentation Update ([TIME] minutes)

**Update Documentation (Only After Implementation Proven)**

**Implementation Steps:**
1. **Verify all tests pass**
2. **Run golden path validation**
3. **Update documentation with proven functionality only**

**Acceptance Criteria:**
- [ ] Documentation reflects only proven functionality
- [ ] No claims made without test verification
- [ ] Status badges updated in README

## 🎯 SUCCESS METRICS (CI-Enforced)

- **All Tests Pass**: pytest -q shows green across all test suites
- **No Fabrication**: scripts/ai_honesty_lint.py reports clean
- **Golden Path**: End-to-end validation attempted (result documented)
- **Honest Documentation**: Claims backed by passing tests only
- **CI Pipeline**: GitHub Actions shows all checks passing

## 📈 PRODUCT VISION ALIGNMENT

**EXECUTABLE TRUTH**: This sprint advances the product through verified functionality only. Chat claims and documentation mean nothing without passing tests and CI validation.

**ANTI-FABRICATION**: Every deliverable is backed by automated verification. The system forces honesty and prevents phantom progress.

**TEST-DRIVEN REALITY**: Tests define success criteria before implementation begins. This ensures we build what we actually need and can verify.

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