drop database if exists blogger;
drop database if exists blog_db;
create database blogger;

\c blogger

SET statement_timeout = 0;
SET lock_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SET check_function_bodies = false;
SET client_min_messages = warning;
SET default_tablespace = '';
SET default_with_oids = false;

-- combined user account and person since it's 1 to 1 relationship
-- no additional attributes for author and persons, so both are the same as person

create table person (
    id serial primary key,
    username varchar(30) unique not NULL,
    password varchar(128) NOT NULL,
    first_name varchar(50) NOT NULL,
    last_name varchar(50) NOT NULL
);

create table blog (
    id serial primary key,
    title text not null,
    summary text not null,
    last_action varchar(20),
    last_updated timestamp,
    person_id INT,
    constraint fk_blog_author
    foreign key (person_id)
    REFERENCES person(id)
);

create table blog_follow (
    blog_id INT not null,
    person_id INT not null,
    primary key(blog_id, person_id),
    constraint fk_blog_follow_blog
    foreign key (blog_id)
    REFERENCES blog(id),
    constraint fk_blog_follow_person
    foreign key (person_id)
    REFERENCES person(id)
);

create table post (
    id serial primary key,
    title text not null,
    content text not null,
    last_action varchar(20),
    last_updated timestamp,
    -- view_count INT default 0,
    blog_id INT,
    constraint fk_post_blog
    foreign key (blog_id)
    REFERENCES blog(id)
);


create table comment (
    id serial primary key,
    content text not null,
    last_action varchar(20),
    last_updated timestamp,
    post_id INT,
    person_id INT,
    constraint fk_comment_post
    foreign key (post_id)
    REFERENCES post(id),
    constraint fk_comment_person
    foreign key (person_id)
    REFERENCES person(id)
);