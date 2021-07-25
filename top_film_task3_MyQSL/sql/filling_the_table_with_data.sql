
LOAD DATA INFILE 'C:/Program Files/MySQL/data/movies.csv'
INTO TABLE movies
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\r\n'
IGNORE 1 LINES
(movieId, title, genres)
SET movieYear = SUBSTR(REGEXP_SUBSTR(title,'[(|-][0-9]{4}[)]'),2,4),
title = IF(title REGEXP('[(|-][0-9]{4}[)]'), SUBSTR(title,1,LENGTH(title)-6),title);


LOAD DATA INFILE 'C:/Program Files/MySQL/data/ratings.csv'
INTO TABLE ratings
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\r\n'
IGNORE 1 LINES
(@str,movieId, rating, @str1)
