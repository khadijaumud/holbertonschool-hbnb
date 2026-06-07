# HBnB Project - Part 3: Enhanced Backend with Authentication and Database Integration

Welcome to Part 3 of the HBnB Project. In this phase, the backend application is transitioned from an in-memory repository to a persistent relational database using SQLAlchemy and SQLite. Additionally, secure user sessions, JWT-based authentication, and role-based access control (RBAC) are introduced.

## Objectives
* Authentication & Authorization: Implement secure JWT-based user login and protect endpoints based on user roles (is_admin).
* Database Integration: Replace temporary in-memory storage with an SQLite database using SQLAlchemy ORM for development.
* Data Consistency: Define database schemas, models, and constraints to ensure data integrity.
* Data Relationships: Map one-to-many and many-to-many relationships between Users, Places, Reviews, and Amenities.

---

## Database Schema (ER Diagram)

The database structure and relationships are modeled as follows:

```mermaid
erDiagram
    USERS {
        string id PK
        datetime created_at
        datetime updated_at
        string first_name
        string last_name
        string email UK
        string password_hash
        boolean is_admin
    }
    PLACES {
        string id PK
        datetime created_at
        datetime updated_at
        string title
        string description
        float price
        float latitude
        float longitude
        string owner_id FK
    }
    REVIEWS {
        string id PK
        datetime created_at
        datetime updated_at
        string text
        int rating
        string user_id FK
        string place_id FK
    }
    AMENITIES {
        string id PK
        datetime created_at
        datetime updated_at
        string name UK
    }
    PLACE_AMENITY {
        string place_id FK
        string amenity_id FK
    }

    USERS ||--o{ PLACES : "owns"
    USERS ||--o{ REVIEWS : "writes"
    PLACES ||--o{ REVIEWS : "has"
    PLACES ||--o{ PLACE_AMENITY : "contains"
    AMENITIES ||--o{ PLACE_AMENITY : "assigned_to"
```

---

## Setup & Installation

### 1. Initialize the SQLite Database
To generate the tables and populate the database with initial seed data (including an administrator account and basic amenities), run the following command in your terminal:

sqlite3 development.db < init_db.sql

### 2. Run the Application
Start the Flask development server:

python run.py
