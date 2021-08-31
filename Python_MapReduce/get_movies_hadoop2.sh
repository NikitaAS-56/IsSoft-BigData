#!/bin/bash

if ! [ -f tmp/movies.csv ]; then
  hdfs dfs -put tmp/movies.py
fi


function print_help() {
    echo "--N - Number of top rated movies for each genre"
    echo "--regexp - Filter movies by title"
    echo "--year_from - Filter movies by year starting from --year_from"
    echo "--year-to - Filter movies by year ending --year_to"
    echo "--genres - Filter movies by genre"
}

while [ -n "$1" ]
do
  case "$1" in
    --N)
      if [ -n "$2" ] && [ ${2:0:1} != "-" ]; then
        n_flag=$1
        n_value=$2

        shift 2
      fi;;
    --regexp)
      if [ -n "$2" ] && [ ${2:0:1} != "-" ]; then
        regexp_flag=$1
        regexp_value=$2
        shift 2
      fi;;
    --year_from)
      if [ -n "$2" ] && [ ${2:0:1} != "-" ]; then
        year_from_flag=$1
        year_from_value=$2
        shift 2
      fi;;
    --year_to)
      if [ -n "$2" ] && [ ${2:0:1} != "-" ]; then
        year_to_flag=$1
        year_to_value=$2
        shift 2
      fi;;
    --genres)
      if [ -n "$2" ] && [ ${2:0:1} != "-" ]; then
        genres_flag=$1
        genres_value=$2
        shift 2
      fi;;
    *) print_help;
            exit 1;;
  esac
done

if [ -d /result ]; then
  hdfs dfs -rm -R /result/
fi


yarn jar hadoop-streaming-3.2.2.jar -input /tmp/movies.csv \
  -output /result/output \
  -file mapper.py reduce.py \
  -mapper "python3 mapper.py $regexp_flag $regexp_value $year_from_flag $year_from_value $year_to_flag $year_to_value $genres_flag $genres_value" \
  -reducer "python3 reduce.py $n_flag $n_value"