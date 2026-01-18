#!/usr/bin/env python3
"""
Smart installation script that detects CUDA availability and installs appropriate dependencies.
"""
import subprocess
import sys
import platform


def check_cuda_available():
    """Check if CUDA is available on the system."""
    try:
        # Try to run nvidia-smi
        result = subprocess.run(
            ['nvidia-smi'],
            capture_output=True,
            text=True,
            timeout=5
        )
        if result.returncode == 0:
            print("✓ NVIDIA GPU detected via nvidia-smi")
            return True
    except (subprocess.TimeoutExpired, FileNotFoundError):
        pass

    # Try to import torch and check CUDA
    try:
        import torch
        if torch.cuda.is_available():
            print("✓ CUDA available via PyTorch")
            return True
    except ImportError:
        pass

    return False


def get_install_command():
    """Determine the appropriate pip install command."""
    system = platform.system()
    has_cuda = check_cuda_available()

    print(f"\nPlatform: {system}")
    print(f"CUDA Available: {has_cuda}")

    if system == "Linux" and has_cuda:
        print("\n🚀 Installing with CUDA support...")
        return "pip install -e '.[cuda]'"
    elif system == "Darwin":  # macOS
        print("\n🍎 Installing for macOS (CPU only)...")
        return "pip install -e ."
    elif system == "Windows" and has_cuda:
        print("\n🪟 Installing for Windows with CUDA support...")
        return "pip install -e '.[cuda]'"
    else:
        print("\n💻 Installing CPU version...")
        return "pip install -e ."


def main():
    """Main installation logic."""
    print("=" * 60)
    print("Latent Reasoning Environment Setup")
    print("=" * 60)

    install_cmd = get_install_command()

    print(f"\nRecommended installation command:")
    print(f"  {install_cmd}")

    # Ask user if they want to proceed
    response = input("\nProceed with installation? (y/n): ").strip().lower()

    if response in ('y', 'yes'):
        print("\n📦 Installing dependencies...\n")
        try:
            subprocess.run(install_cmd, shell=True, check=True)
            print("\n✅ Installation completed successfully!")
            print("\nYou can now use the environment.")
        except subprocess.CalledProcessError as e:
            print(f"\n❌ Installation failed with error code {e.returncode}")
            sys.exit(1)
    else:
        print("\nInstallation cancelled.")
        print(f"To install manually, run: {install_cmd}")


if __name__ == "__main__":
    main()
