CREATE TABLE ventes (
    id SERIAL PRIMARY KEY,
    produit VARCHAR(50),
    montant NUMERIC
);
INSERT INTO ventes (produit, montant) VALUES
    ('Abonnement A', 120.00),
    ('Abonnement B', 89.90);