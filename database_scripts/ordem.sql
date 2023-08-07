CREATE TABLE IF NOT EXISTS public.ordem
(
    id SERIAL NOT NULL PRIMARY KEY,
    nome character varying(100) NOT NULL,
    ticker character varying(10) NOT NULL,
    valor_compra numeric(10, 2) NOT NULL,
	quantidade_compra numeric(5) NOT NULL,
    data_compra DATE NOT NULL,
    cliente_id integer NOT NULL REFERENCES public.cliente (id) ON DELETE CASCADE
);
