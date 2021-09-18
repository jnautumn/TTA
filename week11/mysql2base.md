create database student;
create table student_info(
student_id int not null,
LastName varchar (255),
FirstName varchar (255),
ContactNumber varchar (11),
Qualification varchar (255));
Alter Table student_info
ADD PRIMARY KEY (student_id);
insert into student_info (student_id, LastName, FirstName, ContactNumber, Qualification)
values (1, 'Aaronson', 'Andrew', '07123123123', 'BA Fine Art'),
(2, 'Brown', 'Bobby', '07234234234', 'BA Philosophy'),
(3, 'Charlestone', 'Connie', '07345345345', 'BA Law'),
(4, 'Davidson', 'Darcey', '07456456456', 'BSc Computer Science'),
(5, 'Evans', 'Edward', '07567567567', 'BSc Political Science'),
(6, 'Zeller', 'Zara', '07678678678', 'BA Fine Art'),
(7, 'Young', 'Yvonne', '07891891891', 'BA Journalism'),
(8, 'Xenos', 'Xander', '07912912912', 'BA Law'),
(9, 'Williams', 'Will', '07147147147', 'BA Theatre'),
(10, 'Valentine', 'Victor', '07258258258', 'BA Law');
select * from student_info
