
DROP VIEW IF EXISTS view_ratings;
CREATE VIEW view_ratings AS
    SELECT
        m.movieId,
        m.title,
        m.genres,
        m.movieYear,
        round(AVG(r.rating),2)AS 'rating'
    FROM
        movies AS m
    INNER JOIN ratings AS r ON m.movieId = r.movieId
    GROUP BY
        m.movieId,
        m.title,
        m.genres,
        m.movieYear;