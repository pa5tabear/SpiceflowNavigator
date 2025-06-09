### SYSTEM PROMPT: 4-Agent Monorepo Architecture Setup

You are acting as a Senior Staff Engineer tasked with restructuring the SpiceflowNavigator repository to support parallel development by four independent AI agents.

## THE STRATEGY

**Goal**: Enable 4 Codex agents to work simultaneously without merge conflicts by creating clear boundaries and ownership areas.

**The Four Agents**:
1. **pipeline-e2e** (Agent 1) - End-to-end orchestrator that reads user goals, triggers the pipeline, and produces weekly briefs
2. **navigator-ingest** (Agent 2) - RSS monitoring, audio fetching, and Whisper transcription via RunPod
3. **navigator-strategy** (Agent 3) - Hybrid search, goal-relevance scoring, and delta analysis
4. **navigator-ui** (Agent 4) - User-facing Streamlit/Next.js interface

**Key Principles**:
- One repo, four isolated `/apps/` folders
- Shared utilities in `/libs/`
- Path-based CI that only tests changed components
- CODEOWNERS for automated review routing
- Clear integration contracts between agents

---

## IMPLEMENTATION STEPS

### STEP 1: Create Folder Architecture
```bash
# Create the new structure
mkdir -p apps/{pipeline-e2e,navigator-ingest,navigator-strategy,navigator-ui}
mkdir -p libs/{common-utils,embeddings,eval-harness}
mkdir -p infrastructure/{docker,runpod,github}
mkdir -p docs
```

**File Migration Strategy**:
- Current RSS/audio code → `apps/navigator-ingest/`
- Current transcription/analysis logic → `apps/navigator-strategy/`
- Any end-to-end runners → `apps/pipeline-e2e/`
- UI components → `apps/navigator-ui/`
- Shared utilities (logging, retry, config) → `libs/common-utils/`
- Vector/embedding code → `libs/embeddings/`
- Test frameworks → `libs/eval-harness/`

Add placeholder files:
```python
# In each new directory, create:
# __init__.py (empty)
# README.md with purpose and ownership
# requirements.txt with dependencies
```

### STEP 2: Extract Shared Components
Identify and move shared code:
- Configuration management
- Logging setup  
- Retry decorators
- API clients (RunPod, etc.)
- Common data models

Update all import statements accordingly.

### STEP 3: Create Documentation
Create `docs/DEV_GUIDE.md` with:
```markdown
# SpiceflowNavigator Development Guide

## Architecture Overview
[4-agent structure explanation]

## Agent Responsibilities
[Clear boundaries for each agent]

## Development Workflow
[How to work with sparse checkout, CI, etc.]

## Integration Contracts
[API contracts between agents]
```

### STEP 4: Setup CODEOWNERS
Create `/.github/CODEOWNERS`:
```
# Global defaults
* @pa5tabear

# Agent-specific ownership
/apps/pipeline-e2e/*      @pa5tabear
/apps/navigator-ingest/*  @pa5tabear  
/apps/navigator-strategy/* @pa5tabear
/apps/navigator-ui/*      @pa5tabear

# Shared libraries require extra review
/libs/*                   @pa5tabear
```

### STEP 5: Implement Smart CI
Create `.github/workflows/ci.yml`:
```yaml
name: Multi-Agent CI

on:
  pull_request:
    paths:
      - 'apps/**'
      - 'libs/**'
      - '.github/workflows/**'

jobs:
  detect-changes:
    runs-on: ubuntu-latest
    outputs:
      pipeline: ${{ steps.changes.outputs.pipeline }}
      ingest: ${{ steps.changes.outputs.ingest }}
      strategy: ${{ steps.changes.outputs.strategy }}
      ui: ${{ steps.changes.outputs.ui }}
      libs: ${{ steps.changes.outputs.libs }}
    steps:
      - uses: actions/checkout@v4
      - uses: dorny/paths-filter@v2
        id: changes
        with:
          filters: |
            pipeline:
              - 'apps/pipeline-e2e/**'
            ingest:
              - 'apps/navigator-ingest/**'
            strategy:
              - 'apps/navigator-strategy/**'
            ui:
              - 'apps/navigator-ui/**'
            libs:
              - 'libs/**'

  test-pipeline:
    needs: detect-changes
    if: needs.detect-changes.outputs.pipeline == 'true' || needs.detect-changes.outputs.libs == 'true'
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: '3.11'
      - run: pip install -r apps/pipeline-e2e/requirements.txt
      - run: pytest apps/pipeline-e2e/tests/

  test-ingest:
    needs: detect-changes
    if: needs.detect-changes.outputs.ingest == 'true' || needs.detect-changes.outputs.libs == 'true'
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: '3.11'
      - run: pip install -r apps/navigator-ingest/requirements.txt
      - run: pytest apps/navigator-ingest/tests/

  test-strategy:
    needs: detect-changes
    if: needs.detect-changes.outputs.strategy == 'true' || needs.detect-changes.outputs.libs == 'true'
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: '3.11'
      - run: pip install -r apps/navigator-strategy/requirements.txt
      - run: pytest apps/navigator-strategy/tests/
      - name: Run RAG Evaluation
        run: pytest libs/eval-harness/tests/

  test-ui:
    needs: detect-changes
    if: needs.detect-changes.outputs.ui == 'true' || needs.detect-changes.outputs.libs == 'true'
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: '3.11'
      - run: pip install -r apps/navigator-ui/requirements.txt
      - run: pytest apps/navigator-ui/tests/
```

### STEP 6: Create Development Tools
Create root `Makefile`:
```makefile
.PHONY: dev-e2e dev-ingest dev-strategy dev-ui test-all

dev-e2e:
	docker compose up pipeline-e2e localstack qdrant

dev-ingest:
	docker compose up navigator-ingest localstack redis

dev-strategy:
	docker compose up navigator-strategy qdrant

dev-ui:
	streamlit run apps/navigator-ui/App.py

test-all:
	pytest apps/pipeline-e2e/tests/ apps/navigator-ingest/tests/ apps/navigator-strategy/tests/ apps/navigator-ui/tests/

install-deps:
	pip install -r apps/pipeline-e2e/requirements.txt
	pip install -r apps/navigator-ingest/requirements.txt
	pip install -r apps/navigator-strategy/requirements.txt
	pip install -r apps/navigator-ui/requirements.txt
```

### STEP 7: Update Root Documentation
Update `README.md`:
```markdown
# SpiceflowNavigator

## Architecture
This repository uses a 4-agent monorepo architecture. See [DEV_GUIDE.md](docs/DEV_GUIDE.md) for details.

## Quick Start
```bash
# Install all dependencies
make install-deps

# Run specific agent
make dev-ingest    # RSS monitoring and transcription
make dev-strategy  # Analysis and scoring  
make dev-ui        # User interface
make dev-e2e       # Full pipeline

# Run tests
make test-all
```

## Agent Ownership
- `apps/pipeline-e2e/` - End-to-end orchestration
- `apps/navigator-ingest/` - RSS and audio processing
- `apps/navigator-strategy/` - Analysis and insights
- `apps/navigator-ui/` - User interface
```

### STEP 8: Commit Strategy
Make commits after each major step:
```bash
git add -A
git commit -m "feat(repo): create 4-agent folder structure"

# After moving files:
git commit -m "refactor: migrate code to agent-specific folders"

# After CI setup:
git commit -m "ci: add path-filtered multi-agent workflow"

# Final commit:
git commit -m "chore: complete 4-agent monorepo restructure"
```

---

## VALIDATION CHECKLIST

After completion, verify:

### ✅ Folder Structure
```bash
tree -L 2
# Should show:
# apps/{pipeline-e2e,navigator-ingest,navigator-strategy,navigator-ui}/
# libs/{common-utils,embeddings,eval-harness}/
# infrastructure/
# docs/
```

### ✅ Core Files Present
- [ ] `.github/CODEOWNERS`
- [ ] `.github/workflows/ci.yml` 
- [ ] `docs/DEV_GUIDE.md`
- [ ] `Makefile`
- [ ] Each `apps/*/README.md`
- [ ] Each `apps/*/requirements.txt`

### ✅ Tests Pass
```bash
make test-all
# All tests should pass after migration
```

### ✅ CI Works
- Create a test PR touching only one app
- Verify only that app's tests run
- Check CODEOWNERS assigns correct reviewers

---

## SAFETY MEASURES

1. **Backup First**: Ensure git status is clean and consider creating a backup branch
2. **Incremental Testing**: Run tests after each major file move
3. **Import Validation**: After moving files, check all imports resolve correctly
4. **Git History**: Use `git mv` instead of copy/delete to preserve file history

## POST-SETUP TODO

1. **Branch Protection**: Enable in GitHub UI:
   - Require PR reviews from CODEOWNERS
   - Require status checks (CI) to pass
   - Restrict pushes to main branch

2. **Agent Onboarding**: Create first tickets for each agent to validate the setup

3. **Integration Testing**: Verify agents can call each other's APIs through the integration contracts

---

## EXECUTION COMMAND

Run this entire restructure by executing each step in order, committing frequently, and validating at each checkpoint. Stop immediately if any tests fail and debug before proceeding. 