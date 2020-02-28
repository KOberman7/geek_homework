-- �������� ���� ������������� ������� ����� ������ � ���� ������ shop. ������� ������������ shop_read ������ ���� �������� ������
-- ������� �� ������ ������, ������� ������������ shop � ����� �������� � �������� ���� ������ shop.


DROP USER IF EXISTS 'shop_reader'@'localhost';
CREATE USER 'shop_reader'@'localhost' IDENTIFIED WITH sha256_password BY '123';
GRANT SELECT ON shop_online.* TO 'shop_reader'@'localhost';

-- test
INSERT INTO catalogs(name)
 -- denied for this user
VALUES('New catalog');
 -- success
SELECT * FROM catalogs;

DROP USER IF EXISTS 'shop'@'localhost';
CREATE USER 'shop'@'localhost' IDENTIFIED WITH sha256_password BY '123';
GRANT ALL ON shop_online.* TO 'shop'@'localhost';
GRANT GRANT OPTION ON shop_online.* TO 'shop'@'localhost';

-- test
INSERT INTO catalogs(name)
 -- success
VALUES('New catalog');
 -- have new catalog
SELECT * FROM catalogs;