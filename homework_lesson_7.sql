drop database if exists geekbrains;
create database geekbrains;
use geekbrains;

drop table if exists users;
create table users (
  id serial primary key,
  name varchar(255),
  birthday_at date,
  created_at datetime default current_timestamp,
  updated_at datetime default current_timestamp on update current_timestamp
);

drop table if exists orders;
create table orders (
  id serial primary key,
  user_id int unsigned,
  created_at datetime default current_timestamp,
  updated_at datetime default current_timestamp on update current_timestamp,
  key index_of_user_id(user_id)
);

drop table if exists catalogs;
create table catalogs (
  id serial primary key,
  name varchar(255),
  unique unique_name(name(10))
);

drop table if exists products;
create table products (
  id serial primary key,
  name varchar(255),
  desription text,
  price decimal (11,2),
  catalog_id int unsigned,
  created_at datetime default current_timestamp,
  updated_at datetime default current_timestamp on update current_timestamp,
  key index_of_catalog_id (catalog_id)
);

/*
 *Составьте список пользователей users, которые осуществили хотя бы один заказ orders в интернет магазине. 
 */

select 
	name 
from 
	users
where
	exists(select 1 from orders where user_id = users.id);

/*
 * Выведите список товаров products и разделов catalogs, который соответствует товару.
 */

select
	products.name as product_name,
	catalogs.name as catalog_name
from
	products
inner join catalogs on catalogs.id = products.catalog_id








