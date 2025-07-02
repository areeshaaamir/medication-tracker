-- SQLite
create table users(
  userID integer primary key AUTOINCREMENT,
  username varchar(50) not null,
  age integer not null,
  weight decimal(5, 2),
  gender varchar(50) DEFAULT 'prefer not to say',
  password varchar(10) not null,
  email varchar(50) not null unique
);

create table medicines(
  medID integer primary key AUTOINCREMENT,
  medName varchar(100) not null,
  dosage_mg int not null,
  quantity int not null,
  start_date date,
  end_date date,
  reminder_enabled boolean,
  userID integer,
  FOREIGN KEY (userID) REFERENCES users(userID)
);

select * from users;
select * from medicines;
delete from users
where username = "arewwsha";

select * from medicines
where userID=3;

create table medicines(
  medID integer primary key AUTOINCREMENT,
  medName varchar(100) not null,
  dosage_mg int not null,
  quantity int not null,
  start_date date,
  end_date date,
  reminder_enabled boolean,
  userID integer,
  FOREIGN KEY (userID) REFERENCES users(userID)
);
  
create table reminders(
  id integer primary key AUTOINCREMENT,
  time text,
  medID integer,
  foreign key(medID) REFERENCES medicines(medID)
);

select * from reminders;
