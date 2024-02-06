--Before:

-- Let's add a record to the table
--INSERT INTO transactions (transaction_date, amount, fee) 
--VALUES ('2018-24-09', 5454, '30');

-- Doublecheck the contents
--SELECT *
--FROM transactions;

--After:
-- Let's add a record to the table
INSERT INTO transactions (transaction_date, amount, fee) 
VALUES ('2018-09-24', 5454, '30');

-- Doublecheck the contents
SELECT *
FROM transactions;