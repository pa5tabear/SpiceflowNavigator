# Navigator Strategy Agent

**Owner**: Agent 3 - Analysis and insights  
**Responsibility**: Hybrid search, goal-relevance scoring, and delta analysis

## Purpose
This agent provides intelligent analysis of podcast content:
- Performs hybrid search (cosine + BM25) on transcripts
- Scores content relevance against user goals
- Detects deltas (changes week-over-week)
- Returns top-N snippets with source attributions

## API Contracts
- **Endpoints**: 
  - `POST /score` - Score transcript relevance against goals
- **Input**: Transcripts, user goals
- **Output**: Scored snippets with relevance metrics and attributions
- **Dependencies**: Vector database (Qdrant), embeddings service

## Development
```bash
# Run this agent
make dev-strategy

# Test this agent
pytest apps/navigator-strategy/tests/
``` 