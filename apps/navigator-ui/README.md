# Navigator UI Agent

**Owner**: Agent 4 - User interface  
**Responsibility**: User-facing Streamlit/Next.js interface

## Purpose
This agent provides the user interface for SpiceflowNavigator:
- Upload and manage user goals
- Display weekly briefs and insights
- Show relevance heatmaps and visualizations
- Collect user feedback
- (Future) Authentication and billing

## API Contracts
- **Interface**: Web-based UI (Streamlit MVP)
- **Dependencies**: pipeline-e2e gRPC API or direct REST calls to ingest/strategy
- **Output**: Interactive web interface

## Development
```bash
# Run this agent
make dev-ui

# Test this agent
pytest apps/navigator-ui/tests/
``` 