-- Displays tvshows title and tvshow genres
SELECT tv.shows.title, tv.show_genres.genre_id
FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
ORDER BY tv_shows.title ASC, tv_show_genres.genre.id ASC;
