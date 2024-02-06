--Before:

-- Calculate the net amount as amount + fee
--SELECT transaction_date, amount + fee AS net_amount 
--FROM transactions;

--After:
-- Calculate the net amount as amount + fee
SELECT transaction_date, amount + CAST(fee AS integer) AS net_amount 
FROM transactions;