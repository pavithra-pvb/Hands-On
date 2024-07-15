-- Rename the university_shortname column to id
ALTER TABLE universities
RENAME COLUMN university_shortname TO id;


-- Make id a primary key
ALTER TABLE universities
ADD CONSTRAINT university_pk PRIMARY KEY (id);