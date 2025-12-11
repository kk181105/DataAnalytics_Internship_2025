
-- Task 3: Queries for Netflix dataset

-- 1. Show all movies
SELECT * FROM netflix WHERE content_type = 'Movie';

-- 2. Count of Movies vs TV Shows
SELECT content_type, COUNT(*) AS total FROM netflix GROUP BY content_type;

-- 3. Number of titles per country (top 10)
SELECT country, COUNT(*) AS total_titles FROM netflix GROUP BY country ORDER BY total_titles DESC LIMIT 10;

-- 4. Top 10 directors with most titles
SELECT director, COUNT(*) AS total_titles FROM netflix WHERE director IS NOT NULL AND director <> 'Unknown' GROUP BY director ORDER BY total_titles DESC LIMIT 10;

-- 5. Average movie duration (minutes) - requires numeric extraction
SELECT AVG(CAST(REGEXP_REPLACE(duration_raw, '[^0-9]', '') AS INTEGER)) AS avg_duration FROM netflix WHERE content_type = 'Movie' AND duration_raw LIKE '%min%';

-- 6. Ratings distribution
SELECT rating, COUNT(*) AS total FROM netflix GROUP BY rating ORDER BY total DESC;

-- 7. Most common genres (listed_in)
SELECT listed_in, COUNT(*) AS total FROM netflix GROUP BY listed_in ORDER BY total DESC LIMIT 15;

-- 8. Movies longer than average duration (subquery)
SELECT title, duration_raw FROM netflix WHERE content_type='Movie' AND CAST(REGEXP_REPLACE(duration_raw, '[^0-9]', '') AS INTEGER) > (
    SELECT AVG(CAST(REGEXP_REPLACE(duration_raw, '[^0-9]', '') AS INTEGER)) FROM netflix WHERE content_type='Movie' AND duration_raw LIKE '%min%'
);

-- 9. Create a view: content_by_year
CREATE VIEW content_by_year AS SELECT release_year, COUNT(*) AS total_titles FROM netflix GROUP BY release_year;

-- 10. Index suggestions (syntax varies by engine)
-- SQLite example:
-- CREATE INDEX idx_content_type ON netflix(content_type);
