CREATE TABLE IF NOT EXISTS public.endereco
(
    id SERIAL PRIMARY KEY,
    cep character varying(10) NOT NULL,
    logradouro character varying(100) NOT NULL,
    complemento character varying(100),
    bairro character varying(100)NOT NULL,
    cidade character varying(100) NOT NULL,
    estado character(2) NOT NULL,
    numero_residencia character varying(5) NOT NULL
    cliente_id integer NOT NULL REFERENCES public.cliente (id) ON DELETE CASCADE
);
