-- Listing all cities in the database hbtn_0d_usa.
-- ordering data in ascending ids.
SELECT `id`, `name`
  FROM `cities`
 WHERE `state_id` IN
       (SELECT `id`
	  FROM `states`
	 WHERE `name` = "California")
 ORDER BY `id`;
