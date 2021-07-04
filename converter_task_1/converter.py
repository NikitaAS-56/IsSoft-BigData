import pandas as pd
import pyarrow
import click


def get_schema(schema_parquet_file):
    parquet_file_name = schema_parquet_file
    try:
        df = pd.read_parquet(parquet_file_name)
        schema = pyarrow.Table.from_pandas(df=df).schema
    except Exception as e:
        print(e)
    return schema

@click.command()
@click.option("--csv2parquet", type=(str, str), help="Convert csv to parquet")
@click.option("--parquet2csv", type=(str, str), help="Convert parquet to csv")
@click.option("--schema_parquet", type=str, help="Get schema of parquet file")
def convert(csv2parquet, parquet2csv, schema_parquet):
    if csv2parquet:
        csv_file_name, parquet_file_name = csv2parquet

        try:
            df = pd.read_csv(csv_file_name)
            df.to_parquet(parquet_file_name, index=False)
        except Exception as e:
            print(e)

    if parquet2csv:
        parquet_file_name, csv_file_name = parquet2csv
        try:
            df = pd.read_parquet(parquet_file_name)
            df.to_csv(csv_file_name, index=False)

        except Exception as e:
            print(e)

    if schema_parquet:
        print(get_schema(schema_parquet))


if __name__ == "__main__":
   convert()