create database student;
create table student_info(
student_id int not null,
LastName varchar (255),
FirstName varchar (255),
ContactNumber int,
Qualification varchar (255));
Alter Table student_info
ADD PRIMARY KEY (student_id);
