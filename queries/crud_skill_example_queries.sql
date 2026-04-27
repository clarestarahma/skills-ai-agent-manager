-- :name get_all_skill_example_queries
SELECT * FROM skill_example_queries;

-- :name create_skill_example_queries
INSERT INTO skill_example_queries (skill_id, query) VALUES (:skill_id, :query);

-- :name update_skill_example_queries_query
UPDATE skill_example_queries SET query = :query WHERE skill_id = :skill_id;

-- :name delete_row_skill_example_queries
DELETE FROM skill_example_queries WHERE skill_id = :skill_id;