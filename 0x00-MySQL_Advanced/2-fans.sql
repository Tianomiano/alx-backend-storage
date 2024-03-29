-- SQL script that ranks country origins of bands,
-- ordered by the number of (non-unique) fans
-- script can be executed on any database
SELECT origin, SUM(fans) as nb_fans from metal_bands
GROUP BY origin ORDER BY nb_fans DESC;
