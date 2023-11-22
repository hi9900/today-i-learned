--
-- PostgreSQL database dump
--

-- Dumped from database version 15.3
-- Dumped by pg_dump version 15.3

-- Started on 2023-06-19 18:15:52

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'EUC_KR';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- TOC entry 6 (class 2615 OID 16399)
-- Name: PRJ1; Type: SCHEMA; Schema: -; Owner: postgres
--

CREATE SCHEMA "PRJ1";


ALTER SCHEMA "PRJ1" OWNER TO postgres;

--
-- TOC entry 3326 (class 0 OID 0)
-- Dependencies: 6
-- Name: SCHEMA "PRJ1"; Type: COMMENT; Schema: -; Owner: postgres
--

COMMENT ON SCHEMA "PRJ1" IS '자기주도학습 PRJ1';


--
-- TOC entry 216 (class 1259 OID 16409)
-- Name: SEQ_USER; Type: SEQUENCE; Schema: PRJ1; Owner: postgres
--

CREATE SEQUENCE "PRJ1"."SEQ_USER"
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE "PRJ1"."SEQ_USER" OWNER TO postgres;

--
-- TOC entry 3327 (class 0 OID 0)
-- Dependencies: 216
-- Name: SEQUENCE "SEQ_USER"; Type: COMMENT; Schema: PRJ1; Owner: postgres
--

COMMENT ON SEQUENCE "PRJ1"."SEQ_USER" IS 'TBL_USER를 위한 Sequence';


SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- TOC entry 215 (class 1259 OID 16403)
-- Name: TBL_USER; Type: TABLE; Schema: PRJ1; Owner: postgres
--

CREATE TABLE "PRJ1"."TBL_USER" (
    user_seq bigint NOT NULL,
    user_id character varying(20) NOT NULL,
    user_name character varying(30),
    user_pass character varying(256),
    user_level character(1) DEFAULT 1
);


ALTER TABLE "PRJ1"."TBL_USER" OWNER TO postgres;

--
-- TOC entry 3328 (class 0 OID 0)
-- Dependencies: 215
-- Name: TABLE "TBL_USER"; Type: COMMENT; Schema: PRJ1; Owner: postgres
--

COMMENT ON TABLE "PRJ1"."TBL_USER" IS '회원테이블';


--
-- TOC entry 3319 (class 0 OID 16403)
-- Dependencies: 215
-- Data for Name: TBL_USER; Type: TABLE DATA; Schema: PRJ1; Owner: postgres
--

COPY "PRJ1"."TBL_USER" (user_seq, user_id, user_name, user_pass, user_level) FROM stdin;
1	id1	사용자이름1	pass	1
\.


--
-- TOC entry 3329 (class 0 OID 0)
-- Dependencies: 216
-- Name: SEQ_USER; Type: SEQUENCE SET; Schema: PRJ1; Owner: postgres
--

SELECT pg_catalog.setval('"PRJ1"."SEQ_USER"', 1, true);


--
-- TOC entry 3176 (class 2606 OID 16408)
-- Name: TBL_USER TBL_USER_pkey; Type: CONSTRAINT; Schema: PRJ1; Owner: postgres
--

ALTER TABLE ONLY "PRJ1"."TBL_USER"
    ADD CONSTRAINT "TBL_USER_pkey" PRIMARY KEY (user_seq);


-- Completed on 2023-06-19 18:15:53

--
-- PostgreSQL database dump complete
--

