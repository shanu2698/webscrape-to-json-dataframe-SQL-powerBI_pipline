show databases;

create database presentation;
use presentation;
show tables;
select * from customer_details_table

drop table flipkart_table;
drop table flipkarttable;
drop table testtable2;
drop table twitter_table;
drop table twittertable;
drop table customer_details_table;
drop table order_details_table;
drop table twitter_table;

SELECT @@SERVERNAME

select suser_name() 
SELECT SYSTEM_USER

use tempDB 
GO;
with getPermissions as ( SELECT * FROM fn_my_permissions (NULL, 'DATABASE') ) 
select permission_name from getPermissions 
where permission_name like 'create%' 
GO
