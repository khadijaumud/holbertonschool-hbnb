DROP TABLE IF EXISTS place_amenity;
DROP TABLE IF EXISTS reviews;
DROP TABLE IF EXISTS places;
DROP TABLE IF EXISTS amenities;
DROP TABLE IF EXISTS users;


CREATE TABLE users (
    id VARCHAR(36) PRIMARY KEY,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(120) UNIQUE NOT NULL,
    password_hash VARCHAR(128) NOT NULL,
    is_admin BOOLEAN DEFAULT 0
);


CREATE TABLE amenities (
    id VARCHAR(36) PRIMARY KEY,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    name VARCHAR(50) UNIQUE NOT NULL
);


CREATE TABLE places (
    id VARCHAR(36) PRIMARY KEY,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    title VARCHAR(100) NOT NULL,
    description VARCHAR(500),
    price REAL NOT NULL,
    latitude REAL NOT NULL,
    longitude REAL NOT NULL,
    owner_id VARCHAR(36) NOT NULL,
    FOREIGN KEY (owner_id) REFERENCES users(id)
);

CREATE TABLE reviews (
    id VARCHAR(36) PRIMARY KEY,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    text VARCHAR(1000) NOT NULL,
    rating INTEGER NOT NULL,
    user_id VARCHAR(36) NOT NULL,
    place_id VARCHAR(36) NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users(id),
    FOREIGN KEY (place_id) REFERENCES places(id)
);

CREATE TABLE place_amenity (
    place_id VARCHAR(36),
    amenity_id VARCHAR(36),
    PRIMARY KEY (place_id, amenity_id),
    FOREIGN KEY (place_id) REFERENCES places(id),
    FOREIGN KEY (amenity_id) REFERENCES amenities(id)
);

INSERT INTO users (id, first_name, last_name, email, password_hash, is_admin) 
VALUES ('admin-uuid-1111-2222-333333333333', 'Admin', 'HBnB', 'admin@hbnb.com', '$2b$12$K89O.w6GgD7VbM1vX9dTe.6g8eE62hYmRk0gX2eH8yBqg8u7x9iJy', 1);

INSERT INTO amenities (id, name) VALUES ('amenity-1', 'WiFi');
INSERT INTO amenities (id, name) VALUES ('amenity-2', 'Air Conditioning');
INSERT INTO amenities (id, name) VALUES ('amenity-3', 'Swimming Pool');