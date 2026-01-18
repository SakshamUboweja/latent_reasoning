.PHONY: help install install-cuda install-dev install-all clean test venv

help:
	@echo "Latent Reasoning - Installation Commands"
	@echo "========================================="
	@echo ""
	@echo "  make venv          - Create virtual environment"
	@echo "  make install       - Install CPU version"
	@echo "  make install-cuda  - Install with CUDA support (Linux only)"
	@echo "  make install-dev   - Install with dev tools"
	@echo "  make install-all   - Install everything (CUDA + dev)"
	@echo "  make install-smart - Auto-detect and install"
	@echo "  make clean         - Remove virtual environment"
	@echo "  make test          - Verify installation"
	@echo ""

venv:
	@echo "Creating virtual environment with Python 3.12..."
	python3.12 -m venv venv
	@echo "✓ Virtual environment created"
	@echo ""
	@echo "Activate with: source venv/bin/activate"

install: venv
	@echo "Installing base dependencies..."
	./venv/bin/pip install --upgrade pip setuptools wheel
	./venv/bin/pip install -e .
	@echo "✓ Installation complete"

install-cuda: venv
	@echo "Installing with CUDA support..."
	./venv/bin/pip install --upgrade pip setuptools wheel
	./venv/bin/pip install -e ".[cuda]"
	@echo "✓ Installation complete (with CUDA)"

install-dev: venv
	@echo "Installing with dev tools..."
	./venv/bin/pip install --upgrade pip setuptools wheel
	./venv/bin/pip install -e ".[dev]"
	@echo "✓ Installation complete (with dev tools)"

install-all: venv
	@echo "Installing everything..."
	./venv/bin/pip install --upgrade pip setuptools wheel
	./venv/bin/pip install -e ".[all,dev]"
	@echo "✓ Installation complete (all packages)"

install-smart: venv
	@echo "Running smart installer..."
	./venv/bin/pip install --upgrade pip setuptools wheel
	./venv/bin/python install.py
	@echo "✓ Smart installation complete"

clean:
	@echo "Removing virtual environment..."
	rm -rf venv
	rm -rf *.egg-info
	rm -rf build dist
	find . -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null || true
	find . -type f -name "*.pyc" -delete 2>/dev/null || true
	@echo "✓ Cleanup complete"

test:
	@echo "Testing installation..."
	@./venv/bin/python -c "import torch; import transformers; import datasets; print('✓ Core packages: OK')" || echo "❌ Core packages: FAILED"
	@./venv/bin/python -c "import torch; print(f'✓ CUDA available: {torch.cuda.is_available()}')" || echo "❌ CUDA check: FAILED"
	@./venv/bin/python -c "import torch, transformers, datasets, peft, accelerate; print('✓ ML packages: OK')" || echo "❌ ML packages: FAILED"
	@echo ""
	@echo "Python version:"
	@./venv/bin/python --version
	@echo ""
	@echo "Installed packages:"
	@./venv/bin/pip list | head -20

# Aliases
setup: install
cuda: install-cuda
dev: install-dev
all: install-all
