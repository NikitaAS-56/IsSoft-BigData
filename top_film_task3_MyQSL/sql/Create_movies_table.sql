DROP TABLE IF EXISTS movies;
CREATE TABLE movies (
  movieId int(20) ,
  title varchar(256) NOT NULL,
  genres varchar(256) DEFAULT NULL,
  movieYear int(11)
) ;
