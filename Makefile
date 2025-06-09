.PHONY: dev-e2e dev-ingest dev-strategy dev-ui test-all install-deps clean help

# Default target
help:
	@echo "SpiceflowNavigator Development Commands"
	@echo "======================================"
	@echo ""
	@echo "Development:"
	@echo "  dev-e2e        Run pipeline-e2e agent (end-to-end orchestration)"
	@echo "  dev-ingest     Run navigator-ingest agent (RSS monitoring and transcription)"
	@echo "  dev-strategy   Run navigator-strategy agent (analysis and scoring)"
	@echo "  dev-ui         Run navigator-ui agent (user interface)"
	@echo ""
	@echo "Testing:"
	@echo "  test-all       Run all tests across all agents"
	@echo "  test-pipeline  Run pipeline-e2e tests only"
	@echo "  test-ingest    Run navigator-ingest tests only"
	@echo "  test-strategy  Run navigator-strategy tests only"
	@echo "  test-ui        Run navigator-ui tests only"
	@echo ""
	@echo "Setup:"
	@echo "  install-deps   Install all dependencies for all agents"
	@echo "  clean          Clean up temporary files and caches"

# Development targets
dev-e2e:
	@echo "Starting pipeline-e2e agent..."
	@echo "Note: Docker compose configuration needed for full setup"
	cd apps/pipeline-e2e && python run_workflow.py

dev-ingest:
	@echo "Starting navigator-ingest agent..."
	@echo "Note: Docker compose configuration needed for full setup"
	cd apps/navigator-ingest && python run_transcription_job.py

dev-strategy:
	@echo "Starting navigator-strategy agent..."
	@echo "Note: Docker compose configuration needed for Qdrant"
	@echo "Strategy agent requires vector database setup"

dev-ui:
	@echo "Starting navigator-ui agent..."
	@echo "Note: Streamlit app not yet implemented"
	@echo "Future: streamlit run apps/navigator-ui/App.py"

# Testing targets
test-all:
	@echo "Running all tests..."
	pytest apps/pipeline-e2e/tests/ apps/navigator-ingest/tests/ apps/navigator-strategy/tests/ apps/navigator-ui/tests/ libs/eval-harness/tests/ -v

test-pipeline:
	@echo "Running pipeline-e2e tests..."
	pytest apps/pipeline-e2e/tests/ -v

test-ingest:
	@echo "Running navigator-ingest tests..."
	pytest apps/navigator-ingest/tests/ -v

test-strategy:
	@echo "Running navigator-strategy tests..."
	pytest apps/navigator-strategy/tests/ -v
	@if [ -d "libs/eval-harness/tests" ]; then \
		echo "Running RAG evaluation tests..."; \
		pytest libs/eval-harness/tests/ -v; \
	fi

test-ui:
	@echo "Running navigator-ui tests..."
	pytest apps/navigator-ui/tests/ -v

# Setup targets
install-deps:
	@echo "Installing dependencies for all agents..."
	pip install -r apps/pipeline-e2e/requirements.txt
	pip install -r apps/navigator-ingest/requirements.txt
	pip install -r apps/navigator-strategy/requirements.txt
	pip install -r apps/navigator-ui/requirements.txt
	@echo "All dependencies installed successfully"

clean:
	@echo "Cleaning up temporary files..."
	find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name ".pytest_cache" -exec rm -rf {} + 2>/dev/null || true
	find . -type f -name "*.pyc" -delete 2>/dev/null || true
	find . -type f -name "*.pyo" -delete 2>/dev/null || true
	find . -type f -name ".coverage" -delete 2>/dev/null || true
	@echo "Cleanup complete"

# Docker development (future)
docker-dev-e2e:
	@echo "Future: docker compose up pipeline-e2e localstack qdrant"

docker-dev-ingest:
	@echo "Future: docker compose up navigator-ingest localstack redis"

docker-dev-strategy:
	@echo "Future: docker compose up navigator-strategy qdrant" 