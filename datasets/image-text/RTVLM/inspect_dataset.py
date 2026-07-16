import json
from collections import Counter
from pathlib import Path

import pandas as pd


ROOT = Path("RTVLM-data")


def inspect_json(path: Path) -> None:
    with path.open("r", encoding="utf-8") as file:
        data = json.load(file)

    print("=" * 80)
    print("文件：", path)
    print("类型：", type(data).__name__)

    if isinstance(data, list):
        print("样本数量：", len(data))

        if data:
            print("\n第一条样本：")
            print(json.dumps(data[0], ensure_ascii=False, indent=2))

            for field in (
                "aspect",
                "category",
                "task",
                "subtask",
                "label",
                "refuse",
            ):
                values = [
                    item.get(field)
                    for item in data
                    if isinstance(item, dict) and item.get(field) is not None
                ]

                if values:
                    print(f"\n{field} 分布：")
                    print(Counter(map(str, values)))


def inspect_table(path: Path) -> None:
    if path.suffix.lower() == ".csv":
        df = pd.read_csv(path)
    else:
        df = pd.read_parquet(path)

    print("=" * 80)
    print("文件：", path)
    print("样本数量：", len(df))
    print("字段：", df.columns.tolist())
    print(df.head().to_string())

    for field in (
        "aspect",
        "category",
        "task",
        "subtask",
        "label",
    ):
        if field in df.columns:
            print(f"\n{field} 分布：")
            print(df[field].value_counts(dropna=False))


def main() -> None:
    if not ROOT.exists():
        raise FileNotFoundError(
            f"未找到 {ROOT}，请先运行 download.bat。"
        )

    files = [
        path
        for path in ROOT.rglob("*")
        if path.suffix.lower() in {".json", ".csv", ".parquet"}
    ]

    print("找到的数据文件：")
    for path in files:
        print(path)

    if not files:
        print("未找到 JSON、CSV 或 Parquet 文件。")
        return

    for path in files[:5]:
        try:
            if path.suffix.lower() == ".json":
                inspect_json(path)
            else:
                inspect_table(path)
        except Exception as exc:
            print(f"读取失败：{path}")
            print(exc)


if __name__ == "__main__":
    main()