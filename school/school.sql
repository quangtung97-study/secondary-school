drop database if exists school;

create database school;

use school;

drop table if exists Privilege;
create table Privilege (
    privilegeName varchar(20) not null,
    primary key (privilegeName)
);

insert into Privilege (privilegeName) values ("admin");
insert into Privilege (privilegeName) values ("saodo");
insert into Privilege (privilegeName) values ("loptruong");

drop table if exists User;
create table User (
    username varchar(50) not null,
    userPasswordHash char(60) not null, -- using bcrypt 60 chars, python bcrypt
    privilegeName varchar(20) not null,
    primary key (username),
    foreign key (privilegeName) references Privilege(privilegeName)
);

insert into User (username, userPasswordHash, privilegeName)
    values ("admin", "$2b$12$rWuHFkxmKZkLE1lfBLsWnOEhLXdh7gxLh4K50fkBnpsbY65JUdzOe", "admin");

drop table if exists Class;
create table Class (
    className varchar(5) not null,
    primary key (className)
);


create table Monitoring (
    lopTruong varchar(50) not null,
    className varchar(5) not null,
);

drop table if exists NeNep;
create table NeNep (
    ngay char(10) not null,
    className varchar(5) not null
    saoDo varchar(50) not null,

    siSo int not null, 
    dongPhuc int not null,
    khanQuang int not null,
    truyBai int not null,
    chaoCo int not null,
    veSinh int not null,
    baKhong int not null,
    shDoi int not null,
    tdabc int not null,
    nghiThucDoi int not null,
    ghiChu varchar(100) not null,

    primary key (day, className),
    foreign key (className) references Class (className),
    foreign key (saoDo) references User (username)
);

drop table if exists HocTap;
create table HocTap (
    day date not null,
    lopTruong varchar(50) not null,

    gioTot int not null,
    gioKha int not null,
    gioTB int not null,

    diemGioi int not null,
    diemKha int not null, 
    diemTB int not null, 
    diemYeu int not null,
    diemKem int not null,

    primary key (day),
    foreign key (lopTruong) references User (username)
);
