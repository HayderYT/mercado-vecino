CREATE TABLE IF NOT EXISTS tiendas (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    barrio VARCHAR(100) NOT NULL
);

INSERT INTO tiendas (nombre, barrio) VALUES
('Tienda Don Pedro', 'Suba'),
('Minitienda Doña Maria', 'Teusaquillo');
