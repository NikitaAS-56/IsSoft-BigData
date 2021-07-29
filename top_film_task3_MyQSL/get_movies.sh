#!/bin/bash


function print_help() {
    echo "  ./get-movies.sh [-h] [-n TOPN] [-g GENRES] [-f YEAR_FROM] [-t YEAR_TO] [-r REGEXP]"
    echo "Optional arguments:"
    echo "  -h (help) show help message and exit"
    echo "  -n (topN) Number of top rated movies for each genre"
    echo "  -g (genres)  Filter movies by genre"
    echo "  -f (year_from) Filter movies by year starting from --year_from"
    echo "  -t (year_to)Filter movies by year ending --year_to"
    echo "  -r (regexp) Filter movies by name"
    echo "  -s (setup database) flag for setup db"
    echo "  -H (host) host name for connection to db "
    echo "  -u (user) user name for connection to db "
    echo "  -p (password) user password for connection to db "
    echo "  -d (db) database name for use "
}

function parse_arguments() {
 while getopts "q:n:g:f:t:r:s:h:u:p:d:" flag
    do
        case "${flag}" in
            q) print_help;;

            n) topN=${OPTARG};;

            g) genres=${OPTARG};;

            f) year_from=${OPTARG};;

            t) year_to=${OPTARG};;

            r) regexp=${OPTARG};;

            s) setupdb=1;;

            h) host=${OPTARG};;

            u) user=${OPTARG};;

            p) pass=${OPTARG};;

            d) db=${OPTARG};;

            *)
                exit 1;;
        esac
    done
}



function execute_sql_files() {

    mysql -h $host $db -u$user < sql/Create_data_Base.sql

    mysql -h $host  $db -u$user < sql/Create_movies_table.sql

    mysql -h $host  $db -u$user < sql/Create_ratings_table.sql

    mysql -h $host  $db -u$user < sql/filling_the_table_with_data.sql

    mysql -h $host  $db -u$user < sql/usp_find_top_rated_movies.sql

    mysql -h $host  $db -u$user < sql/view_ratings.sql

}

 function unpacking()
{
	  {
	        curl -O https://files.grouplens.org/datasets/movielens/ml-latest-small.zip
          unzip ml-latest-small.zip
  	} &> /dev/null

   rm ml-latest-small.zip
   mv ml-latest-small/movies.csv data
   mv ml-latest-small/ratings.csv data
   rm -rf  ml-latest-small
}



function construct_command () {
    cmd="python movies_sql.py"

    if [[ -v topN ]]
    then
        cmd="${cmd} -n ${topN}"
    fi

    if [[ -v genres ]]
    then
        cmd="${cmd} -g \"${genres}\""
    fi

    if [[ -v year_from ]]
    then
        cmd="${cmd} -f ${year_from}"
    fi

    if [[ -v year_to ]]
    then
        cmd="${cmd} -t ${year_to}"
    fi

    if [[ -v regexp ]]
    then
        cmd="${cmd} -r ${regexp}"
    fi
}


parse_arguments "$@";

if [[ -v setupdb ]];
then
   unpacking;
   execute_sql_files;
else
    construct_command;
    echo $cmd;
    eval $cmd;
fi



