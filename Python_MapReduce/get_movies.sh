#!/bin/bash

 cat movies.csv | python mapper.py --year_from 1993 --year_to 2010 --genre "War|Western" --regexp The | python redyce.py

while  (("$#")); do
  case "$1" in
    --help)
        echo "Help"
        exit 1
        ;;
    --N)
      if [-v "$2"] && [${2:0:1}  !="-"]; then
        n_flag=$1
        n_value=$2
        echo "$1 $2"
        shift 2

      else
          echo "Eror1 $1"
            echo "$1 $2"
          exit 1
          fi ;;

    --year_from)
      if [-v "$2"] && [${2:0:1}  !="-"]; then
        yf_flag=$1
        yf_value=$2
          echo "$1 $2"
        shift 2

      else
          echo "Eror2"
            echo "$1 $2"
          exit 1
          fi ;;

    --year_to)
      if [-v "$2"] && [${2:0:1}  !="-"]; then
        yt_flag=$1
        yt_value=$2
          echo "$1 $2"
        shift 2

      else
          echo "Eror3"
            echo "$1 $2"
          exit 1
          fi ;;

    --regexp)
      if [-v "$2"] && [${2:0:1}  !="-"]; then
        rg_flag=$1
        rg_value=$2
          echo "$1 $2"
        shift 2

      else
          echo "Eror4"
            echo "$1 $2"
          exit 1

          fi ;;

    --genres)
      if [-v "$2"] && [${2:0:1}  !="-"]; then
        g_flag=$1
        g_value=$2
          echo "$1 $2"
        shift 2

      else
          echo "Eror5 "
            echo " \"$2\" "
          exit 1
          fi ;;
    *)
        exit 1
        ;;
    esac
done

cat movies.csv \
|python mapper.py $yf_flag $yf_value $yt_flag $yt_value $rg_flag $rg_value $g_flag \"$g_value\" \
|python redyce.py $n_flag $n_value