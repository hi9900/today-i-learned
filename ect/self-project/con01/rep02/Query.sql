SELECT * FROM "PRJ1"."TBL_USER";

SELECT LAST_VALUE FROM "PRJ1"."SEQ_USER";

INSERT INTO "PRJ1"."TBL_USER"(user_seq, user_id, user_name, user_pass, user_level)
VALUES (NEXTVAL('"PRJ1"."SEQ_USER"'),'id1','사용자이름1', 'pass', '1');
