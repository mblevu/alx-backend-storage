-- creates a stored procedure AddBonus that adds a new correction for a student.
DROP PROCEDURE IF EXISTS AddBonus;
DELIMITER $$
CREATE PROCEDURE AddBonus(
    IN user_id INT,
    IN project_name VARCHAR(255),
    IN score FLOAT)
BEGIN
    DECLARE project_id INT;    
    -- Check if project_name exists in projects table
    IF (SELECT COUNT(*) FROM projects WHERE name = project_name) = 0 THEN
        -- If project_name does not exist, insert it into projects table
        INSERT INTO projects (name) VALUES (project_name);
    END IF;    
    -- Get the project_id for the project_name
    SET project_id = (SELECT id FROM projects WHERE name = project_name LIMIT 1);    
    -- Insert the correction into corrections table
    INSERT INTO corrections (user_id, project_id, score) VALUES(user_id, project_id, score);
END
$$
DELIMITER ;
