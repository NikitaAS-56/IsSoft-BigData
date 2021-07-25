
DROP VIEW IF EXISTS view_ratings;
CREATE VIEW view_ratings AS
    SELECT
        m.movieId,
        m.title,
        m.genres,
        m.movieYear,
        round(AVG(r.rating),2) AS 'rating'
    FROM
        movies_table AS m_t
    INNER JOIN ratings_table AS r_t ON m_t.movieId = r_t.movieId
    GROUP BY
        m_t.movieId,
        m_t.title,
        m_t.genres,
        m_t.movieYear;