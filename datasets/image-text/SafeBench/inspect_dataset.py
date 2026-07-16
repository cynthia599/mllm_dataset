from collections import Counter
from pathlib import Path

import pandas as pd


ROOT = Path("SafeBench-data")


def inspect_category() -> None:
    category_path = ROOT / "category.csv"

    if not category_path.exists():
        print(f"未找到：{category_path}")
        return

    df = pd.read_csv(category_path)

    print("=" * 80)
    print("category.csv")
    print("字段：", df.columns.tolist())
    print("类别数量：", len(df))
    print(df.to_string(index=False))


def inspect_sample() -> None:
    sample_path = ROOT / "sample.csv"

    if not sample_path.exists():
        print(f"未找到：{sample_path}")
        return

    df = pd.read_csv(sample_path)

    print("=" * 80)
    print("sample.csv")
    print("样本数量：", len(df))
    print("字段：", df.columns.tolist())
    print("\n前 5 条样本：")
    print(df.head().to_string())

    for field in ("category", "label", "type", "modality"):
        if field in df.columns:
            print(f"\n字段 {field} 的分布：")
            print(df[field].value_counts(dropna=False))


def inspect_files() -> None:
    print("=" * 80)
    print("数据目录统计")

    extensions = {
        "image": {".png", ".jpg", ".jpeg", ".webp"},
        "audio": {".wav", ".mp3", ".flac", ".m4a"},
        "text": {".txt", ".json", ".jsonl", ".csv"},
    }

    files = list(ROOT.rglob("*"))

    for data_type, suffixes in extensions.items():
        count = sum(
            1
            for path in files
            if path.is_file() and path.suffix.lower() in suffixes
        )
        print(f"{data_type}: {count}")

    directories = sorted(
        path
        for path in ROOT.rglob("*")
        if path.is_dir()
    )

    print("\n主要目录：")
    for path in directories[:30]:
        print(path)


def main() -> None:
    if not ROOT.exists():
        raise FileNotFoundError(
            f"未找到 {ROOT}，请先运行 download_minibench.bat。"
        )

    inspect_category()
    inspect_sample()
    inspect_files()


if __name__ == "__main__":
    main()