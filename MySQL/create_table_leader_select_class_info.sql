
create table selectclassinfo(
 	stuno varchar(15) not null,
 	stuname varchar(30) not null,
 	stucollege varchar(50) not null,
 	leader varchar(30) not null,
 	stuweek varchar(10) not null,
 	stukeshi varchar(10) not null,
 	telphone varchar(13) not null,
 	qq varchar(12),
 	datetime timestamp not null default CURRENT_TIMESTAMP,
	number int not null
)ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- select * from selectclassinfo;

-- update selectclassinfo set number=1 where stuname='roger';

-- alter table selectclassinfo change stucollege stucollege varchar(50);

-- delete from selectclassinfo where stuname='';

-- update selectclassinfo set number=number-1 where number > 10;
