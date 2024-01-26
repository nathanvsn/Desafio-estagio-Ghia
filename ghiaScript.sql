use ghia; 
select * from Altas9_20240126165008; 
select * from auxiliar_destaque9_20240126165008;

SELECT AVG(Osciação) as media_oscilacao FROM Altas9_20240126165008;
SELECT AVG(Osciação) as media_oscilacao FROM baixas9_20240126165008;

SELECT *, (máximo - mínimo) as variacao_preco 
FROM auxiliar_destaque9_20240126165008 
ORDER BY variacao_preco ASC 
LIMIT 5;
