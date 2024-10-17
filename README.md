---- It will be updated soon

- ## to connect with KSQL --> 

 docker exec -it primary-ksqldb-server ksql http://localhost:8088 .

- to create Stream for random_numbers 
        CREATE STREAM random_numbers_stream (number INT, timestamp STRING) 
     WITH (KAFKA_TOPIC='random_numbers', VALUE_FORMAT='JSON', TIMESTAMP='timestamp', TIMESTAMP_FORMAT='yyyy-MM-dd HH:mm:ss');
 




- to create stream for  greater_than_nine
    CREATE STREAM greater_than_nine_stream AS 
    SELECT number, timestamp 
    FROM random_numbers_stream 
    WHERE number > 9;

- to see data
    SELECT * FROM random_numbers_stream EMIT CHANGES;
    SELECT * FROM greater_than_nine_stream  EMIT CHANGES;

- to work with NIFI --- USE CONSUMERKAFKA ,EVALUATEJSON AND PUTEMAIL PROCESSOR ON WEB 


