#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Data validation utilities.
"""

from typing import Any, Dict, List

from utils.logger import get_logger

logger = get_logger(__name__)


class DataValidator:
    """Validate input data."""

    REQUIRED_FIELDS = ['product_id', 'product_name', 'category']
    VALID_CATEGORIES = [
        '烘焙食品',
        '包装礼盒',
        '美妆个护',
        '家居百货',
        '小商品',
    ]

    @staticmethod
    def validate_product_data(product_data: Dict) -> bool:
        """Validate product data.

        Args:
            product_data: Product dictionary

        Returns:
            True if valid
        """
        # Check required fields
        for field in DataValidator.REQUIRED_FIELDS:
            if field not in product_data or not product_data[field]:
                logger.warning(f'Missing required field: {field}')
                return False

        # Validate category
        category = product_data.get('category')
        if category not in DataValidator.VALID_CATEGORIES:
            logger.warning(f'Invalid category: {category}')
            return False

        return True
