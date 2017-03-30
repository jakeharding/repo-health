create database msr14;

GRANT ALL ON *.* to msr14@localhost IDENTIFIED BY 'msr14';
GRANT ALL ON *.* to msr14@'%' IDENTIFIED BY 'msr14';

FLUSH PRIVILEGES;