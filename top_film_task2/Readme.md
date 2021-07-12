# Top MovieLens


This script allows user to get information about top rated films.



## Parameters

*  `--help` show help message and exit
*  `-N`,  the number of top rated movies for each genre. *(3)*
*   `--genres` user-defined genre filter. can be multiple. *("Comedy|Adventure")
*   `--year_from` the lower boundary of year filter *( 1980)*
*   `--year_to` the lower boundary of year filter *(2010)*
*   `--regexp` filter on name of the film *(love)*
 
## Usage

### Get top N ranked movies

Use `--N` parameter to get top N ranked movies, for example, following command returns top 2 films:
```
python movies.py -n 2
```
Output:
```
movieId,title,genres,year,rating
100556,Act of Killing, The,Documentary,2012,5.0
100906,Maniac Cop 2,Action|Horror|Thriller,1990,5.0
```

###  Search by title
Pass RegEx as a argument of `--regexp` to search by movie title.

For example, to get  top 3 films about "Monster" use command:
```
python movies.py --N 3 --regexp Monster
```
Output:
```
movieId, title, genres, year, rating
136353,Scooby-Doo! and the Loch Ness Monster (),Animation|Children|Comedy,2004,5.0
4135,Monster Squad, The (),Adventure|Comedy|Horror,1987,5.0
85295,Scooby-Doo! Curse of the Lake Monster (),Adventure|Children|Comedy|Mystery,2010,5.0

```

### Filter by year
Use `--year_from` and `year_to` to determinate movie\`s year range.

```
python movies.py --N 4  --year_from 2001 --year_to 2002
```
Output:
```movieId, title, genres, year, rating
27373,61* (),Drama,2001,5.0
27523,My Sassy Girl (Yeopgijeogin geunyeo) (),Comedy|Romance,2001,5.0
44943,9/11 (),Documentary,2002,5.0
5328,Rain (),Drama|Romance,2001,5.0
```

###  Top films for each genre
Specify `--genres` argument in order to get top ranked films for each genre category.

```
python movies.py --N 4 --year_from 2000 --genres "Romance|Drama"
```
Output:
```
movieId, title, genres, year, rating
107771,Only Lovers Left Alive (),Drama|Horror|Romance,2013,5.0
108078,Chinese Puzzle (Casse-tГЄte chinois) (),Comedy|Romance,2013,5.0
109633,Garden of Words, The (Koto no ha no niwa) (),Animation|Romance,2013,5.0
113829,One I Love, The (),Comedy|Drama|Romance,2014,5.0
107771,Only Lovers Left Alive (),Drama|Horror|Romance,2013,5.0
112512,Colourful (Karafuru) (),Animation|Drama|Fantasy|Mystery,2010,5.0
113829,One I Love, The (),Comedy|Drama|Romance,2014,5.0
120130,Into the Forest of Fireflies' Light (),Animation|Drama|Fantasy,2011,5.0

```
