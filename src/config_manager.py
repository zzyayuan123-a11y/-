#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Configuration management for the generator.
"""

import json
from pathlib import Path
from typing import Dict, Any

from utils.logger import get_logger

logger = get_logger(__name__)


class ConfigManager:
    """Manage application configuration."""

    def __init__(self, config_dir: str = 'config'):
        """Initialize config manager.

        Args:
            config_dir: Path to configuration directory
        """
        self.config_dir = Path(config_dir)
        self.config_dir.mkdir(parents=True, exist_ok=True)

    def load_config(self, config_name: str) -> Dict[str, Any]:
        """Load configuration file.

        Args:
            config_name: Configuration filename

        Returns:
            Configuration dictionary
        """
        config_path = self.config_dir / f'{config_name}.json'
        if config_path.exists():
            try:
                with open(config_path, 'r', encoding='utf-8') as f:
                    return json.load(f)
            except Exception as e:
                logger.error(f'Failed to load config {config_name}: {e}')
        return {}

    def save_config(self, config_name: str, config: Dict[str, Any]) -> bool:
        """Save configuration file.

        Args:
            config_name: Configuration filename
            config: Configuration dictionary

        Returns:
            True if successful
        """
        try:
            config_path = self.config_dir / f'{config_name}.json'
            with open(config_path, 'w', encoding='utf-8') as f:
                json.dump(config, f, ensure_ascii=False, indent=2)
            logger.info(f'Config saved: {config_path}')
            return True
        except Exception as e:
            logger.error(f'Failed to save config: {e}')
            return False
