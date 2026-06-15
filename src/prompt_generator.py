#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
AI prompt generator for image generation tools.

Generates prompts for:
- Midjourney
- DALL-E
- 即梦
- 可灵
"""

import json
from pathlib import Path
from typing import Dict, List, Optional

from utils.logger import get_logger

logger = get_logger(__name__)

# Category-specific keywords
CATEGORY_KEYWORDS = {
    '烘焙食品': {
        'style': ['artisanal', 'freshly baked', 'delicious', 'homemade'],
        'materials': ['flour', 'butter', 'chocolate', 'cream'],
        'ambiance': ['warm lighting', 'cozy', 'appetizing'],
    },
    '包装礼盒': {
        'style': ['premium', 'luxury', 'elegant', 'gift-worthy'],
        'materials': ['kraft paper', 'ribbon', 'gold foil', 'silk'],
        'ambiance': ['professional photography', 'studio lighting', 'high-end'],
    },
    '美妆个护': {
        'style': ['glamorous', 'professional', 'sophisticated', 'beauty'],
        'materials': ['glass', 'packaging design', 'minimalist'],
        'ambiance': ['soft lighting', 'makeup aesthetic', 'high fashion'],
    },
    '家居百货': {
        'style': ['modern', 'stylish', 'functional', 'home decor'],
        'materials': ['wood', 'metal', 'ceramic', 'fabric'],
        'ambiance': ['interior design', 'lifestyle photography', 'natural light'],
    },
    '小商品': {
        'style': ['cute', 'practical', 'colorful', 'everyday'],
        'materials': ['plastic', 'metal', 'rubber'],
        'ambiance': ['bright', 'cheerful', 'product photography'],
    },
}

# Style modifiers
STYLE_MODIFIERS = {
    'modern': 'modern, minimalist, clean lines, contemporary',
    'elegant': 'elegant, sophisticated, luxury, refined',
    'fresh': 'fresh, vibrant, colorful, light-filled',
    'creative': 'creative, artistic, unique, innovative',
    'premium': 'premium quality, high-end, professional',
}


class PromptGenerator:
    """Generate AI prompts for image generation."""

    def __init__(self, config_dir: str = 'config'):
        """Initialize prompt generator.

        Args:
            config_dir: Path to configuration directory
        """
        self.config_dir = Path(config_dir)
        self.category_keywords = CATEGORY_KEYWORDS
        self.style_modifiers = STYLE_MODIFIERS

    def generate_prompt(
        self,
        product_name: str,
        category: str,
        selling_points: List[str],
        style: str = 'modern',
        platform: str = 'midjourney',
    ) -> str:
        """Generate AI prompt for image generation.

        Args:
            product_name: Product name
            category: Product category
            selling_points: List of selling points
            style: Design style
            platform: Target platform (midjourney, dalle, jimengyun, keling)

        Returns:
            Generated prompt string
        """
        # Get category keywords
        keywords = self.category_keywords.get(category, {})
        style_desc = self.style_modifiers.get(style, style)
        materials = ', '.join(keywords.get('materials', ['quality materials'])[:2])
        ambiance = ', '.join(keywords.get('ambiance', ['professional photography'])[:2])

        # Build description
        description = f'{product_name}'
        if selling_points:
            main_point = selling_points[0]
            description += f', {main_point}'

        # Build platform-specific prompt
        if platform == 'midjourney':
            prompt = f'{description}, {style_desc}, {materials}, {ambiance}, professional photography, high quality, detailed, --ar 3:4 --v 5.2'
        elif platform == 'dalle':
            prompt = f'A professional product photography of {description}. {style_desc}. Materials: {materials}. Lighting: {ambiance}. High quality, detailed, realistic.'
        elif platform == 'jimengyun':
            prompt = f'{description}，{style_desc}，{materials}，{ambiance}，专业产品摄影，高质量，详细，逼真'
        elif platform == 'keling':
            prompt = f'{description}，{style_desc}，{materials}，{ambiance}，产品视角，专业拍摄'
        else:
            prompt = f'{description}, {style_desc}, {materials}, {ambiance}'

        logger.info(f'Prompt generated for {platform}')
        return prompt

    def generate_prompts_all_platforms(
        self,
        product_name: str,
        category: str,
        selling_points: List[str],
        style: str = 'modern',
    ) -> Dict[str, str]:
        """Generate prompts for all platforms.

        Args:
            product_name: Product name
            category: Product category
            selling_points: List of selling points
            style: Design style

        Returns:
            Dictionary of prompts by platform
        """
        platforms = ['midjourney', 'dalle', 'jimengyun', 'keling']
        prompts = {}
        for platform in platforms:
            prompts[platform] = self.generate_prompt(
                product_name,
                category,
                selling_points,
                style,
                platform,
            )
        return prompts

    def generate_keywords(
        self,
        category: str,
        style: str = 'modern',
    ) -> List[str]:
        """Generate keyword suggestions for product.

        Args:
            category: Product category
            style: Design style

        Returns:
            List of keyword suggestions
        """
        keywords = []

        # Add category keywords
        if category in self.category_keywords:
            cat_keywords = self.category_keywords[category]
            keywords.extend(cat_keywords.get('style', []))
            keywords.extend(cat_keywords.get('materials', []))
            keywords.extend(cat_keywords.get('ambiance', []))

        # Add style keywords
        if style in self.style_modifiers:
            keywords.extend(self.style_modifiers[style].split(', '))

        # Remove duplicates
        keywords = list(set(keywords))

        logger.info(f'Generated {len(keywords)} keywords')
        return keywords
