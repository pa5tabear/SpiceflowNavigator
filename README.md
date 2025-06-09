# SpiceflowNavigator

**A 4-Agent Podcast Intelligence Pipeline**

## Architecture

SpiceflowNavigator uses a **4-agent monorepo architecture** designed to enable parallel development by independent AI agents without merge conflicts. See [DEV_GUIDE.md](docs/DEV_GUIDE.md) for detailed development information.

### Agent Overview

- **`apps/pipeline-e2e/`** - End-to-end orchestration and workflow management
- **`apps/navigator-ingest/`** - RSS monitoring, audio fetching, and transcription
- **`apps/navigator-strategy/`** - Content analysis, goal-relevance scoring, and insights
- **`apps/navigator-ui/`** - User interface for goals, briefs, and visualizations

## Quick Start

### Prerequisites
- Python 3.11+
- Virtual environment recommended
- RunPod API access for transcription

### Installation
```bash
# Clone and setup
git clone <repository-url>
cd SpiceflowNavigator

# Create virtual environment
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install all dependencies
make install-deps

# Set required environment variables
export RUNPOD_ENDPOINT="your-runpod-endpoint"
export RUNPOD_API_KEY="your-api-key"
```

### Development Commands
```bash
# Run specific agents
make dev-ingest    # RSS monitoring and transcription
make dev-strategy  # Analysis and scoring  
make dev-ui        # User interface
make dev-e2e       # Full pipeline

# Run tests
make test-all      # All tests
make test-ingest   # Specific agent tests
make test-strategy
make test-ui
make test-pipeline

# Utilities
make clean         # Clean temporary files
make help          # Show all available commands
```

## Core Functionality

The system performs podcast intelligence through a multi-agent pipeline:

1. **RSS Monitoring** (navigator-ingest) - Monitors configured podcast feeds for new episodes
2. **Audio Transcription** (navigator-ingest) - Downloads and transcribes audio via RunPod/Whisper
3. **Content Analysis** (navigator-strategy) - Analyzes transcripts against user-defined goals
4. **Insight Generation** (navigator-strategy) - Scores relevance and detects content deltas
5. **Brief Creation** (pipeline-e2e) - Compiles insights into weekly markdown briefs
6. **User Interface** (navigator-ui) - Presents results and collects feedback

## Configuration

### RSS Feeds
Configure monitored podcasts in `config/rss_feeds.yml`:
```yaml
feeds:
  - name: "Shift Key"
    url: "https://feeds.simplecast.com/oA0B8h1g"
    strategic_importance: 9
  - name: "Open Circuit"  
    url: "https://feeds.megaphone.fm/opencircuit/"
    strategic_importance: 8
```

### User Goals
Define analysis goals in `Goals/*.md` files:
```markdown
# Investment Thesis: Clean Energy Storage

## Key Topics
- Battery technology breakthroughs
- Grid-scale storage deployment
- Policy impacts on storage markets

## Success Metrics
- Identify 3+ investment opportunities per quarter
- Track regulatory changes affecting storage
```

## Development Principles

This project maintains strict engineering principles:

1. **Agent Isolation** - Each agent works independently in its assigned folder
2. **Test-Driven Development** - No feature complete without passing tests
3. **Path-Filtered CI** - Only test components that changed
4. **Clear Integration Contracts** - Well-defined APIs between agents
5. **Token Budget Management** - Efficient use of AI agent context windows

## Testing

```bash
# Run all tests
make test-all

# Run specific test suites
pytest apps/navigator-ingest/tests/     # Ingestion tests
pytest apps/navigator-strategy/tests/   # Analysis tests
pytest libs/eval-harness/tests/         # RAG evaluation tests

# Integration tests
pytest apps/pipeline-e2e/tests/integration/
```

## Contributing

### For AI Agents
1. **Choose your agent** - Review responsibilities in [DEV_GUIDE.md](docs/DEV_GUIDE.md)
2. **Setup sparse checkout** - Only work on your assigned folders
3. **Follow naming conventions** - Branch names: `<agent>/<ticket-id>/<description>`
4. **Respect boundaries** - Don't edit other agents' code
5. **Test thoroughly** - Run your agent's tests before submitting PRs

### Branch Protection
- All PRs require review from CODEOWNERS
- CI must pass before merging
- Main branch is protected from direct pushes

## Architecture Decisions

- **Monorepo over microservices** - Simpler development and deployment
- **Path-based CI** - Efficient testing of only changed components  
- **Agent isolation** - Prevents merge conflicts in parallel development
- **Shared libraries** - Common utilities without duplication
- **Integration contracts** - Clear APIs enable independent development

## License

[License information]

## Support

- **Development Guide**: [docs/DEV_GUIDE.md](docs/DEV_GUIDE.md)
- **Agent Documentation**: See individual `apps/*/README.md` files
- **Issues**: Use GitHub issues with appropriate agent labels 