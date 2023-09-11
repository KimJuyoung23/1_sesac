-- 230907 SQL 실습
-- 실행 순서 : FROM → ON → JOIN → WHERE → GROUP BY → HAVING → SELECT → ORDER BY
-- 작성 순서 : SELECT → FROM → JOIN → ON → WHERE → GROUP BY → HAVING → ORDER BY

-- Select 실습
-- 1. genres 테이블의 Name Column에서 ‘ 음악’(문자열)을 추가하여 출력하기
SELECT Name || ' 음악' FROM genres g

-- 2. customers 테이블에서 Country 칼럼을 중복없이 출력해보세요
SELECT DISTINCT country from customers c 

-- 3. tracks 테이블에서 Milliseconds칼럼에 1000을 나누어 Seconds 칼럼명으로 출력해주세요
SELECT Milliseconds / 1000 AS Seconds from tracks t  

-- 함수 실습
-- 1(과제). artists 테이블에서 Name 칼럼을 대문자로 출력해주세요
SELECT UPPER(Name) from artists a ; 

-- 2(과제). tracks 테이블에서 곡 이름을 추출하여 길이를 출력해주세요
SELECT name, LENGTH(Name) as '이름의 길이' from tracks t ;

-- 3(과제). invoices 테이블에서 청구서의 총 금액을 반올림한 결과를 표시
SELECT billingCountry, ROUND(Total) as Total from invoices i ;

-- 4. tracks 테이블에서 곡의 길이(Milliseconds)를 반올림 한 다음 분 단위로 곡의 길이를 표
SELECT name, ROUND(Milliseconds/1000/60) as 분 from tracks t; -- Round() 함수 사용을 의

-- 5. invoices 테이블에서 청구서의 총 금액(Total)에 따라서 금액 범위를 분류
-- (Total 값이 10 이하면 '낮음', 10 초과 50 이하면 '보통', 50 초과면 '높음'으로 분류)
SELECT * from invoices i;
select BillingCountry ,
	CASE 
		when Total > 50 then '높음'
		when Total > 10 then '보통'
		ELSE '낮음'
	END as Total
from invoices i;


-- Where 실습
-- 1. customers 테이블에서 나라가 "USA"인 고객들의 정보를 선택
SELECT * FROM customers c WHERE Country is 'USA';

-- 2. employees 테이블에서 고용일이 2003년 이전인 직원들의 정보를 선택
SELECT * FROM employees e WHERE HireDate < '2003-01-01';

-- 3. albums 테이블에서 앨범 제목에 "Love"라는 단어가 포함된 앨범들의 정보를 선택
SELECT * FROM albums a WHERE Title LIKE '%Love%';

-- GROUP BY & HAVING 실습
-- 1(과제). customers 테이블에서 각 나라별로 고객 수가 5명 이상인 나라들의 정보를 선택
SELECT Country, COUNT(CustomerId) as customers FROM customers c group by Country HAVING COUNT(CustomerId) >= 5 ;

-- 2. tracks 테이블에서 곡 장르별로 곡 수가 100개 이상인 장르를 선택
SELECT GenreId, COUNT(TrackId) FROM tracks t group by GenreId HAVING COUNT(TrackId) >= 100; 

-- 3(과제). tracks 테이블에서 각 곡의 장르별로 평균 길이가 300000 밀리초(5분) 이상인 장르를 선택
SELECT GenreId , ROUND(AVG(Milliseconds)/60000) as 분 FROM tracks t Group by GenreId HAVING AVG(Milliseconds) >= 300000; 

-- 4. invoices 테이블에서 각 고객별로 총 구매 금액이 40달러 이상인 고객을 선택
SELECT CustomerId, SUM(Total)  FROM invoices i group by CustomerId HAVING SUM(Total) > 40; 

-- 5(과제). tracks 테이블에서 각 앨범의 트랙 수가 15개 이상인 앨범을 선택
SELECT AlbumId , COUNT(TrackId) FROM tracks t group by AlbumId HAVING COUNT(TrackId) >= 15; 

-- Groupby, having, order by 실습
-- 1. artists 테이블에서 아티스트 이름을 알파벳 순으로 정렬
SELECT Name FROM artists a order by Name;

-- 2. tracks 테이블에서 곡 길이를 오름차순으로 정렬하여 선택
SELECT * FROM tracks t order by Milliseconds;

-- 3. invoices 테이블에서 청구서의 총 금액을 내림차순으로 정렬하여 선택
SELECT * FROM invoices i2 order	by Total desc;
SELECT CustomerId , SUM(Total) FROM invoices i group by CustomerId order by SUM(Total) desc;


-- Join 실습
SELECT *
FROM invoices as i
JOIN customers as c ON i.CustomerId = c.CustomerId
	
SELECT i.InvoiceId , ii.Quantity 
FROM invoice_items ii 
LEFT JOIN invoices i ON ii.InvoiceId = i.InvoiceId
	
-- 1. customers와 invoices을 테이블을 조인하여 각 고객의 이름과 구매한 청구서의 총 금액을 선택
select * FROM customers c ;
SELECT * FROM invoices i ;
SELECT c.FirstName  ||' '|| c.LastName  as 이름 , sum(i.Total) as '청구서 총액'
FROM customers c 
join invoices i on c.CustomerId = i.CustomerId 
group by c.CustomerId 
ORDER BY 이름;


-- 2(과제). employees와 customers 테이블을 조인하여 각 직원과 그 직원이 담당한 고객 수를 선택
SELECT e.LastName || ' ' || e.FirstName as '직원 이름' , count(c.CustomerId) as '담당 고객 수'
FROM employees e
left join customers c on e.EmployeeId = c.SupportRepId 
GROUP BY e.EmployeeId 
ORDER BY e.LastName;

-- 3(과제). albums, tracks, 그리고 genres 테이블을 조인하여 각 앨범의 제목, 곡 수, 그리고 장르 이름을 선택
SELECT a.Title as '앨범 제목' , COUNT(t.TrackId) as '곡 수' , g.Name as 장르  
FROM tracks t 
join albums a on a.AlbumId = t.AlbumId 
join genres g on g.GenreId = t.GenreId 
GROUP BY t.AlbumId 
ORDER BY a.Title ;
