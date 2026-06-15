#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Template generator for detail page modules.

Generates:
- Hero image template
- Detail page modules
- Layout compositions
"""

import json
from pathlib import Path
from typing import Dict, List, Optional

from PIL import Image, ImageDraw

from utils.logger import get_logger

logger = get_logger(__name__)

# Standard sizes for Taobao/Douyin detail pages
STANDARD_SIZES = {
    'mobile_width': 750,
    'hero_height': 900,
    'module_min_height': 400,
    'module_max_height': 1500,
}

MODULE_TEMPLATES = {
    'hero': {
        'name': '主图',
        'width': 750,
        'height': 900,
        'components': ['product_image', 'title', 'price_tag', 'promotional_badge'],
    },
    'selling_points': {
        'name': '卖点模块',
        'width': 750,
        'height': 500,
        'components': ['heading', 'points_grid', 'background'],
    },
    'usage_scene': {
        'name': '使用场景',
        'width': 750,
        'height': 600,
        'components': ['scene_image', 'description_text'],
    },
    'material_details': {
        'name': '材质工艺',
        'width': 750,
        'height': 800,
        'components': ['detail_images', 'material_text', 'process_flow'],
    },
    'size_specs': {
        'name': '尺寸规格',
        'width': 750,
        'height': 600,
        'components': ['size_table', 'measurement_image'],
    },
    'product_comparison': {
        'name': '产品对比',
        'width': 750,
        'height': 700,
        'components': ['comparison_table', 'vs_product_image'],
    },
    'audience_match': {
        'name': '适用人群',
        'width': 750,
        'height': 500,
        'components': ['audience_text', 'scenario_icons'],
    },
    'trust_warranty': {
        'name': '保障信息',
        'width': 750,
        'height': 600,
        'components': ['warranty_icons', 'support_text', 'contact_info'],
    },
}


class TemplateGenerator:
    """Generate detail page templates."""

    def __init__(self, config_dir: str = 'config'):
        """Initialize template generator.

        Args:
            config_dir: Path to configuration directory
        """
        self.config_dir = Path(config_dir)
        self.templates = MODULE_TEMPLATES
        self.styles = self._load_styles()

    def _load_styles(self) -> Dict:
        """Load design styles configuration.

        Returns:
            Dictionary of style configurations
        """
        styles_path = self.config_dir / 'styles.json'
        if styles_path.exists():
            try:
                with open(styles_path, 'r', encoding='utf-8') as f:
                    return json.load(f)
            except Exception as e:
                logger.warning(f'Failed to load styles config: {e}')
        return self._default_styles()

    def _default_styles(self) -> Dict:
        """Return default style configurations.

        Returns:
            Default styles dictionary
        """
        return {
            'modern': {
                'primary_color': '#FF6B6B',
                'secondary_color': '#4ECDC4',
                'background': '#FFFFFF',
                'text_color': '#333333',
                'accent_color': '#FFD93D',
                'font_family': 'SimHei, Arial',
            },
            'elegant': {
                'primary_color': '#8B4513',
                'secondary_color': '#D2B48C',
                'background': '#FFF8DC',
                'text_color': '#2C2C2C',
                'accent_color': '#CD853F',
                'font_family': 'SimHei, Arial',
            },
            'fresh': {
                'primary_color': '#90EE90',
                'secondary_color': '#87CEEB',
                'background': '#F0FFFF',
                'text_color': '#333333',
                'accent_color': '#FFB6C1',
                'font_family': 'SimHei, Arial',
            },
        }

    def generate_hero_image(
        self,
        product_image: Image.Image,
        title: str,
        selling_points: List[str],
        style: str = 'modern',
        price: Optional[str] = None,
    ) -> Image.Image:
        """Generate hero image template.

        Args:
            product_image: Product image
            title: Product title
            selling_points: List of selling points
            style: Design style
            price: Product price (optional)

        Returns:
            Generated hero image
        """
        width = STANDARD_SIZES['mobile_width']
        height = STANDARD_SIZES['hero_height']

        # Create base image
        image = Image.new('RGB', (width, height), '#FFFFFF')
        draw = ImageDraw.Draw(image)

        # Composite product image (top 60%)
        product_height = int(height * 0.6)
        resized_product = product_image.resize((width, product_height), Image.Resampling.LANCZOS)
        image.paste(resized_product, (0, 50))

        # Add title and selling points (bottom 40%)
        text_start_y = product_height + 100

        # Draw title
        title_text = title[:20] + '...' if len(title) > 20 else title
        draw.text((20, text_start_y), title_text, fill='#333333', font=None)

        # Draw selling points
        points_y = text_start_y + 60
        for i, point in enumerate(selling_points[:2]):
            point_text = f'✓ {point[:15]}...'
            draw.text((20, points_y + i * 40), point_text, fill='#FF6B6B', font=None)

        # Add price if provided
        if price:
            draw.text((20, height - 80), f'¥ {price}', fill='#FF6B6B', font=None)

        logger.info(f'Hero image generated: {width}x{height}')
        return image

    def generate_selling_points_module(
        self,
        selling_points: List[str],
        style: str = 'modern',
    ) -> Image.Image:
        """Generate selling points module.

        Args:
            selling_points: List of selling points
            style: Design style

        Returns:
            Generated module image
        """
        width = STANDARD_SIZES['mobile_width']
        height = STANDARD_SIZES['module_min_height']

        image = Image.new('RGB', (width, height), '#FFFFFF')
        draw = ImageDraw.Draw(image)

        # Draw heading
        draw.text((30, 30), '核心卖点', fill='#333333', font=None)

        # Draw points
        point_height = (height - 100) // max(len(selling_points), 1)
        for i, point in enumerate(selling_points[:5]):
            y = 100 + i * point_height
            draw.rectangle(
                [(30, y), (720, y + point_height - 20)],
                outline='#FF6B6B',
                width=2
            )
            draw.text(
                (50, y + 20),
                f'• {point[:30]}...' if len(point) > 30 else f'• {point}',
                fill='#333333',
                font=None
            )

        logger.info(f'Selling points module generated: {width}x{height}')
        return image

    def generate_detail_modules(
        self,
        product_data: Dict,
        style: str = 'modern',
    ) -> Dict[str, Image.Image]:
        """Generate all detail page modules.

        Args:
            product_data: Product information dictionary
            style: Design style

        Returns:
            Dictionary of module images
        """
        modules = {}

        # Generate hero image
        if 'image' in product_data and 'title' in product_data:
            try:
                modules['hero'] = self.generate_hero_image(
                    product_data['image'],
                    product_data['title'],
                    product_data.get('selling_points', []),
                    style,
                    product_data.get('price'),
                )
            except Exception as e:
                logger.error(f'Failed to generate hero image: {e}')

        # Generate selling points module
        if 'selling_points' in product_data:
            try:
                modules['selling_points'] = self.generate_selling_points_module(
                    product_data['selling_points'],
                    style,
                )
            except Exception as e:
                logger.error(f'Failed to generate selling points module: {e}')

        logger.info(f'Generated {len(modules)} modules')
        return modules

    def get_module_config(self, module_id: str) -> Optional[Dict]:
        """Get module configuration.

        Args:
            module_id: Module identifier

        Returns:
            Module configuration dictionary or None
        """
        return self.templates.get(module_id)

    def list_modules(self) -> List[str]:
        """List available modules.

        Returns:
            List of module IDs
        """
        return list(self.templates.keys())
