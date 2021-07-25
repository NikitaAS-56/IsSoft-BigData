CREATE DEFINER=`root`@`localhost` PROCEDURE `usp_find_top_rated_movies`(
    IN n INT,
    IN `regexp` VARCHAR(200),
    IN year_from INT,
    IN year_to INT,
    IN genres VARCHAR(256)
)
BEGIN

        with cte_1 as(
            with cte as (
                    SELECT * FROM view_ratings )
            SELECT
                   movieId,
                   title,
                   mn.genre,
                   movieYear,
                   rating,
                   t.genres
            from cte as t

            join json_table (
                replace (json_array(t.genres),'|','","'),
                '$[*]' columns (genre varchar(50) path '$')
            ) as mn
            )
        SELECT movieId, title , movieYear, rating, m.genres from  cte_1 as m

        WHERE
            ((year_from IS NULL) OR (m.movieYear >= year_from))
            AND ((year_to IS NULL) OR (m.movieYear <= year_to))
            AND ((`regexp` IS NULL) OR (REGEXP_SUBSTR(m.title,`regexp`) != ''))
            AND REGEXP_SUBSTR(m.genre, genres) != ''
        ORDER BY m.rating DESC, m.movieYear DESC LIMIT n;
END