import json
from collections import Counter
from pathlib import Path
from typing import Any


ROOT = Path("VLSBench-data")
JSON_PATH = ROOT / "data.json"


def find_image_path(item: dict[str, Any]) -> str:
    for field in ("image_path", "image", "img_path", "path"):
        value = item.get(field)
        if value:
            return str(value)
    return ""


def main() -> None:
    if not JSON_PATH.exists():
        raise FileNotFoundError(
            f"未找到 {JSON_PATH}，请先运行 download.bat 下载数据。"
        )

    with JSON_PATH.open("r", encoding="utf-8") as file:
        data = json.load(file)

    if not isinstance(data, list):
        raise TypeError(
            f"预期 data.json 为列表，实际为 {type(data).__name__}"
        )

    print("样本总数：", len(data))

    if not data:
        return

    print("\n第一条样本字段：")
    print(list(data[0].keys()))

    print("\n第一条样本：")
    print(json.dumps(data[0], ensure_ascii=False, indent=2))

    categories = Counter(
        str(item.get("category"))
        for item in data
        if isinstance(item, dict) and item.get("category") is not None
    )

    if categories:
        print("\n风险类别分布：")
        for category, count in categories.most_common():
            print(f"{category}: {count}")

    existing_images = 0
    missing_images = 0

    for item in data:
        if not isinstance(item, dict):
            continue

        relative_path = find_image_path(item)
        if not relative_path:
            missing_images += 1
            continue

        normalized = Path(relative_path.replace("\\", "/"))
        image_path = ROOT / normalized

        if image_path.exists():
            existing_images += 1
        else:
            missing_images += 1

    print("\n图片存在数量：", existing_images)
    print("图片缺失数量：", missing_images)


if __name__ == "__main__":
    main()