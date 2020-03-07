/*
 * Instagtam network database. 
 * The database collects information about the user , stores photos, videos, and stories. 
 * You can also track direct messages and subscriptions.
*/

drop database if exists insta;
create database insta;
use insta;

drop table if exists users;
create table users(
	id serial primary key,
	user_name varchar(100),
	name varchar(100),
	website varchar(100),
	bio varchar(100),
	password_hash varchar(100),
	index user_name_idx(user_name),
	index name_idx(name)
);

insert into users (user_name, name, bio) values
	('koberman.png', 'Veraslav Koberman', 'Blogger, 19 y.o., Surgut\Tyumen'),
	('otvergayushchiy', 'E.Korf', '21.1999'),
	('kira_nemova00', 'kira', ''),
	('mr.sarkazi', 'Ivan Sergeevich', 'smile'),
	('kiaoso', 'Konstantin', 'barista 24/7');

delimiter //
create trigger users_id before insert on users
for each row
begin
	declare cat_id int ;
	select id into cat_id from users order by id limit 1 ;
	set new.id = coalesce (new.id, cat_id);
end //
delimiter ;
select @users_id;

drop table if exists profile_info;
create table profile_info(
	id serial primary key,
	page varchar(100),
	category varchar(100),
	contact_options varchar(100),
	
	index id_idx(id),
	index contact_options_idx(contact_options),
	
	foreign key (id) references users(id)
);

insert into profile_info (page, category) values
	('Vera Koberman', 'Blogger'),
	('Ekaterina Korf', 'Artist'),
	('Kira Nemova', 'Author'),
	('Ivan', '-'),
	('Konstantin Kashin', 'Chef');

select
	u.id, u.user_name, u.name, u.bio,
	(select
		p_i.category
	from 
		profile_info p_i
	where
		p_i.id = u.id)
from
	users u;

drop table if exists contact_option;
create table contact_option(
	id serial primary key,
	b_email varchar(100) unique,
	phone varchar(12),
	
	index b_email_idx(b_email),
	index id_idx(id),
	index phone_idx(phone),
	
	foreign key (id) references users(id)
);

insert into contact_option (b_email, phone) values
	('evtukovavera@mail.ru', '89825017522'),
	('korf99@mail.ru', '89227981097'),
	('nemova_@mail.ru', '89519797285'),
	('sarkazi96@mail.ru', '89124162024'),
	('k.konstantin@mail.ru', '89505106335');

select 
	u.id, u.user_name,
	(select
		c_o.phone
	from
		contact_option c_o
	where
		c_o.id = u.id) as phone
from users u;

select
	*
from
	users join contact_option;
	
drop table if exists admin_contact_info;
create table admin_contact_info(
	id serial primary key,
	email varchar(100) unique,
	phone varchar(12),
	gender varchar(1),
	
	index phone_idx(phone),
	index id_idx(id),
	
	foreign key (phone) references contact_option(phone),
	foreign key (id) references users(id)
);

insert into admin_contact_info(email, phone, gender) values
	('evtukovavera@mail.ru', '89825017522', 'f'),
	('korf99@mail.ru', '89227981097', 'f'),
	('nemova_@mail.ru', '89519797285', 'f'),
	('sarkazi96@mail.ru', '89124162024', 'm'),
	('k.konstantin@mail.ru', '89505106335', 'm');
	
drop table if exists media_types;
create table media_types(
	id serial primary key,
    name varchar(255),
    created_at datetime default now(),
    updated_at datetime default current_timestamp on update current_timestamp
);

insert into media_types(id, name) values
	('1', 'photo'),
	('2', 'video'),
	('3', 'text');

drop table if exists media;
create table media(
	id serial primary key,
    media_type_id bigint unsigned not null,
    user_id bigint unsigned not null,
  	body text,
    created_at datetime default now(),
    updated_at datetime default current_timestamp on update current_timestamp,
   
	index media_id_idx(id),
    index id_idx(id),
    
    foreign key (user_id) references users(id),
    foreign key (media_type_id) references media_types(id)
);

insert into media(media_type_id, user_id, body) values
	('1', '1', 'With ma'),
	('1', '1', '<3'),
	('1', '1', ''),
	('1', '2', 'shizoid'),
	('2', '2', ''),
	('1', '3', ''),
	('1', '3', 'beautiful day today'),
	('1', '4', '^^');

select
	m_t.id, m_t.name, m.*
from
	media_types m_t
left join 
	media m 
using (id);
	
drop table if exists stories;
create table stories(
	id serial primary key,
	user_id bigint unsigned not null,
	created_at datetime default now(),
	media_type_id bigint unsigned not null,
	
	index stories_id_idx(id),
	index id_idx(id),
    
	foreign key (user_id) references users(id),
	foreign key (media_type_id) references media_types(id)
);

insert into stories(user_id, media_type_id) values
	('1', '1'),
	('1', '2'),
	('1', '3'),
	('2', '1'),
	('2', '2'),
	('2', '2'),
	('3', '1'),
	('4', '1');

select 
	user_id, media_type_id
from 
	stories
group by
	user_id;

select
	m_t.id, m_t.name, s.*
from
	media_types m_t
right join 
	stories s
using (id);

drop table if exists direct;
create table direct(
	id serial primary key,
	from_user_id bigint unsigned not null,
    to_user_id bigint unsigned not null,
    body text,
    created_at datetime default now(),
    
    index messages_from_user_id_idx(from_user_id),
    index messages_to_user_id_idx(to_user_id),
    index id_idx(id),
    
    foreign key (to_user_id) references users(id),
    foreign key (from_user_id) references users(id)
);

insert into direct(from_user_id, to_user_id, body) values
	('1', '2', 'hi'),
	('2', '1', 'hi, how are you?'),
	('1', '3', 'send me your number'),
	('3', '5', 'watch out'),
	('5', '1', 'hi');
	
drop table if exists likes;
create table likes(
	id serial primary key,
    user_id bigint unsigned not null,
    to_user_id bigint unsigned not null,
    media_id bigint unsigned not null,
    created_at datetime default now(),
    
    index id_idx(id),
    
    foreign key (user_id) references users(id),
    foreign key (to_user_id) references users(id),
    foreign key (media_id) references media_types(id)
);

insert into likes(user_id, to_user_id, media_id) values
	('1', '2', '1'),
	('1', '2', '1'),
	('1', '3', '1'),
	('1', '3', '2'),
	('1', '3', '2'),
	('2', '1', '1'),
	('3', '1', '1'),
	('4', '1', '1');

drop table if exists follow_requests;
create table follow_requests(
	id serial primary key,
	initiator_user_id bigint unsigned not null,
    target_user_id bigint unsigned not null,
    `status` enum('requested', 'approved', 'declined'),
    requested_at datetime default now(),
	confirmed_at datetime,
	
	index id_idx(id),
    
	foreign key (id) references users(id)
);

insert into follow_requests(initiator_user_id, target_user_id, status) values
	('1', '2', 'approved'),
	('1', '4', 'approved'),
	('3', '1', 'approved');

create or replace view info as select * from likes order by id;
select * from info;

create or replace view media_view (media_type_id , user_id)
as select body, id FROM media;
select * from media_view;
















