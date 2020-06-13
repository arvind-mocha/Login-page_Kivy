--Execute Once to create singin table --
create table Singin(userid int constraint fk_uid foreign key references [dbo].[singup](userid) ,
logged_in_as varchar(30),time_of_login time,date_of_login date)

--Execute to view singin table content--
select * from [dbo].[Singin]

--Execute to remove singup table contents--
truncate table [dbo].[Singin]

--Execute to remove singup table --
drop table [dbo].[Singin]