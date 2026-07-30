--Lists all cities with their states
SELECT c.id, c.name, s.name
FROM cities
JOIN states ON c.state_id = s.id
ORDER BY c.id ASC;
