--Execute Once to create singup table --
create table singup(userid int identity constraint pk_user primary key ,username varchar(25)
,email varchar(30),password varchar(20),date_of_creation date,time_of_creation time)

--Execute to view singup table content--
select * from singup

--Execute to remove singup table contents--
truncate table singup

--Execute to remove singup table --
drop table singup

delete from [dbo].[singup] where userid=4



