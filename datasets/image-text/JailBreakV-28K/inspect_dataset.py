from pathlib import Path

import pandas as pd


ROOT = Path("JailBreakV-28K-data") / "JailBreakV_28K"
CSV_PATH = ROOT / "JailBreakV_28K.csv"


def main() -> None:
    if not CSV_PATH.exists():
        raise FileNotFoundError(
            f"未找到 {CSV_PATH}，请先运行 download.bat 下载数据。"
        )

    df = pd.read_csv(CSV_PATH)

    print("样本总数：", len(df))
    print("字段：", df.columns.tolist())
    print("\n前 5 条数据：")
    print(df.head().to_string())

    possible_image_columns = [
        "image_path",
        "image",
        "img_path",
    ]

    image_column = next(
        (
            column
            for column in possible_image_columns
            if column in df.columns
        ),
        None,
    )

    if image_column is None:
        print("\n未自动找到图片路径字段。")
        return

    def resolve_path(value: object) -> Path:
        relative_path = Path(str(value).replace("\\", "/"))

        if (
            relative_path.parts
            and relative_path.parts[0].lower()
            == "jailbreakv_28k"
        ):
            relative_path = Path(*relative_path.parts[1:])

        return ROOT / relative_path

    full_paths = df[image_column].apply(resolve_path)
    exists = full_paths.apply(Path.exists)

    print("\n图片路径字段：", image_column)
    print("存在图片：", int(exists.sum()))
    print("缺失图片：", int((~exists).sum()))

    if "format" in df.columns:
        print("\n攻击类型分布：")
        print(df["format"].value_counts(dropna=False))

    if "policy" in df.columns:
        print("\n风险类别分布：")
        print(df["policy"].value_counts(dropna=False))


if __name__ == "__main__":
    main()