GigHub API & Library API - CIT 3107 Back-End Development

Author: Ivy Githinji
Admission Number: C027-01-0883/2024
Course: Back-End Development (CIT 3107)
Date: July 2026


A NOTE ABOUT THIS PROJECT

This repository contains all my work for CIT 3107 Back-End Development. The journey has been a great learning experience, with both successes and challenges along the way.

One of the biggest challenges was getting PostgreSQL to work with my Windows machine. Despite spending hours troubleshooting network issues, authentication problems, and Docker configurations, I kept running into the same error: "password authentication failed for user postgres".

The psql command worked perfectly inside the Docker container, which confirmed PostgreSQL was running correctly. But Python's psycopg2 driver simply refused to connect, even after trying different versions, authentication methods, and connection settings.

After extensive troubleshooting, I made the practical decision to use SQLite for Lab 4. This allowed me to complete the work and demonstrate all the required concepts: CRUD operations, database models, validation, search, and update endpoints.

Why SQLite was the right choice for this situation:
- It works immediately without complex network setup
- It uses a file-based database (library.db) that's simple to manage
- It still demonstrates all the database concepts required by the lab
- It allowed me to focus on building the API rather than fighting with infrastructure

While this was a challenge at the time, I now better understand the importance of database configuration and the kinds of real-world issues that can arise when connecting applications to databases. I'm also more confident in using Docker and troubleshooting connection issues in the future.


LAB 1: Environment Setup


What was done:
- Installed Python 3.12+
- Installed Git
- Installed UV package manager
- Created virtual environment (Githinji)
- Installed FastAPI and Uvicorn
- Created first FastAPI application
- Ran server on port 8000 and 9000

Skills Learned:
- Virtual environments
- Package management with UV
- Running a FastAPI server
- Port switching


LAB 2: Dockerizing FastAPI Application
____________________________________

What was done:
- Created a Dockerfile for the FastAPI application
- Built a Docker image (backend-app:latest)
- Ran the application inside a Docker container
- Used docker-compose for multi-container setup
- Shared the application via Docker image

Skills Learned:
- Dockerfile creation
- Docker image building
- Container management
- Docker Compose


PROJECT 1: GIGHUB API - Freelance Platform


Project Overview

GigHub is a freelance platform API that connects freelancers with clients in Nairobi. This API allows clients to post gigs (jobs) and freelancers to browse and apply for them.

My goal was to build a practical API that could be used as the backend for a real freelance marketplace.

Dataset Details (Based on Admission Number)

My admission number (C027-01-0883/2024) determined my dataset:
- Number of Gigs: 8 (5 + last digit 3)
- Categories: Marketing, Data, Consulting (xxxx 0883 is odd)
- Currency: KES (first two digits 08 is less than 10)

GigHub Features

- List all gigs with optional filtering
- Filter by category (Marketing, Data, or Consulting)
- Filter by minimum and maximum budget
- View a single gig by ID
- Search for gigs by title
- Create a new gig with validation
- Update a gig's budget or status
- Delete a gig

GigHub API Endpoints

GET / - Welcome message
GET /gigs - List all gigs with filters (category, min_budget, max_budget)
GET /gigs/{id} - Get a specific gig by ID
GET /gigs/search?q=query - Search gigs by title
POST /gigs - Create a new gig
PUT /gigs/{id} - Update a gig's budget or status
DELETE /gigs/{id} - Delete a gig

My 8 Gigs

Marketing Gigs
1. Social Media Manager for Fashion Brand - 25,000 KES - Open
2. SEO Content Writer - 15,000 KES - Open
3. Digital Marketing Campaign - 40,000 KES - In Progress

Data Gigs
4. Data Entry Clerk - 10,000 KES - Open
5. Data Analyst for Sales Report - 35,000 KES - Open
6. Database Cleanup - 20,000 KES - Closed

Consulting Gigs
7. Business Strategy Consultant - 50,000 KES - Open
8. HR Process Consultant - 45,000 KES - In Progress


LAB 4: LIBRARY API - Database Integration


Project Overview

A Library Management API built with FastAPI. This API demonstrates CRUD (Create, Read, Update, Delete) operations and database integration.

The Challenge

The lab required using PostgreSQL, but I encountered persistent connection issues on my Windows machine. PostgreSQL was running correctly (psql worked perfectly inside the Docker container), but Python's psycopg2 driver would not authenticate.

What I Tried:
- Changing from localhost to 127.0.0.1
- Adding sslmode=disable to the connection string
- Switching from postgres:16 to postgres:15
- Using POSTGRES_HOST_AUTH_METHOD: trust
- Trying host.docker.internal
- Wiping all Docker volumes and starting fresh
- Hardcoding the database URL directly in the code

Despite all these attempts, the error persisted: "FATAL: password authentication failed for user postgres"

The Decision

After extensive troubleshooting, I chose to use SQLite for this lab. This was a practical decision that allowed me to:
1. Complete the work and demonstrate all required concepts
2. Focus on building the API functionality
3. Avoid spending more time on infrastructure issues

The Solution

Using SQLite meant:
- No network configuration needed
- A simple file-based database (library.db)
- The same CRUD operations and endpoints
- All validation and error handling intact
- The same Swagger UI experience

Library API Features

- Create new books
- List all books with pagination
- Get a specific book by ID
- Update book details
- Delete books
- Search books by title or author

Library API Endpoints

POST /books - Create a new book
GET /books - List all books with pagination
GET /books/{id} - Get a specific book
PATCH /books/{id} - Update a book
DELETE /books/{id} - Delete a book
GET /books/search - Search books by author or title

Exercises Completed:
- Exercise 2: Search Endpoint (/books/search)
- Exercise 3: Update Endpoint (PATCH /books/{id})


TECHNOLOGY STACK


FastAPI - Web framework for building APIs
Uvicorn - ASGI server for running FastAPI
SQLModel - ORM + Pydantic for database operations
SQLite - Database for Library API (practical choice)
PostgreSQL - Database for GigHub API (via Docker)
Docker - Containerization
Python 3.12 - Programming language
UV - Package manager


PROJECT STRUCTURE


cit-backend-course/
├── gighub.py                 # GigHub API (Main Project)
├── library_main.py           # Library API (Lab 4)
├── requirements.txt          # Python dependencies
├── Dockerfile                # Docker configuration (Lab 2)
├── docker-compose.yml        # Docker Compose for PostgreSQL
├── library.db                # SQLite database (Lab 4)
├── models/
│   └── book.py               # Book model (Lab 4)
├── database/
│   └── session.py            # Database connection (Lab 4)
├── .env                      # Environment variables
├── README.md                 # This file
└── Githinji/                 # Virtual environment


SETUP INSTRUCTIONS


Prerequisites

- Python 3.12+
- Docker Desktop (for GigHub API)
- UV package manager

Steps to Run All Projects

1. Navigate to project folder:
   cd C:\Users\User\cit-backend-course

2. Activate virtual environment:
   .\Githinji\Scripts\activate

3. Install dependencies:
   uv add --active fastapi uvicorn sqlmodel psycopg2-binary alembic python-dotenv

4. Start PostgreSQL (for GigHub API):
   docker compose up -d

5. Run GigHub API:
   uv run uvicorn gighub:app --reload --port 9000

6. Run Library API (Lab 4):
   python -m uvicorn library_main:app --reload --port 8001


ACCESS SWAGGER UI


GigHub API: http://127.0.0.1:9000/docs
Library API: http://127.0.0.1:8001/docs


LESSONS LEARNED
_______________

This project taught me several important lessons:

1. Infrastructure matters - Setting up databases and networking can be just as challenging as writing the code itself.

2. Troubleshooting is a skill - The process of trying different solutions and systematically eliminating possibilities was valuable, even when I didn't ultimately solve the PostgreSQL issue.

3. Practical decisions are sometimes necessary - Using SQLite was a practical choice that let me complete the work rather than getting stuck on a single issue.

4. The concepts transfer - Even though I used SQLite for the lab, the same CRUD operations, validation, and API design patterns apply to any database.

5. Docker is powerful but complex - Containerization is incredibly useful but requires careful configuration.


CONTACT


GitHub: ivygithinji-student
Email: ivy.githinji24@students.dkut.ac.ke


ACKNOWLEDGMENTS


Course Instructor: John Wandeto
CIT 3107 - Back-End Development
FastAPI Documentation: https://fastapi.tiangolo.com
SQLModel Documentation: https://sqlmodel.tiangolo.com

Last Updated: July 2026
