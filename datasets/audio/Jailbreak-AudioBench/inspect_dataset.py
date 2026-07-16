from pathlib import Path
import pandas as pd


ROOT = Path("Jailbreak-AudioBench-data")


def main():

    files = list(ROOT.rglob("*.parquet"))

    print("Found parquet files:")
    for f in files:
        print(f)


    if not files:
        return


    df = pd.read_parquet(files[0])


    print("\nColumns:")
    print(df.columns.tolist())


    print("\nSamples:")
    print(df.head())


    print("\nSize:")
    print(len(df))


if __name__ == "__main__":
    main()