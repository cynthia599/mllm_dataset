from pathlib import Path
import json


ROOT = Path("Video-SafetyBench-data")


def inspect_json(path):

    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)

    print("="*50)
    print(path.name)

    print("Samples:", len(data))

    print("First sample:")
    print(
        json.dumps(
            data[0],
            ensure_ascii=False,
            indent=2
        )
    )


def main():

    files = list(ROOT.glob("*.json"))

    for file in files:
        inspect_json(file)


if __name__ == "__main__":
    main()