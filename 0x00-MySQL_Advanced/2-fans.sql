-- ranks country origins of bands ordered by number of non unique fans
SELECT origin AS 'origin', COUNT(fans) AS 'nb_fans'
FROM metal_bands
GROUP BY origin
ORDER by COUNT(fans) DESC;
