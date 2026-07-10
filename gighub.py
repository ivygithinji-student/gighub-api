from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel, Field
from typing import Optional, List

# Create the FastAPI app
app = FastAPI(
    title="GigHub API - Nairobi Freelance Platform",
    description="An API for managing freelance gigs in Nairobi",
    version="1.0.0"
)

# Admission Number: C027-01-0883/2024
# Number of gigs: 8 (5 + last digit 3)
# Categories: Marketing, Data, Consulting (odd xxxx)
# Currency: KES (first two digits 08 < 10)

# ============================================
# GIGS DATABASE (8 gigs based on admission number)
# ============================================

gigs_db = [
    # Marketing Gigs
    {
        "id": 1,
        "title": "Social Media Manager for Fashion Brand",
        "description": "Manage Instagram, TikTok, and Twitter for a Nairobi-based fashion brand. Create 10 posts per week and engage with followers.",
        "category": "Marketing",
        "budget": 25000.0,
        "currency": "KES",
        "status": "Open",
        "client_name": "Jane Muthoni"
    },
    {
        "id": 2,
        "title": "SEO Content Writer",
        "description": "Write 5 SEO-optimized blog posts for a tech startup's website. Must include keywords and meta descriptions.",
        "category": "Marketing",
        "budget": 15000.0,
        "currency": "KES",
        "status": "Open",
        "client_name": "David Kiprop"
    },
    {
        "id": 3,
        "title": "Digital Marketing Campaign",
        "description": "Plan and execute a 30-day Facebook/Instagram ad campaign for a new restaurant in Westlands. Target local audience.",
        "category": "Marketing",
        "budget": 40000.0,
        "currency": "KES",
        "status": "In Progress",
        "client_name": "Sarah Wanjiru"
    },
    # Data Gigs
    {
        "id": 4,
        "title": "Data Entry Clerk",
        "description": "Enter customer data from physical forms into an Excel spreadsheet. 500 entries to be completed within 1 week.",
        "category": "Data",
        "budget": 10000.0,
        "currency": "KES",
        "status": "Open",
        "client_name": "Michael Ochieng"
    },
    {
        "id": 5,
        "title": "Data Analyst for Sales Report",
        "description": "Analyze 3 months of sales data and create a PowerPoint presentation with insights and recommendations for management.",
        "category": "Data",
        "budget": 35000.0,
        "currency": "KES",
        "status": "Open",
        "client_name": "Alice Kemunto"
    },
    {
        "id": 6,
        "title": "Database Cleanup",
        "description": "Clean duplicate and incomplete records in a MySQL database. Ensure data integrity and consistency.",
        "category": "Data",
        "budget": 20000.0,
        "currency": "KES",
        "status": "Closed",
        "client_name": "Peter Njenga"
    },
    # Consulting Gigs
    {
        "id": 7,
        "title": "Business Strategy Consultant",
        "description": "Help a small retail business create a 1-year growth strategy and operational plan to expand to 3 new locations.",
        "category": "Consulting",
        "budget": 50000.0,
        "currency": "KES",
        "status": "Open",
        "client_name": "Grace Akinyi"
    },
    {
        "id": 8,
        "title": "HR Process Consultant",
        "description": "Review and redesign HR onboarding process for a mid-sized company in Nairobi. Create new employee handbook.",
        "category": "Consulting",
        "budget": 45000.0,
        "currency": "KES",
        "status": "In Progress",
        "client_name": "Robert Kariuki"
    }
]



# ============================================
# PYDANTIC MODELS (Validation)
# ============================================

# Valid categories (based on your admission number)
VALID_CATEGORIES = ["Marketing", "Data", "Consulting"]
VALID_STATUSES = ["Open", "In Progress", "Closed"]

# Model for creating a new gig
class GigCreate(BaseModel):
    title: str = Field(min_length=5, max_length=100)
    description: str = Field(min_length=20, max_length=500)
    category: str
    budget: float = Field(gt=0)
    client_name: str = Field(min_length=2, max_length=50)

# Model for updating a gig
class GigUpdate(BaseModel):
    budget: Optional[float] = Field(None, gt=0)
    status: Optional[str] = None



# ============================================
# ENDPOINTS (API Endpoints)
# ============================================

# 1. GET /gigs - Get all gigs with optional filtering
@app.get("/gigs")
def get_gigs(
    category: Optional[str] = None,
    min_budget: Optional[float] = None,
    max_budget: Optional[float] = None
):
    """Get all gigs with optional filtering by category and min/max budget."""
    results = gigs_db
    
    # Filter by category
    if category:
        results = [g for g in results if g["category"].lower() == category.lower()]
    
    # Filter by min budget
    if min_budget is not None:
        results = [g for g in results if g["budget"] >= min_budget]
    
    # Filter by max budget
    if max_budget is not None:
        results = [g for g in results if g["budget"] <= max_budget]
    
    return results




# 2. GET /gigs/{gig_id} - Get a single gig by ID
@app.get("/gigs/{gig_id}")
def get_gig(gig_id: int):
    """Get a single gig by its ID."""
    for gig in gigs_db:
        if gig["id"] == gig_id:
            return gig
    raise HTTPException(status_code=404, detail="Gig not found")




# 3. GET /gigs/search - Search gigs by title
@app.get("/gigs/search")
def search_gigs(q: str):
    """Search for gigs by title (query param q)."""
    results = []
    for gig in gigs_db:
        if q.lower() in gig["title"].lower():
            results.append(gig)
    return results



# 4. POST /gigs - Create a new gig
@app.post("/gigs")
def create_gig(gig: GigCreate):
    """Create a new gig with validation."""
    # Check if a gig with same title and client exists (prevent duplicates)
    for existing_gig in gigs_db:
        if existing_gig["title"].lower() == gig.title.lower() and existing_gig["client_name"].lower() == gig.client_name.lower():
            raise HTTPException(status_code=400, detail="Gig already exists")
    
    # Generate new ID
    new_id = max([g["id"] for g in gigs_db]) + 1
    
    # Validate category
    if gig.category not in VALID_CATEGORIES:
        raise HTTPException(status_code=400, detail=f"Category must be one of: {', '.join(VALID_CATEGORIES)}")
    
    # Create new gig
    new_gig = {
        "id": new_id,
        "title": gig.title,
        "description": gig.description,
        "category": gig.category,
        "budget": gig.budget,
        "currency": "KES",
        "status": "Open",  # New gigs start as "Open"
        "client_name": gig.client_name
    }
    
    gigs_db.append(new_gig)
    return {"message": "Gig created successfully", "gig": new_gig}




# 5. PUT /gigs/{gig_id} - Update a gig's budget or status
@app.put("/gigs/{gig_id}")
def update_gig(gig_id: int, gig_update: GigUpdate):
    """Update a gig's budget or status."""
    for index, gig in enumerate(gigs_db):
        if gig["id"] == gig_id:
            # Update budget if provided
            if gig_update.budget is not None:
                gigs_db[index]["budget"] = gig_update.budget
            
            # Update status if provided
            if gig_update.status is not None:
                # Validate status
                if gig_update.status not in VALID_STATUSES:
                    raise HTTPException(status_code=400, detail=f"Status must be one of: {', '.join(VALID_STATUSES)}")
                gigs_db[index]["status"] = gig_update.status
            
            return {"message": "Gig updated successfully", "gig": gigs_db[index]}
    
    raise HTTPException(status_code=404, detail="Gig not found")




# 6. DELETE /gigs/{gig_id} - Delete a gig
@app.delete("/gigs/{gig_id}")
def delete_gig(gig_id: int):
    """Delete a gig."""
    for index, gig in enumerate(gigs_db):
        if gig["id"] == gig_id:
            deleted_gig = gigs_db.pop(index)
            return {"message": "Gig deleted successfully", "gig": deleted_gig}
    
    raise HTTPException(status_code=404, detail="Gig not found")




# ============================================
# ROOT ENDPOINT (For testing)
# ============================================

@app.get("/")
def root():
    return {
        "message": "Welcome to GigHub API - Nairobi Freelance Platform",
        "admission": "C027-01-0883/2024",
        "endpoints": [
            "GET /gigs - Get all gigs (with filtering)",
            "GET /gigs/{id} - Get a single gig",
            "GET /gigs/search?q=title - Search gigs",
            "POST /gigs - Create a new gig",
            "PUT /gigs/{id} - Update a gig",
            "DELETE /gigs/{id} - Delete a gig"
        ]
    }