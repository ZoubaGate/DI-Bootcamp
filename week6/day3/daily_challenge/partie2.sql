
create table Book(
	book_id SERIAL PRIMARY KEY,
	title VARCHAR(50) NOT NULL,
	author VARCHAR(50) NOT NULL
);

insert into Book(title,author)
	values('Alice In Wonderland','Lewis Carroll'),
		('Harry Potter', 'J.K Rowling'),
		('To kill a mockingbird', 'Harper Lee');

create table Student(
	student_id SERIAL PRIMARY KEY,
	name varchar(50) NOT NULL UNIQUE,
	age INTEGER,
	CHECK (Age<=15)
);


insert into Student(name,age)
	values('John',12),('Layer',11),('Patrick',10),('Bob',14);

CREATE TABLE Library(
	book_id integer not null,
	student_id integer not null,
	PRIMARY KEY(book_id,student_id),
	FOREIGN KEY (book_id) references Book(book_id) ON DELETE CASCADE ON UPDATE CASCADE,
	FOREIGN KEY (student_id) references Student(student_id) ON DELETE CASCADE ON UPDATE CASCADE,
	borrowed_date date
);

--c'est a partir d'ici L'error
insert into Library
values
	((select book_id from Book where title='Alice In Wonderland'),
	  (select student_id from student where name='John'),
	  '15/02/2022'),
	  ((select book_id from Book where title='To kill a mockingbird'),
	  (select student_id from student where name='Bob'),
	  '03/03/2021'),	  
	  ((select book_id from Book where title='Alice In Wonderland'),
	  (select student_id from student where name='Layer'),
	  '23/05/2021'),
	  ((select book_id from Book where title='Harry Potter'),
	  (select student_id from student where name='Bob'),
	  '12/08/2021');


--Select all the columns from the junction table
select * from library;
--Select the name of the student and the title of the borrowed books
select s.name,b.title from Student s
join Library l on s.student_id=l.student_id
join Book b on l.book_id=b.book_id;
--Select the average age of the children, that borrowed the book Alice in Wonderland
select s.age from Student s
join Library l on s.student_id=l.student_id
join Book b on l.book_id=b.book_id
where b.title='Alice In Wonderland';
--Delete a student from the Student table, what happened in the junction table ?
delete from student where student.name='Layer';
--ON remarque qu'il est supprimer au niveau de la library.

	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	