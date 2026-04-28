-- :name get_all_skills_data
SELECT * FROM skills;

-- :name create_skill
INSERT INTO skills (
  name, 
  description, 
  when_to_use,
  example_queries,
  tags,
  tools,
  instructions, 
  embedding
)
VALUES (
  :name,
  :description,
  :when_to_use,
  regexp_split_to_array(:example_queries, '\n\n'),
  regexp_split_to_array(:tags, '\n\n'),
  regexp_split_to_array(:tools, '\n\n'),
  :instructions,
  :embedding
);

-- :name update_skills_name
UPDATE skills SET name = :name WHERE id = :id;

-- :name update_skills_description
UPDATE skills SET description = :description WHERE id = :id;

-- :name update_skills_when_to_use
UPDATE skills SET when_to_use = :when_to_use WHERE id = :id;

-- :name update_skills_example_queries
UPDATE skills 
SET example_queries = COALESCE(example_queries, '{}') || regexp_split_to_array(:example_queries, '\n\n')
WHERE id = :id;

-- :name update_skills_tags
UPDATE tags 
SET tags = COALESCE(tags, '{}') || regexp_split_to_array(:tags, '\n\n')
WHERE id = :id;

-- :name update_skills_tools
UPDATE tools 
SET tools = COALESCE(tools, '{}') || regexp_split_to_array(:tools, '\n\n')
WHERE id = :id;

-- :name update_skills_instructions
UPDATE skills SET instructions = :instructions WHERE id = :id;

-- :name update_skills_embedding
UPDATE skills SET embedding = :embedding WHERE id = :id;

-- :name delete_skill
DELETE FROM skills WHERE id = :id;