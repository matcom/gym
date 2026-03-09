.PHONY: test

test:
	@echo "Running public sanity checks..."
	pytest tests/
