# Latent Reasoning Project

Combined environment for exploring latent reasoning techniques using:
- **[HRPO](https://github.com/Yueeeeeeee/HRPO)**: Hidden Reward Policy Optimization
- **[Scratchpad-Thinking](https://github.com/sayam-goyal/Scratchpad-Thinking)**: Latent reasoning with scratchpad techniques

## 🚀 Quick Start

### 1. Clone with Submodules
```bash
git clone --recurse-submodules <your-repo-url>
cd latent_reasoning

# Or if already cloned:
git submodule update --init --recursive
```

### 2. Install Dependencies

**Easiest method** (using Makefile):
```bash
make install          # For CPU or macOS
make install-cuda     # For Linux with NVIDIA GPU
make install-smart    # Auto-detect your system
```

**Or using pip directly**:
```bash
# Create virtual environment
python3.12 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install
pip install -e .              # CPU version
pip install -e ".[cuda]"      # With CUDA support (Linux)
pip install -e ".[all,dev]"   # Everything including dev tools
```

**Or use the smart installer**:
```bash
python install.py  # Detects CUDA and installs appropriately
```

### 3. Verify Installation
```bash
python check_env.py
```

## 📋 Installation Options

This project uses modern Python packaging with `pyproject.toml` that supports:

| Installation | Command | Use Case |
|-------------|---------|----------|
| **CPU/macOS** | `pip install -e .` | Standard installation |
| **CUDA** | `pip install -e ".[cuda]"` | Linux with NVIDIA GPU |
| **Development** | `pip install -e ".[dev]"` | Add testing/linting tools |
| **Everything** | `pip install -e ".[all,dev]"` | All features |

The CUDA packages are automatically excluded on macOS using platform markers in `pyproject.toml`.

## 📦 What's Included

### Core ML Stack
- **PyTorch 2.7.1** - Deep learning framework
- **Transformers 4.52.4** - HuggingFace models
- **Datasets 3.6.0** - Data loading and processing
- **Accelerate 1.7.0** - Distributed training
- **PEFT 0.15.2** - Parameter-efficient fine-tuning
- **Wandb 0.19.8** - Experiment tracking

### Optional CUDA Packages (Linux only)
- **vLLM** - Fast inference engine
- **xFormers** - Memory-efficient attention
- **SGLang** - Structured generation
- **Flash Attention** - Optimized attention kernels
- **NVIDIA CUDA libraries** - GPU acceleration

### Development Tools (with `[dev]`)
- pytest, black, ruff, mypy

## 🛠️ Available Commands

```bash
make help            # Show all commands
make install         # Install CPU version
make install-cuda    # Install with CUDA
make install-smart   # Auto-detect and install
make test           # Verify installation
make clean          # Remove venv and cache files
```

## 🔍 Project Structure

```
latent_reasoning/
├── HRPO/                    # Submodule: Hidden Reward Policy Optimization
├── Scratchpad-Thinking/     # Submodule: Latent reasoning techniques
├── venv/                    # Virtual environment (created during install)
├── pyproject.toml           # Modern Python packaging with optional deps
├── requirements.txt         # Legacy format (CUDA commented out)
├── install.py              # Smart installer script
├── check_env.py            # Environment validation script
├── Makefile                # Convenient installation commands
├── INSTALL.md              # Detailed installation guide
├── README-venv.md          # Environment details
└── README.md               # This file
```

## 📖 Documentation

- **[INSTALL.md](INSTALL.md)** - Comprehensive installation guide
- **[README-venv.md](README-venv.md)** - Current environment details
- **[pyproject.toml](pyproject.toml)** - Package configuration

## 🖥️ Platform Support

| Platform | Status | Notes |
|----------|--------|-------|
| **macOS (Apple Silicon)** | ✅ Full support | CPU/MPS backend |
| **Linux + NVIDIA GPU** | ✅ Full support | CUDA acceleration |
| **Linux (CPU only)** | ✅ Full support | CPU backend |
| **Windows + NVIDIA GPU** | ⚠️ Partial | Some packages may have issues |
| **Windows (CPU only)** | ✅ Full support | CPU backend |

## 🐍 Python Version Support

- ✅ **Recommended**: Python 3.12.7
- ✅ **Supported**: Python 3.9, 3.10, 3.11, 3.12
- ❌ **Not Supported**: Python 3.13+ (numba compatibility)

## 🔧 How It Works

The `pyproject.toml` uses **optional dependencies** with **platform markers**:

```toml
[project.optional-dependencies]
cuda = [
    "vllm==0.7.3; platform_system=='Linux'",
    "xformers==0.0.28.post3; platform_system=='Linux'",
    # ... other CUDA packages
]
```

This means:
- On macOS: CUDA packages are automatically skipped
- On Linux: CUDA packages are installed when you use `[cuda]`
- On Windows: Same as Linux

## 🎯 Usage

After installation, use either submodule:

```bash
# Activate environment (if not already active)
source venv/bin/activate

# Use HRPO
cd HRPO
python train.py  # or your script

# Use Scratchpad-Thinking
cd Scratchpad-Thinking
python your_script.py
```

## 🐛 Troubleshooting

### Python 3.13 Issues
```bash
# Use Python 3.12 instead
python3.12 -m venv venv
```

### CUDA Packages on macOS
```bash
# Don't use [cuda] on macOS
pip install -e .  # Not: pip install -e ".[cuda]"
```

### Import Errors
```bash
# Verify your installation
python check_env.py

# Reinstall if needed
make clean
make install
```

### See More
Check [INSTALL.md](INSTALL.md) for detailed troubleshooting.

## 📝 License

This project combines:
- HRPO: (check HRPO/LICENSE)
- Scratchpad-Thinking: (check Scratchpad-Thinking/LICENSE)

## 🤝 Contributing

This is a research project combining two submodules. For contributions:
- HRPO-related: contribute to the [HRPO repository](https://github.com/Yueeeeeeee/HRPO)
- Scratchpad-related: contribute to the [Scratchpad-Thinking repository](https://github.com/sayam-goyal/Scratchpad-Thinking)

## 📚 References

- **HRPO**: [GitHub](https://github.com/Yueeeeeeee/HRPO)
- **Scratchpad-Thinking**: [GitHub](https://github.com/sayam-goyal/Scratchpad-Thinking)

## 🎉 Acknowledgments

Thanks to the authors of HRPO and Scratchpad-Thinking for their excellent research work!
