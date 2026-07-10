GigHub API 
Author: Ivy Githinji

Admission Number: C027-01-0883/2024

Course: Back-End Development (CIT 3107)

Date: July 2026



Project Overview



GigHub is a freelance platform API that connects freelancers with clients in Nairobi. This API allows clients to post gigs (jobs) and freelancers to browse and apply for them.



Dataset Details (Based on Admission Number)



Number of Gigs: 8 (5 + last digit 3)

Categories: Marketing, Data, Consulting (xxxx 0883 is odd)

Currency: KES (first two digits 08 is less than 10)



Features



List all gigs with optional filtering

Filter by category (Marketing, Data, or Consulting)

Filter by minimum and maximum budget

View a single gig by ID

Search for gigs by title

Create a new gig with validation

Update a gig's budget or status

Delete a gig



Technology Stack



FastAPI - Web framework for building APIs

Uvicorn - ASGI server for running FastAPI

Python 3.12 - Programming language

Docker - Containerization for PostgreSQL



Setup Instructions



Prerequisites



Python 3.12+

Docker Desktop

UV package manager



Steps to Run



1\. Navigate to project folder

cd C:\\Users\\User\\cit-backend-course



2\. Activate virtual environment

.\\Githinji\\Scripts\\activate



3\. Install dependencies

uv add --active fastapi uvicorn sqlmodel psycopg2-binary alembic python-dotenv



4\. Start PostgreSQL (for Lab 4)

docker compose up -d



5\. Run the API

uv run uvicorn gighub:app --reload --port 9000



6\. Access Swagger UI

http://127.0.0.1:9000/docs



API Endpoints



GET / - Welcome message

GET /gigs - List all gigs with filters (category, min\_budget, max\_budget)

GET /gigs/{id} - Get a specific gig by ID

GET /gigs/search?q=query - Search gigs by title

POST /gigs - Create a new gig

PUT /gigs/{id} - Update a gig's budget or status

DELETE /gigs/{id} - Delete a gig



Sample Gig Data



{

&#x20; "id": 1,

&#x20; "title": "Social Media Manager for Fashion Brand",

&#x20; "description": "Manage Instagram, TikTok, and Twitter for a Nairobi-based fashion brand.",

&#x20; "category": "Marketing",

&#x20; "budget": 25000.0,

&#x20; "currency": "KES",

&#x20; "status": "Open",

&#x20; "client\_name": "Jane Muthoni"

}



My 8 Gigs



Marketing Gigs

1\. Social Media Manager for Fashion Brand - 25,000 KES - Open

2\. SEO Content Writer - 15,000 KES - Open

3\. Digital Marketing Campaign - 40,000 KES - In Progress



Data Gigs

4\. Data Entry Clerk - 10,000 KES - Open

5\. Data Analyst for Sales Report - 35,000 KES - Open

6\. Database Cleanup - 20,000 KES - Closed



Consulting Gigs

7\. Business Strategy Consultant - 50,000 KES - Open

8\. HR Process Consultant - 45,000 KES - In Progress



Lab 4: Database Integration



This repository also includes Lab 4 work demonstrating database integration with PostgreSQL.



Library API Endpoints (Lab 4)

POST /books - Create a new book

GET /books - List all books with pagination

GET /books/{id} - Get a specific book

PATCH /books/{id} - Update a book

GET /books/search - Search books by author or title



Running Lab 4

uv run uvicorn library\_main:app --reload --port 8001



Project Structure



cit-backend-course/

├── gighub.py

├── library\_main.py

├── requirements.txt

├── Dockerfile

├── docker-compose.yml

├── models/

│   └── book.py

├── database/

│   └── session.py

├── .env

├── README.md

└── Githinji/



Contact



GitHub: \[ivygithinji-student]





Acknowledgments



Course Instructor: CIT 3107 Back-End Development

FastAPI Documentation: https://fastapi.tiangolo.com

SQLModel Documentation: https://sqlmodel.tiangolo.com



Last Updated: July 2026

