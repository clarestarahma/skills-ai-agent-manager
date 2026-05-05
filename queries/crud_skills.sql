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
  embedding
)
VALUES (
  :name,
  :description,
  :when_to_use,
  (SELECT array_agg(DISTINCT x) FROM unnest(regexp_split_to_array(:example_queries, '\n\n')) x WHERE x <> ''),
  (SELECT array_agg(DISTINCT x) FROM unnest(regexp_split_to_array(:tags, '\n\n')) x WHERE x <> ''),
  (SELECT array_agg(DISTINCT x) FROM unnest(regexp_split_to_array(:tools, '\n\n')) x WHERE x <> ''),
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
SET example_queries = regexp_split_to_array(:example_queries, '\n\n')
WHERE id = :id;

-- :name update_skills_tags
UPDATE skills 
SET tags = regexp_split_to_array(:tags, '\n\n')
WHERE id = :id;

-- :name update_skills_tools
UPDATE skills 
SET tools = (
    SELECT array_agg(DISTINCT x) 
    FROM unnest(regexp_split_to_array(:tools, '\n\n')) x 
    WHERE x <> ''
)
WHERE id = :id;

-- :name update_skills_embedding
UPDATE skills SET embedding = :embedding WHERE id = :id;

-- :name delete_skill
DELETE FROM skills WHERE id = :id;