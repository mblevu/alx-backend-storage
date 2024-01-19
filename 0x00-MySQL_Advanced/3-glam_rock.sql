-- lists all bands with glam rock as main style ranked by longetivity
SELECT band_name AS bandname, IF NULL(split, 2022) - IF NULL(formed, 0) AS lifespan
FROM metal_bands
WHERE style LIKE '%Glam rock%'
ORDER by lifespan DESC;
