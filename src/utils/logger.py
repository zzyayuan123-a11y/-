#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Logging utility.
"""

import logging
import sys
from pathlib import Path

# Create logs directory
logs_dir = Path('logs')
logs_dir.mkdir(exist_ok=True)


def get_logger(name: str, level=logging.INFO) -> logging.Logger:
    """Get configured logger.

    Args:
        name: Logger name
        level: Logging level

    Returns:
        Configured logger instance
    """
    logger = logging.getLogger(name)
    logger.setLevel(level)

    # Console handler
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(level)
    console_format = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    console_handler.setFormatter(console_format)

    # File handler
    file_handler = logging.FileHandler(logs_dir / 'app.log')
    file_handler.setLevel(level)
    file_format = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    file_handler.setFormatter(file_format)

    # Add handlers if not already added
    if not logger.handlers:
        logger.addHandler(console_handler)
        logger.addHandler(file_handler)

    return logger
