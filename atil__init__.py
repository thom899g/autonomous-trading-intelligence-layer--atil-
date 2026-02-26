"""
Autonomous Trading Intelligence Layer (ATIL)
Core package for pattern integrity-based trading system
Version: 1.0.0
"""

__version__ = "1.0.0"
__author__ = "ATIL Development Team"
__license__ = "Proprietary"

from .config import ATILConfig
from .pattern_integrity import PatternIntegrityEngine
from .data_ingestion import MarketDataIngestor
from .execution import TradeExecutor
from .reinforcement import RLAgent

__all__ = [
    "ATILConfig",
    "PatternIntegrityEngine",
    "MarketDataIngestor",
    "TradeExecutor",
    "RLAgent"
]