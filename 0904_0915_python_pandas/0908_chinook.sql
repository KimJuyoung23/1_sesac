-- 230908 SQL 실습
-- 실행 순서 : FROM → ON → JOIN → WHERE → GROUP BY → HAVING → SELECT → ORDER BY
-- 작성 순서 : SELECT → FROM → JOIN → ON → WHERE → GROUP BY → HAVING → ORDER BY

-- 1(과제). invoices 테이블에서 가장 높은 총 금액을 가진 청구서의 정보를 선택
SELECT * 
FROM invoices i3 
WHERE Total = (
	SELECT MAX(Total) 
	from invoices i4);


-- 2. tracks 테이블에서 곡 길이가 평균 길이보다 긴 곡들의 정보를 선택
SELECT * 
FROM tracks t 
WHERE Milliseconds > (
	SELECT AVG(Milliseconds) 
	from tracks t2) ;


-- 3(과제). genres 테이블에서 곡 수가 가장 많은 장르의 정보를 선택
SELECT * 
FROM genres g 
WHERE GenreId = (
	SELECT GenreId 
	from tracks t 
	group by GenreId 
	HAVING COUNT(*) 
	ORDER BY COUNT(*) DESC 
	LIMIT 1);


-- 4. albums 테이블과 tracks 테이블을 사용하여 각 앨범의 제목과 해당 앨범의 곡 수를 함께 선택
SELECT a.Title , 
	(SELECT COUNT(*)  
	from tracks t 
	WHERE a.AlbumId = t.AlbumId 
	group by t.AlbumId  )
FROM albums a ;


-- 5(과제). artists 테이블에서 각 아티스트의 이름과 해당 아티스트가 발매한 첫 번째 앨범의 제목을 함께 선택
SELECT a2.Title , (
	SELECT a3.Name  
	from artists a3 
	WHERE a3.ArtistId = a2.ArtistId 
	LIMIT 1) 
FROM albums a2 ;
