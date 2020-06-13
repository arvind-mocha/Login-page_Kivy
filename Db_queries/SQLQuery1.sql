create table singup(username varchar(25)constraint pk_user primary key ,email varchar(30)
,password varchar(20),date_of_creation date,time_of_creation time)

select * from singup

truncate table singup
