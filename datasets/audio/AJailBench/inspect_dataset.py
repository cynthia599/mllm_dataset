from pathlib import Path
import json


ROOT = Path("AJailBench-data")


def main():

    files = list(ROOT.rglob("*"))

    print("Files:")
    for f in files[:50]:
        print(f)


    json_files = list(ROOT.rglob("*.json"))

    if json_files:

        with open(json_files[0],
                  "r",
                  encoding="utf-8") as f:

            data = json.load(f)

        print("\nSample:")
        print(data[0])


if __name__ == "__main__":
    main()