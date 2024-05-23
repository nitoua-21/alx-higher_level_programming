-- script that lists all shows without the genre Comedy in the database hbtn_0d_tvshows.
-- The tv_genres table contains only one record where name = Comedy (but the id can be different)
-- Each record should display: tv_shows.title
-- Results must be sorted in ascending order by the show title
SELECT DISTINCT
    tv_shows.title
FROM
    tv_shows
    LEFT JOIN tv_show_genres ON tv_show_genres.show_id = tv_shows.id
    LEFT JOIN tv_genres ON tv_genres.id = tv_show_genres.genre_id
WHERE
    tv_shows.title NOT IN (
        SELECT
            tv_shows.title
        FROM
            tv_shows
            LEFT JOIN tv_show_genres ON tv_show_genres.show_id = tv_shows.id
            LEFT JOIN tv_genres ON tv_genres.id = tv_show_genres.genre_id
        WHERE
            tv_genres.name = "Comedy"
    )
ORDER BY
    1 ASC;
    