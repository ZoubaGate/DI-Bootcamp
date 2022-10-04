--Update Statement
--1.)Write a SQL statement to change the following details belonging all employes who’s department_id is 110:
	--email column should be: ‘not available’
	--commission_pct column should be: 0.10
update employees
SET email='not available'
where department_id=110;

--2.)Write a SQL statement which will change the email column of all employees to ‘available’ whom work in the ‘Accounting’ department.
update employees
set email='vailable' from departments where employees.department_id=departments.department_id and	departments.department_name='Accounting';
--3.)Write a SQL statement to change the salary of the employee whose ID is 105. If the existing salary is less than 5000, change it to 8000.
update employees
set salary=8000 
where employee_id=105 and salary<5000;


--Aggregate Functions
--1.)Write a query to find the number of jobs available in the employees table.
select COUNT(DISTINCT job_id) from employees;
--2.)Write a query to get the number of employees working in each post.
select job_title,count(employee_id) from employees,jobs where employees.job_id=jobs.job_id group by job_title;
--3.)Write a query to get the difference between the highest and lowest salaries.
select max(salary)-min(salary) from employees;
--4.)Write a query to find a manager ID and the salary of the lowest-paid employee under that manager.
select manager_id,min(salary)
from employees
where manager_id is not NULL
group by manager_id
order by min(salary) desc;
--5.)Write a query to get the average salary for each post excluding programmer.
select job.job_title,avg(emp.salary)
from employees emp join jobs job
on emp.job_id=job.job_id
where job.job_title!='Programmer'
group by job.job_title;
--6.)Write a query to get the average salary for all departments that employ more than 10 employees.
select dept.department_name,avg(emp.salary),count(emp.employee_id) as Number_employees
from employees emp join departments dept
on emp.department_id=dept.department_id
group by dept.department_name
having count(emp.employee_id)>10;

--Alter Table Statement

--1.)Write a SQL statement to change the name of the column “state_province” to “state” in the locations table, keeping the same data type and size.
Alter table locations
RENAME COLUMN state_province TO state;
--2.)Write a SQL statement to add a primary key to the “location_id” column in the locations table.
--ALTER TABLE locations 
--add primary key(location_id);



	
	
	
	
	
	
	
	
	
	
	
	
	
	
	











