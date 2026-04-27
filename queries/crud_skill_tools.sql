-- :name get_all_skill_tools
SELECT * FROM skill_tools;

-- :name create_skill_tools
INSERT INTO skill_tools (skill_id, tool) VALUES (:skill_id, :tool);

-- :name update_skill_tools_tool
UPDATE skill_tools SET tool = :tool WHERE skill_id = :skill_id;

-- :name delete_row_skill_tools
DELETE FROM skill_tools WHERE skill_id = :skill_id;