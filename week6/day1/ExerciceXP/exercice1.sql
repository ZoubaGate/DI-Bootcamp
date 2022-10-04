/*
All the items.
All the items with a price above 80 (80 not included).
All the items with a price below 300. (300 included)
All customers whose last name is ‘Smith’ (What will be your outcome?).
All customers whose last name is ‘Jones’.
All customers whose firstname is not ‘Scott’.
*/
select * from items;
select * from items where price > 80;
select * from items where price <300;
select * from customers where last_name='Smith'; /*there is no body*/
select * from customers where last_name='Jones';
select * from customers where first_name!='Scott'