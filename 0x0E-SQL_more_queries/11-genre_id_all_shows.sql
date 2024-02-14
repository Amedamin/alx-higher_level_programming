-- Behold! An epic saga of shows awaits within the realms of hbtn_0d_tvshows.
-- Embark on this journey to discover the enchanting fusion of titles and genres.
SELECT 
    tv_shows.title 
    tv_show_genres.genre_id
FROM 
    tv_shows 
LEFT JOIN 
    tv_show_genres 
ON 
    tv_shows.id = tv_show_genres.show_id
ORDER BY 
    tv_shows.title ASC, 
    tv_show_genres.genre_id ASC;
