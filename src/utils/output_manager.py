#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Output management and file handling.
"""

import json
from datetime import datetime
from pathlib import Path
from typing import Dict, List

from utils.logger import get_logger

logger = get_logger(__name__)


class OutputManager:
    """Manage output files and directories."""

    def __init__(self, output_dir: str = 'output'):
        """Initialize output manager.

        Args:
            output_dir: Base output directory
        """
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)

    def save_config(self, config: Dict, output_path: str) -> bool:
        """Save configuration to JSON file.

        Args:
            config: Configuration dictionary
            output_path: Output file path

        Returns:
            True if successful
        """
        try:
            Path(output_path).parent.mkdir(parents=True, exist_ok=True)
            with open(output_path, 'w', encoding='utf-8') as f:
                json.dump(config, f, ensure_ascii=False, indent=2)
            logger.info(f'Config saved: {output_path}')
            return True
        except Exception as e:
            logger.error(f'Failed to save config: {e}')
            return False

    def save_prompts(self, prompts: Dict[str, str], output_path: str) -> bool:
        """Save prompts to text file.

        Args:
            prompts: Prompts dictionary
            output_path: Output file path

        Returns:
            True if successful
        """
        try:
            Path(output_path).parent.mkdir(parents=True, exist_ok=True)
            with open(output_path, 'w', encoding='utf-8') as f:
                for platform, prompt in prompts.items():
                    f.write(f'[{platform.upper()}]\n')
                    f.write(f'{prompt}\n\n')
            logger.info(f'Prompts saved: {output_path}')
            return True
        except Exception as e:
            logger.error(f'Failed to save prompts: {e}')
            return False

    def get_timestamp(self) -> str:
        """Get current timestamp in ISO format.

        Returns:
            ISO format timestamp
        """
        return datetime.now().isoformat()
