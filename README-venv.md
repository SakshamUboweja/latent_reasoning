# Virtual Environment Setup

## Overview
This project combines the requirements from both submodules:
- **HRPO**: Reinforcement learning for language models
- **Scratchpad-Thinking**: Latent reasoning techniques

The project now supports flexible installation via `pyproject.toml` with optional CUDA dependencies!

## Quick Installation

Choose one of these methods:

### Method 1: Makefile (Easiest)
```bash
make install          # CPU version (macOS, or systems without CUDA)
make install-cuda     # With CUDA support (Linux with NVIDIA GPU)
make install-smart    # Auto-detect and install
make help            # See all options
```

### Method 2: Using pyproject.toml
```bash
pip install -e .              # CPU version
pip install -e ".[cuda]"      # With CUDA support
pip install -e ".[all,dev]"   # Everything
```

### Method 3: Smart Installer
```bash
python install.py  # Detects your system and installs appropriately
```

### Method 4: Traditional requirements.txt
```bash
pip install -r requirements.txt  # Legacy method
```

For detailed installation instructions, see [INSTALL.md](INSTALL.md).

## Environment Details
- **Python Version**: 3.12.7
- **Location**: `./venv`
- **Total Packages**: ~173 packages installed

## Key Packages Installed
- **PyTorch**: 2.7.1
- **Transformers**: 4.52.4
- **Datasets**: 3.6.0
- **Accelerate**: 1.7.0
- **PEFT**: 0.15.2
- **Wandb**: 0.19.8
- **NumPy**: 1.26.4 (downgraded for numba compatibility)
- **Protobuf**: 5.29.3 (downgraded for wandb compatibility)

## macOS Compatibility Notes
The following packages were excluded as they are CUDA-specific and not compatible with macOS:
- cuda-bindings, cuda-python, cupy-cuda12x, cut-cross-entropy
- flashinfer-python
- NVIDIA CUDA libraries (cublas, cudnn, etc.)
- vllm, xformers, sglang, sglang-router, sgl-kernel
- torchao, xgrammar, triton
- torchaudio and torchvision (CUDA versions)
- decord

## Activation
To activate the virtual environment, run:
```bash
source venv/bin/activate
```

## Requirements File
The combined requirements are in `requirements.txt` at the project root.

## Version Conflicts Resolved
1. **numpy**: Downgraded from 2.2.6 to 1.26.4 for numba compatibility (requires <2.1)
2. **protobuf**: Downgraded from 6.31.1 to 5.29.3 for wandb compatibility (requires <6)
3. **Python**: Used 3.12 instead of 3.13 for numba compatibility

## Project Files

The project now includes several helpful files:

| File | Purpose |
|------|---------|
| `pyproject.toml` | Modern Python packaging with optional CUDA dependencies |
| `requirements.txt` | Legacy format (CUDA packages commented out) |
| `install.py` | Smart installer that detects your system |
| `check_env.py` | Validates your installation |
| `Makefile` | Convenient installation commands |
| `INSTALL.md` | Comprehensive installation guide |
| `README.md` | Main project documentation |

## Testing Your Installation

Run the environment checker:
```bash
source venv/bin/activate
python check_env.py
```

Or use make:
```bash
make test
```

## Notes
- Current environment is designed for macOS (Apple Silicon/ARM64)
- CUDA-dependent features from the original repos are excluded on macOS
- All core ML/NLP functionality works correctly
- To use CUDA features, use a Linux system with NVIDIA GPU and install with `pip install -e ".[cuda]"`
