CREATE DATABASE diagnosticoentidades;

CREATE TABLE execucoes (
    id_execucao SERIAL PRIMARY KEY,
    nome_entidade TEXT NOT NULL,
    data_execucao TIMESTAMP NOT NULL,
    tempo_execucao_seg INTEGER NOT NULL CHECK (tempo_execucao_seg BETWEEN 30 AND 5000),
    status_execucao TEXT NOT NULL CHECK (status_execucao IN ('Sucesso', 'Erro', 'Timeout', 'Cancelado')),
    servidor TEXT NOT NULL CHECK (servidor IN ('server1', 'server2', 'server3', 'server4')),
    categoria_entidade TEXT NOT NULL CHECK (categoria_entidade IN ('Carga', 'Transformação', 'Relatório', 'Exportação'))
);