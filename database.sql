CREATE DATABASE CRYPTO;
USE CRYPTO;
CREATE TABLE blockchain(
    number varchar(16),
    hash varchar(64),
    previous varchar(64),
    data varchar(128),
    nonce varchar(16)
);
