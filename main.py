#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Main entry point for ecommerce product visual generator.

Usage:
    python main.py --input examples/sample_data.xlsx --output ./output
"""

import argparse
import sys
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path(__file__).parent / 'src'))

from batch_processor import BatchProcessor
from utils.logger import get_logger

logger = get_logger(__name__)


def main():
    parser = argparse.ArgumentParser(
        description='批量生成电商详情页和主图'
    )
    parser.add_argument(
        '--input',
        required=True,
        help='输入 Excel 文件路径'
    )
    parser.add_argument(
        '--output',
        default='./output',
        help='输出目录（默认：./output）'
    )
    parser.add_argument(
        '--style',
        default='modern',
        help='设计风格（默认：modern）'
    )
    parser.add_argument(
        '--dpi',
        type=int,
        default=72,
        help='输出分辨率（默认：72）'
    )
    parser.add_argument(
        '--format',
        choices=['png', 'jpg'],
        default='png',
        help='输出格式（默认：png）'
    )
    parser.add_argument(
        '--batch-size',
        type=int,
        default=5,
        help='批处理数量（默认：5）'
    )
    parser.add_argument(
        '--verbose',
        action='store_true',
        help='详细输出日志'
    )

    args = parser.parse_args()

    # Validate input file
    input_path = Path(args.input)
    if not input_path.exists():
        logger.error(f'输入文件不存在: {input_path}')
        sys.exit(1)

    if not input_path.suffix.lower() in ['.xlsx', '.csv', '.xls']:
        logger.error('输入文件必须是 Excel (.xlsx/.xls) 或 CSV 格式')
        sys.exit(1)

    # Create output directory
    output_path = Path(args.output)
    output_path.mkdir(parents=True, exist_ok=True)

    logger.info(f'开始处理: {input_path}')
    logger.info(f'输出目录: {output_path}')

    # Initialize batch processor
    processor = BatchProcessor(
        output_dir=output_path,
        style=args.style,
        dpi=args.dpi,
        output_format=args.format,
        batch_size=args.batch_size,
        verbose=args.verbose
    )

    # Process batch
    try:
        results = processor.process(input_path)
        logger.info(f'\n处理完成！')
        logger.info(f'成功: {results["success_count"]}')
        logger.info(f'失败: {results["failed_count"]}')
        logger.info(f'输出位置: {output_path}')
    except Exception as e:
        logger.error(f'处理失败: {e}')
        sys.exit(1)


if __name__ == '__main__':
    main()
