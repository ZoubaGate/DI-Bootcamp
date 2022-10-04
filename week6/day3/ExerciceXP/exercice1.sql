--Exercise 1: DVD Rental

--Get a list of all film languages.
select * from language;
--2.)Get a list of all films joined with their languages – select the following details : film title, description, and language name. 
select f.title,f.description, l.name from film f inner join language l on f.language_id=l.language_id;
--3.)Create a new table called new_film with the following columns : id, name. Add some new films to the table.
/*
create table new_film(
	id serial primary key,
	name varchar(50) not null
);
*/
insert into new_film(name) values('Antitrust Tomatoes'),('Balloon Homeward'),('BadmanDawn'),('Blackout Private'),('Boogie Amelie'),('Candles Grapes'),('Cider Desire'),('Crusade Honey'),('Deep Crusade');
--4.)Create a new table called customer_review, which will contain film reviews that customers will make.
/*create table customer_review(
	review_id serial primary key,
	film_id INTEGER REFERENCES new_film(id) ON DELETE CASCADE,
	language_id INTEGER REFERENCES language(language_id) ON DELETE CASCADE,
	title_review varchar(50),
	score INTEGER,
	review_text TEXT,
	last_update DATE
);*/
--5.)Add 2 movie reviews. Make sure you link them to valid objects in the other tables.
insert into customer_review(film_id,language_id,title_review,score,review_text,last_update)
values((SELECT id from new_film where name='Crusade Honey' LIMIT 1),(select language_id from language where name='English' limit 1),'cool',8,'this film very cool.','20-09-2012');

--6.)Delete a film that has a review from the new_film table, what happens to the customer_review table?
	--on remarque que la donnée correspondant au ID dans la table customer_review est aussi supprimer







