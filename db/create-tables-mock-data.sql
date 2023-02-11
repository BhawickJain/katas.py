DROP TABLE IF EXISTS orders;
DROP TABLE IF EXISTS product;

create table product
(
product_id serial primary key,
name varchar(128) not null,
rrp numeric not null,
available_from date not null
);
create table orders
(
order_id serial primary key,
product_id integer not null,
quantity integer not null,
order_price numeric not null,
dispatch_date date not null,
foreign key (product_id) references product(product_id)
);


INSERT INTO product(name, rrp, available_from)
VALUES
('Bayesian Methods for Nonlinear Classification and Regression', 94.95, date_trunc('week', CURRENT_DATE)::date - INTERVAL '4 DAY'),
('(next year) in Review (preorder)', 21.95, CURRENT_DATE + INTERVAL '1 YEAR'),
('Learn Python in Ten Minutes', 2.15, CURRENT_DATE - INTERVAL '3 MONTH'),
('sports almanac (1999-2049)', 3.38, CURRENT_DATE - INTERVAL '2 YEAR'),
('finance for dummies', 84.99, CURRENT_DATE - INTERVAL '1 YEAR');

INSERT INTO orders(product_id, quantity, order_price, dispatch_date)
VALUES
(1, 1, 90.00, CURRENT_DATE - INTERVAL '2 MONTH'),
(3, 1, 1.15, CURRENT_DATE - INTERVAL '6 MONTH'),
(1, 10, 90.00, CURRENT_DATE - INTERVAL '11 MONTH'),
(4, 11, 3.38, CURRENT_DATE - INTERVAL '6 MONTH'),
(5, 11, 501.33, CURRENT_DATE - INTERVAL '2 YEAR');











