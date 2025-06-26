import sqlite3

with sqlite3.connect('bdd.db') as connexion:
    cursor = connexion.cursor()
    requete = """
    CREATE TABLE categories(
    categories_naf VARCHAR(50),
    categories_categorie VARCHAR(50),
    PRIMARY KEY(categories_naf)
    );

    CREATE TABLE societe(
    societe_siren INTEGER,
    societe_nom VARCHAR(50),
    categories_naf VARCHAR(50),
    PRIMARY KEY(societe_siren),
    FOREIGN KEY(categories_naf) REFERENCES categories(categories_naf)
    );

    CREATE TABLE etablissement(
    etablissement_siret INTEGER,
    etablissement_nom VARCHAR(50),
    societe_siren INTEGER,
    categories_naf VARCHAR(50),
    adresse_numero INTEGER,
    adresse_rue VARCHAR(50),
    PRIMARY KEY(etablissement_siret),
    FOREIGN KEY(societe_siren) REFERENCES societe(societe_siren),
    FOREIGN KEY(categories_naf) REFERENCES categories(categories_naf)
    FOREIGN KEY(adresse_numero, adresse_rue) REFERENCES adresse(adresse_numero, adresse_rue)
    );

    CREATE TABLE adresse(
    adresse_numero INTEGER,
    adresse_rue VARCHAR(50),
    coordonnees_latitude DECIMAL(15,6),
    coordonnees_longitude DECIMAL(15,6),
    commune_code INTEGER,
    PRIMARY KEY(adresse_numero, adresse_rue),
    FOREIGN KEY(coordonnees_latitude, coordonnees_longitude) REFERENCES coordonnees(coordonnees_latitude, coordonnees_longitude),
    FOREIGN KEY(commune_code) REFERENCES commune(commune_code)
    );

    CREATE TABLE coordonnees(
    coordonnees_latitude DECIMAL(15,6),
    coordonnees_longitude DECIMAL(15,6),
    PRIMARY KEY(coordonnees_latitude, coordonnees_longitude)
    );

    CREATE TABLE commune(
    commune_code INTEGER,
    commune_nom VARCHAR(50),
    commune_codepostal INTEGER ,
    PRIMARY KEY(commune_code)
    );"""
    
    cursor.executescript(requete)
    connexion.commit()