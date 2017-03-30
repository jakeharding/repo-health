create database msr14;

GRANT SELECT, INSERT, DELETE, UPDATE ON msr14.* TO 'msr14'@'%'; 
GRANT SELECT, INSERT, DELETE, UPDATE ON msr14.* TO 'msr14'@'localhost'; 

GRANT ALL ON *.* to msr14@localhost IDENTIFIED BY 'msr14';
GRANT ALL ON *.* to msr14@'%' IDENTIFIED BY 'msr14';

FLUSH PRIVILEGES;