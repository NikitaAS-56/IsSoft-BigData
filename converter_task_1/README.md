# Data Files Convertor


#Files converter
This is a console utility that supports command line arguments.</br>
With this utility you can convert .csv to .parquet and back. You can also get parquet schema</br>
`python convert.py [--csv2parquet | —parquet2csv <src-filename> <dst-filename>] | [--get-schema <filename>] | [--help]`</br>
The utility supports the following functions
- `convert` - convert csv to convert and convert convert to csv

- `get_schema` - returns schema of parquet file


## Parameters
* `--help` show help message and exit
* `--csv2parquet` convert csv to parquet.
* `--parquet2csv` convert parquet to csv. 
* `--schema_parquet` get schema of parquet file.


## Usage

### Convert CSV to Parquet

Assume that you have some data in your `data.csv` file:

need to convert some `data.csv` file to `parquet`, so you need to write the following command:
```
$python convertor.py --csv2parquet data.csv output.parquet
```
And you receive new file `output.parquet` in your directory

### Convert Parquet to CSV
You can specify `--parquet2csv` parameter in order to convert `output.parquet` file back to csv
```
$python convertor.py --parquet2csv output.parquet convert_output.csv
```

### Get Parquet schema
There are some cases when you need to know the schema of your Parquet file. For example:
```
$python convertor.py --schema_parquet data_converted.parquet
```
The script produces the following output:
```
number: int64
Year: int64
Industry_aggregation_NZSIOC: string
Industry_code_NZSIOC: string
Industry_name_NZSIOC: string
Units: string
```
