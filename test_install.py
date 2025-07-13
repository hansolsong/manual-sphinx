#!/usr/bin/env python
"""Test installation of sphinx-marginbook-theme."""

import subprocess
import sys


def test_import():
    """Test that the package can be imported."""
    try:
        import sphinx_marginbook_theme

        print("✓ Package imported successfully")
        print(f"  Version: {sphinx_marginbook_theme.__version__}")
        return True
    except ImportError as e:
        print(f"✗ Import failed: {e}")
        return False


def test_sphinx_extension():
    """Test that Sphinx can load the extension."""
    test_conf = """
extensions = ['myst_parser', 'sphinx_marginbook_theme']
html_theme = 'marginbook'
"""

    # Create a minimal test project
    import os
    import tempfile

    with tempfile.TemporaryDirectory() as tmpdir:
        # Create conf.py
        conf_path = os.path.join(tmpdir, "conf.py")
        with open(conf_path, "w") as f:
            f.write(test_conf)

        # Create index.md
        index_path = os.path.join(tmpdir, "index.md")
        with open(index_path, "w") as f:
            f.write("# Test\n\n{margin}\nTest margin note\n")

        # Try to build
        try:
            result = subprocess.run(
                ["sphinx-build", "-b", "html", tmpdir, os.path.join(tmpdir, "_build")],
                capture_output=True,
                text=True,
            )
            if result.returncode == 0:
                print("✓ Sphinx build successful")
                return True
            else:
                print(f"✗ Sphinx build failed: {result.stderr}")
                return False
        except Exception as e:
            print(f"✗ Sphinx build error: {e}")
            return False


def main():
    """Run all tests."""
    print("Testing sphinx-marginbook-theme installation...\n")

    tests_passed = 0
    total_tests = 2

    if test_import():
        tests_passed += 1

    if test_sphinx_extension():
        tests_passed += 1

    print(f"\n{tests_passed}/{total_tests} tests passed")

    return tests_passed == total_tests


if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
