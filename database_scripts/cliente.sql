CREATE TABLE IF NOT EXISTS public.cliente
(
    id SERIAL PRIMARY KEY,
    nome character varying(100) NOT NULL,
    cpf character varying(14) NOT NULL UNIQUE,
    rg character varying(20) NOT NULL,
    data_nascimento date NOT NULL,
    cep character varying(10) NOT NULL,
    numero_residencia character varying(5) NOT NULL
);
