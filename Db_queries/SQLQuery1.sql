--Execute Once to create table --
create table singup(userid int constraint pk_user primary key ,username varchar(25)
,email varchar(30),password varchar(20),date_of_creation date,time_of_creation time)

create table singin(userid int constraint fk_uid foreign key references singup(userid),logged_in_as varchar(20)
,time_of_login time,date_of_login date)

create table singupdummy(username varchar(20),password varchar(20)) 

--Execute to view singup table content--
select * from singup

select * from singin 

select * from singupdummy








