-- :name get_full_skills_data
SELECT 
    s.id,
    s.name,
    s.description,
    s.when_to_use,
    s.instructions,
    t.tag,
    st.tool,
    q.query
FROM skills s
LEFT JOIN skill_tags t ON s.id = t.skill_id
LEFT JOIN skill_tools st ON s.id = st.skill_id
LEFT JOIN skill_example_queries q ON s.id = q.skill_id;