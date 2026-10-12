"""Load every open LH-Bench dataset and print its size and columns.

    pip install datasets
    python examples/load.py
"""
from datasets import load_dataset

OPEN = [
    "frontend-figma-to-code",
    "figma2code-expert-preferences",
    "remotion-video-gen",
    "remotion-video-preferences",
    "credit-underwriting-preview",
]

for name in OPEN:
    data = load_dataset(f"metaphilabs/{name}", split="train")
    print(f"{name}: {len(data)} rows, columns {data.column_names}")
