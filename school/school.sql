drop table if exists Privilege;
create table Privilege (
    privilegeId integer primary key autoincrement,
    privilegeName varchar(20) not null
);

insert into Privilege (privilegeName) values ("admin");
insert into Privilege (privilegeName) values ("saodo");
insert into Privilege (privilegeName) values ("loptruong");

drop table if exists User;
create table User (
    userId integer primary key autoincrement,
    username varchar(100) not null,
    -------------------------------------------
    userPasswordHash char(60) not null, -- using bcrypt 60 chars, python bcrypt
    -------------------------------------------
    privilegeId integer not null,
    foreign key (privilegeId) references Privilege(privilegeId)
);

insert into User (username, userPasswordHash, privilegeId)
    values ("admin", "$2b$12$rWuHFkxmKZkLE1lfBLsWnOEhLXdh7gxLh4K50fkBnpsbY65JUdzOe", 1);

drop table if exists NeNep;
create table NeNep (
    day date not null,
    saodoId integer not null,
    ------------------------------------
    siso int not null, 
    dongphuc int not null,
    khanquang int not null,
    truybai int not null,
    chaoco int not null,
    vesinh int not null,
    bakhong int not null,
    shdoi int not null,
    tdabc int not null,
    nghithucdoi int not null,
    ghichu varchar(100) not null,
    ------------------------------------
    primary key (day),
    foreign key (saodoId) references User (userId)
);

drop table if exists HocTap;
create table HocTap (
    day date not null,
    loptruongId integer not null,
    ------------------------------------
    gioTot int not null,
    gioKha int not null,
    gioTB int not null,
    ------------------------------------
    diemGioi int not null,
    diemKha int not null, 
    diemTB int not null, 
    diemYeu int not null,
    diemKem int not null,
    ------------------------------------
    primary key (day),
    foreign key (loptruongId) references User (userId)
);
