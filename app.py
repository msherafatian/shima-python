"""
Docker entry point for SHIMA.

This file is specifically for Docker/Gunicorn deployment.
For development, use: python -m shima
"""

from shima.app import app, server

# Expose server for gunicorn
__all__ = ['app', 'server']

if __name__ == "__main__":
    # For direct execution: python app.py
    from shima.app import run_app
    run_app(debug=True)
