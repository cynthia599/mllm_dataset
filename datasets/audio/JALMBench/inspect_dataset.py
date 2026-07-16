from pathlib import Path
import pandas as pd


ROOT = Path("JALMBench-data")


def main():

    files = list(ROOT.rglob("*"))

    print("Dataset files:")

    for f in files[:50]:
        print(f)


    parquet_files = list(ROOT.rglob("*.parquet"))


    if parquet_files:

        df = pd.read_parquet(parquet_files[0])

        print("\nColumns:")
        print(df.columns.tolist())

        print("\nSamples:")
        print(df.head())


if __name__ == "__main__":
    main()