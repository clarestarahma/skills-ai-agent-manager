-- :name get_all_skills_data
SELECT * FROM skills;

-- :name create_skill
INSERT INTO skills (name, description, metadata, when_to_use, instructions, embedding)
VALUES (
  :name,
  :description,
  :metadata,
  :when_to_use,
  :instructions,
  :embedding
);

-- :name update_skill_name
UPDATE skills SET name = :name WHERE id = :id;

-- :name update_skill_description
UPDATE skills SET description = :description WHERE id = :id;

-- :name update_skill_when_to_use
UPDATE skills SET when_to_use = :when_to_use WHERE id = :id;

-- :name update_skill_instructions
UPDATE skills SET instructions = :instructions WHERE id = :id;

-- :name update_skill_embedding
UPDATE skills SET embedding = :embedding WHERE id = :id;

-- :name delete_row_skills
DELETE FROM skills WHERE id = :id;