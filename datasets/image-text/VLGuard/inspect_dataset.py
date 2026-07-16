import json
from collections import Counter
from pathlib import Path


ROOT = Path("VLGuard-data")


def find_json_file(filename: str) -> Path:
    matches = list(ROOT.rglob(filename))
    if not matches:
        raise FileNotFoundError(
            f"未找到 {filename}，请先运行 download.bat 下载数据。"
        )
    return matches[0]


def inspect_json(path: Path) -> None:
    with path.open("r", encoding="utf-8") as file:
        data = json.load(file)

    print("=" * 80)
    print("文件：", path)
    print("数据类型：", type(data))
    print("样本数量：", len(data) if hasattr(data, "__len__") else "未知")

    if isinstance(data, list) and data:
        print("\n第一条样本：")
        print(json.dumps(data[0], ensure_ascii=False, indent=2))

        possible_group_fields = [
            "safety",
            "label",
            "category",
            "type",
            "dataset",
        ]

        for field in possible_group_fields:
            values = [
                item.get(field)
                for item in data
                if isinstance(item, dict) and field in item
            ]

            if values:
                print(f"\n字段 {field} 的分布：")
                print(Counter(map(str, values)))


def main() -> None:
    train_path = find_json_file("train.json")
    test_path = find_json_file("test.json")

    inspect_json(train_path)
    inspect_json(test_path)


if __name__ == "__main__":
    main()