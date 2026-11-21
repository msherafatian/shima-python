"""
Deprecated compatibility namespace for MASIH-Python.

The implementation now lives in :mod:`shima`. This namespace is retained
for one release cycle and forwards imports to the SHIMA implementation.
"""

import importlib
import importlib.abc
import importlib.util
import sys
import warnings

import shima

warnings.warn(
    "The 'masih' namespace is deprecated; import from 'shima' instead.",
    DeprecationWarning,
    stacklevel=2,
)

__version__ = shima.__version__
__author__ = shima.__author__

sys.modules.setdefault("masih", sys.modules[__name__])


class _MasihCompatibilityLoader(importlib.abc.Loader):
    def __init__(self, target_name):
        self.target_name = target_name

    def create_module(self, spec):
        return importlib.import_module(self.target_name)

    def exec_module(self, module):
        return None


class _MasihCompatibilityFinder(importlib.abc.MetaPathFinder):
    def find_spec(self, fullname, path=None, target=None):
        if not fullname.startswith("masih."):
            return None

        target_name = "shima." + fullname[len("masih."):]
        try:
            target_spec = importlib.util.find_spec(target_name)
        except (ImportError, AttributeError, ModuleNotFoundError):
            return None
        if target_spec is None:
            return None

        is_package = target_spec.submodule_search_locations is not None
        return importlib.util.spec_from_loader(
            fullname,
            _MasihCompatibilityLoader(target_name),
            is_package=is_package,
        )


sys.meta_path.insert(0, _MasihCompatibilityFinder())
