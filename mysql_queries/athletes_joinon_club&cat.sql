USE odtu_ori;

SELECT
	c.name,
    a.first_name,
    a.last_name,
    a.si,
    a.email,
    a.sex,
    a.born,
    cat.short_name
FROM clubs c
JOIN athletes a
	ON c.id = a.club_id
JOIN categories cat
	ON a.category_id = cat.id