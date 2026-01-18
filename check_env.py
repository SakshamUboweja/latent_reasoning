#!/usr/bin/env python3
"""
Environment validation script - checks if all required packages are installed and working.
"""
import sys
import platform


def check_import(module_name, display_name=None):
    """Try to import a module and return success status."""
    display_name = display_name or module_name
    try:
        __import__(module_name)
        print(f"  ✓ {display_name}")
        return True
    except ImportError as e:
        print(f"  ✗ {display_name} - {str(e)}")
        return False


def check_cuda():
    """Check CUDA availability."""
    try:
        import torch
        if torch.cuda.is_available():
            print(f"  ✓ CUDA is available")
            print(f"    - Device: {torch.cuda.get_device_name(0)}")
            print(f"    - Count: {torch.cuda.device_count()}")
            return True
        else:
            print(f"  ℹ CUDA not available (CPU mode)")
            return False
    except Exception as e:
        print(f"  ✗ Error checking CUDA: {e}")
        return False


def check_versions():
    """Check versions of key packages."""
    packages = {
        'torch': 'PyTorch',
        'transformers': 'Transformers',
        'datasets': 'Datasets',
        'accelerate': 'Accelerate',
        'peft': 'PEFT',
        'wandb': 'Weights & Biases',
    }

    print("\n📦 Key Package Versions:")
    for module, name in packages.items():
        try:
            mod = __import__(module)
            version = getattr(mod, '__version__', 'unknown')
            print(f"  • {name}: {version}")
        except ImportError:
            print(f"  • {name}: NOT INSTALLED")


def check_optional_cuda():
    """Check optional CUDA packages."""
    cuda_packages = [
        ('vllm', 'vLLM'),
        ('xformers', 'xFormers'),
        ('sglang', 'SGLang'),
        ('triton', 'Triton'),
    ]

    print("\n🚀 Optional CUDA Packages:")
    any_installed = False
    for module, name in cuda_packages:
        if check_import(module, name):
            any_installed = True

    if not any_installed:
        print("  ℹ No CUDA-specific packages installed (CPU mode)")


def main():
    """Main validation routine."""
    print("=" * 60)
    print("Environment Validation")
    print("=" * 60)

    # System info
    print(f"\n🖥️  System Information:")
    print(f"  • Platform: {platform.platform()}")
    print(f"  • Python: {sys.version.split()[0]}")
    print(f"  • Architecture: {platform.machine()}")

    # Core packages
    print(f"\n📚 Core Packages:")
    core_packages = [
        ('torch', 'PyTorch'),
        ('transformers', 'Transformers'),
        ('datasets', 'Datasets'),
        ('accelerate', 'Accelerate'),
        ('peft', 'PEFT'),
        ('numpy', 'NumPy'),
        ('pandas', 'Pandas'),
    ]

    all_core_ok = all(check_import(mod, name) for mod, name in core_packages)

    # CUDA check
    print(f"\n🎮 CUDA Status:")
    check_cuda()

    # Optional packages
    check_optional_cuda()

    # Version info
    check_versions()

    # Summary
    print("\n" + "=" * 60)
    if all_core_ok:
        print("✅ Environment is ready!")
        print("\nYou can now:")
        print("  • Train models with HRPO")
        print("  • Run Scratchpad-Thinking experiments")
        print("  • Use Transformers, Datasets, and PEFT")
    else:
        print("⚠️  Some core packages are missing.")
        print("\nPlease run one of:")
        print("  • make install")
        print("  • pip install -e .")
        print("  • python install.py")
    print("=" * 60)

    return 0 if all_core_ok else 1


if __name__ == "__main__":
    sys.exit(main())
