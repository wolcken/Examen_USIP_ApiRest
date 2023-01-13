--
-- PostgreSQL database dump
--

-- Dumped from database version 15.1
-- Dumped by pg_dump version 15.1

-- Started on 2023-01-12 20:17:27

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- TOC entry 214 (class 1259 OID 32769)
-- Name: users; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.users (
    id numeric NOT NULL,
    nombre character(50),
    apellido character(50),
    edad numeric(3,0)
);


ALTER TABLE public.users OWNER TO postgres;

--
-- TOC entry 3316 (class 0 OID 32769)
-- Dependencies: 214
-- Data for Name: users; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.users (id, nombre, apellido, edad) FROM stdin;
1	Alfredo                                           	Ramos                                             	30
2	Wilder                                            	Rosas                                             	27
3	Gladys                                            	Canaza                                            	30
4	Beatriz                                           	Chura                                             	29
5	Lucho                                             	Velasquez                                         	30
\.


--
-- TOC entry 3173 (class 2606 OID 32775)
-- Name: users Usuarios_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT "Usuarios_pkey" PRIMARY KEY (id);


-- Completed on 2023-01-12 20:17:27

--
-- PostgreSQL database dump complete
--

