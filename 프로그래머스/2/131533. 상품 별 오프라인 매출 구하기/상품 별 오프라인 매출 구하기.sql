-- 코드를 입력하세요
SELECT p.product_code, p.price * sum(s.sales_amount) as name
from offline_sale s
join product p on p.product_id = s.product_id
group by s.product_id
order by -p.price * sum(s.sales_amount),p.product_code