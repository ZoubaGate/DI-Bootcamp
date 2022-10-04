/*
Exercise 1 : Items And Customers
Instructions
We will work on the public database that we created yesterday.

Use SQL to get the following from the database:
1.)All items, ordered by price (lowest to highest).
2.)Items with a price above 80 (80 included), ordered by price (highest to lowest).
3.)The first 3 customers in alphabetical order of the first name (A-Z) – exclude the primary key column from the results.
4.)All last names (no other columns!), in reverse alphabetical order (Z-A)
*/
select * from items order by price asc;
select * from items where price > 80 order by price desc;

select first_name,last_name from customers order by first_name LIMIT 3;
select last_name from customers order by last_name desc;
