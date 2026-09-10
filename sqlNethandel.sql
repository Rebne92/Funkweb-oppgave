-- Måtte ta en “DROP” comand for å rette på en tidligere feil jeg hadde gjort
DROP TABLE IF EXISTS produkter CASCADE;

-- Opprett tabellen som skulle inneholde alle produktene som skulle brukes i databasen 
CREATE TABLE produkter (
    id SERIAL PRIMARY KEY,
    navn VARCHAR(100) NOT NULL,
    pris NUMERIC(10, 2) NOT NULL,
    kategori VARCHAR(50) NOT NULL,
    farge VARCHAR(30) NOT NULL
);

– Sett inn alle produktvarianter variabler som navn, pris, kategori, farge
INSERT INTO produkter (navn, pris, kategori, farge) VALUES
('Taske', 300.00, 'Tasker', 'Blå'),
('Taske', 300.00, 'Tasker', 'Gul'),
('Taske', 300.00, 'Tasker', 'Rød'),
('Taske', 300.00, 'Tasker', 'Hvit'),
('Taske', 300.00, 'Tasker', 'Grå'),
('Bukser', 900.00, 'Bukser', 'Blå'),
('Bukser', 900.00, 'Bukser', 'Gul'),
('Bukser', 900.00, 'Bukser', 'Rød'),
('Bukser', 900.00, 'Bukser', 'Hvit'),
('Bukser', 900.00, 'Bukser', 'Grå'),
('Veske', 800.00, 'Vesker', 'Blå'),
('Veske', 800.00, 'Vesker', 'Gul'),
('Veske', 800.00, 'Vesker', 'Rød'),
('Veske', 800.00, 'Vesker', 'Hvit'),
('Veske', 800.00, 'Vesker', 'Grå');
