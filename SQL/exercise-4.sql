-- Create a table for the professors entity type
CREATE TABLE professors (
 firstname text,
 lastname text
);

CREATE TABLE universities (
    university_shortname text,
    university text,
    university_city text
);

-- Print the contents of this table
SELECT * 
FROM professors