/*create table customer(
	customer_id serial primary key,
	first_name varchar(50) not null,
	last_name varchar(50) not null
);
create table customer_profile(
	profile_id INTEGER NOT NULL,
	isLoggedIn bool DEFAULT false,
	primary key(profile_id),
	constraint customer_id foreign key (profile_id) references customer(customer_id)
);
John, Doe
Jerome, Lalu
Lea, Rive
*/
/*
insert into customer(first_name,last_name)
	values('Doe','John'),('Lalu','Jerome'),('Rive','Lea');

insert into customer_profile(profile_id,isLoggedIn)
	values(1,true),(2,false);
*/
--The first_name of the LoggedIn customers
select last_name from customer c inner join customer_profile p on c.customer_id=p.profile_id;
--All the customers first_name and isLoggedIn columns - even the customers those who don’t have a profile.
select c.first_name,p.isLoggedIn from customer c left outer join customer_profile p on c.customer_id=p.profile_id;
--The number of customers that are not LoggedIn
select count(*) from customer c inner join customer_profile p on c.customer_id=p.profile_id and p.isLoggedIn=false;
















