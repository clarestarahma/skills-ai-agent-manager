-- :name get_all_skill_tags
SELECT * FROM skill_tags;

-- :name create_skill_tags
INSERT INTO skill_tags (skill_id, tag) VALUES (:skill_id, :tag);

-- :name update_skill_tags_tag
UPDATE skill_tags SET tag = :tag WHERE skill_id = :skill_id;

-- :name delete_row_skill_tags
DELETE FROM skill_tags WHERE skill_id = :skill_id;