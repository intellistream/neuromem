"""
neuromem - Standalone Memory Management Engine

A flexible memory management system for RAG applications with support for
vector databases, key-value stores, and graph structures.
"""

from .memory_manager import MemoryManager
from .memory_collection import (
    BaseCollection,
    VDBCollection,
    KVCollection,
    GraphCollection,
)

__version__ = "0.1.0"
__all__ = [
    "MemoryManager",
    "BaseCollection",
    "VDBCollection",
    "KVCollection",
    "GraphCollection",
]
