# Installation Guide

This project supports multiple installation methods depending on your hardware and requirements.

## Quick Start

### Option 1: Automatic Installation (Recommended)

The smart installation script will detect your system and install the appropriate dependencies:

```bash
# Create and activate virtual environment
python3.12 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Run the smart installer
python install.py
```

### Option 2: Manual Installation with pyproject.toml

#### For CPU-only (macOS or no CUDA)
```bash
python3.12 -m venv venv
source venv/bin/activate
pip install -e .
```

#### For CUDA-enabled systems (Linux/Windows with NVIDIA GPU)
```bash
python3.12 -m venv venv
source venv/bin/activate
pip install -e ".[cuda]"
```

#### For everything (development + CUDA)
```bash
python3.12 -m venv venv
source venv/bin/activate
pip install -e ".[all,dev]"
```

### Option 3: Using requirements.txt (Legacy)

If you prefer the traditional approach:

```bash
python3.12 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Note: `requirements.txt` has CUDA packages commented out by default (suitable for macOS).

## Installation Options Explained

### Base Installation (`pip install -e .`)
Installs core dependencies that work on all platforms:
- PyTorch (CPU version)
- Transformers
- Datasets
- Accelerate
- PEFT
- Wandb
- And ~170 other core packages

### CUDA Installation (`pip install -e ".[cuda]"`)
Adds CUDA-specific optimizations (Linux only):
- vllm (fast inference)
- xformers (memory-efficient attention)
- sglang (structured generation)
- NVIDIA CUDA libraries
- Flash Attention support
- cupy, triton, and other GPU accelerators

### Development Installation (`pip install -e ".[dev]"`)
Adds development tools:
- pytest (testing)
- black (formatting)
- ruff (linting)
- mypy (type checking)

## Platform-Specific Notes

### macOS (Apple Silicon)
- CUDA packages are automatically excluded via platform markers
- Uses CPU or MPS (Metal Performance Shaders) backend for PyTorch
- Recommended Python: 3.12.7
```bash
pip install -e .
```

### Linux with NVIDIA GPU
- CUDA packages will be installed automatically
- Requires CUDA 12.x toolkit installed
- Recommended Python: 3.12.7
```bash
# Check CUDA availability
nvidia-smi

# Install with CUDA support
pip install -e ".[cuda]"
```

### Windows with NVIDIA GPU
- Similar to Linux, but some packages may have limited support
- Recommended Python: 3.12.7
```bash
pip install -e ".[cuda]"
```

### Linux/Windows without GPU
- Same as macOS (CPU-only)
```bash
pip install -e .
```

## Python Version Requirements

- **Supported**: Python 3.9, 3.10, 3.11, 3.12
- **Recommended**: Python 3.12.7
- **Not Supported**: Python 3.13+ (numba compatibility issue)

## Verifying Installation

Test that everything is working:

```bash
python -c "import torch; import transformers; import datasets; print('✓ Core packages OK')"

# If you installed CUDA extras, test GPU:
python -c "import torch; print(f'CUDA available: {torch.cuda.is_available()}')"
```

## Troubleshooting

### Issue: numba requires Python < 3.13
**Solution**: Use Python 3.12
```bash
python3.12 -m venv venv
```

### Issue: CUDA packages fail to install on macOS
**Solution**: Use base installation only
```bash
pip install -e .  # Don't use [cuda] on macOS
```

### Issue: protobuf version conflict
**Solution**: Already handled in pyproject.toml (using 5.29.3)

### Issue: numpy version conflict
**Solution**: Already handled in pyproject.toml (using 1.26.4)

## Switching Between CUDA and CPU

If you want to switch:

```bash
# Uninstall CUDA packages
pip uninstall vllm xformers sglang -y

# Or reinstall fresh
rm -rf venv
python3.12 -m venv venv
source venv/bin/activate
pip install -e .  # CPU only
# or
pip install -e ".[cuda]"  # With CUDA
```

## Using with the Submodules

After installation, you can use both submodules:

```bash
# HRPO
cd HRPO
python your_script.py

# Scratchpad-Thinking
cd Scratchpad-Thinking
python your_script.py
```

The virtual environment in the parent directory will be used by both.

## Additional Resources

- **pyproject.toml**: Modern Python packaging with optional dependencies
- **requirements.txt**: Legacy format, manually managed
- **install.py**: Smart installer that detects your system
- **README-venv.md**: Details about the current environment setup
