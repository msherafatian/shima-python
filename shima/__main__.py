"""
Entry point for running SHIMA as a module.

This allows running the application with: python -m shima
"""

from shima.app import run_app

if __name__ == "__main__":
    run_app(debug=True)
