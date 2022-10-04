--Create Tables

--1.)Write a SQL statement to create a simple table “new_countries” including columns country_id and country_name.
	--make sure that no duplicate data is added to the country_id column (which data type should you use for the column country_id ?)
	--make sure that no countries except Italy, India and China will be entered in the table.
/*
CREATE TABLE IF NOT EXISTS new_countries(
	country_id integer NOT NULL,
	country_name varchar(40) NOT NULL,
	UNIQUE(country_id),
	check(country_name in ('Italy', 'India','China'))
);

*/
--2.)Write a SQL statement to create a duplicate copy of the “new_countries” table including the structure and the data of the “new_countries” table.
/*
CREATE TABLE IF NOT EXISTS dup_countries as 
select * from new_countries;
*/
--3.)Write a SQL statement to create a table named “new_jobs” including columns job_id, job_title, min_salary, max_salary
	--make sure that the max_salary column won’t exceed 25000.
	--make sure that job_title, min_salary and max_salary have the following default values:
	--job_title is blank
	--min_salary is 8000
	--max_salary is NULL.
/*
create table new_jobs(
	job_id VARCHAR(10) NOT NULL UNIQUE, 
	job_title varchar(35) DEFAULT ' ',
	min_salary decimal(6,0) DEFAULT 8000,
	max_salary decimal(6,0) DEFAULT NULL,
	check(max_salary < 25000)
);
*/
--4.)Write an SQL statement to create a table called “new_employees” the table should include the following columns: employee_id, first_name, last_name, email, phone_number hire_date, job_id and salary.
     --make sure that, the employee_id column does not contain any duplicate value at the time of insertion,
     --make sure that the foreign key column job_id, references the column job_id in the “new_jobs” table.
/*
create table new_employees(
	employee_id varchar(5) unique,
	first_name varchar(50),
	last_name varchar(50),
	email varchar(30),
	phone_number varchar(10) default null,
	hire_date date not null,
	job_id varchar(10) NOT NULL,
	salary decimal(6,0),
	foreign key(job_id) references new_jobs(job_id)
	
);
*/











