CREATE TABLE tbl_event (
  event_seq INT NOT NULL AUTO_INCREMENT,
  event_data INT NULL,
  regdate DATETIME NULL,
  PRIMARY KEY (`event_seq`))
COMMENT = 'Event Scheduler 테스트';


CREATE EVENT 
    IF NOT EXISTS evt_insert_event
ON SCHEDULE
    EVERY 1 MINUTE
COMMENT 'tbl_event에 1분마다 Insert'
DO
	INSERT INTO tbl_event(event_data, regdate) 
    VALUES (1, now());
    
    
CREATE EVENT 
    IF NOT EXISTS evt_delete_event
ON SCHEDULE
    AT CURRENT_TIMESTAMP + INTERVAL 5 MINUTE
COMMENT '5분 후 tbl_event Data 삭제'
DO
	DELETE FROM tbl_event;
    

CREATE EVENT 
    IF NOT EXISTS evt_update_event
ON SCHEDULE
    EVERY 30 SECOND
    STARTS CURRENT_TIMESTAMP
	ENDS CURRENT_TIMESTAMP + INTERVAL 10 MINUTE
COMMENT '10분간 30초마다 event_data update'
DO
	UPDATE tbl_event SET event_data = event_data + 1;
    
SELECT * FROM information_schema.EVENTS;