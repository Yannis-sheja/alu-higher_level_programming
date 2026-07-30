--Lists all cities with their states
SELECT cities.id, cities.name, states.name
FROM cities
JOIN states ON c.state_id = states.id
ORDER BY cities.id ASC;
