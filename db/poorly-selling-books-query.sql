with product_id_sold_past_year as (
   SELECT o.product_id, sum(o.quantity) as total_sold
   FROM orders as o
   WHERE dispatch_date > CURRENT_DATE - INTERVAL '1 year'
   GROUP BY product_id
 ), less_than_10_sold_past_year as (
   SELECT *
   FROM product_id_sold_past_year
   WHERE total_sold < 10
 ), book_titles_available_for_more_than_3_months as (
   SELECT p.product_id, p.name, p.available_from
   FROM product as p
   WHERE available_from < CURRENT_DATE - INTERVAl '3 months'
 )
 , book_titles_less_than_10_sold_past_year as (
   SELECT p.product_id, p.name, p.available_from, l.total_sold
   FROM less_than_10_sold_past_year as l 
     JOIN book_titles_available_for_more_than_3_months as p
     ON p.product_id = l.product_id
 )
 SELECT *
 FROM book_titles_less_than_10_sold_past_year;

