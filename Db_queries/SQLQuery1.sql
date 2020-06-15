--Execute Once to create singup table --
create table singup(userid int constraint pk_user primary key ,username varchar(25)
,email varchar(30),password varchar(20),date_of_creation date,time_of_creation time)

--Execute to view singup table content--
select * from singup

--Execute to remove singup table contents--
truncate table singup

--Execute to remove singup table --
drop table singup

insert into [dbo].[singup] values(123,'arvind','arvind@gmail.com','Arvind@123','2019-10-12','08:10:20')




