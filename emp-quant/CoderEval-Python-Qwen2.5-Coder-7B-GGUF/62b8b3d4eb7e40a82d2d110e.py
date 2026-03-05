import os

def _c_optimizations_ignored():
    return os.getenv("PURE_PYTHON") is not None and os.getenv("PURE_PYTHON") != "0"