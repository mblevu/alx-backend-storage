-- lists all bands with glam rock as main style ranked by longetivity
SELECT band_name AS 'band_name',
        (CASE
            WHEN split IS NOT NULL THEN split - formed
            ELSE 2022 - formed
        END) as 'lifespan'
FROM metal_bands
WHERE style = 'Glam rock'
ORDER by lifespan DESC;
