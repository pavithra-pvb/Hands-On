-- Gives Error as database constraint is being violated (NOT-NULL)

INSERT INTO professors (firstname, lastname, university_shortname)
VALUES (NULL, 'Miller', 'ETH');