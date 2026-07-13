from fastapi import FastAPI, HTTPException, Depends
from sqlmodel import Session, select, SQLModel, create_engine, Field
from typing import List, Optional
from datetime import datetime

# ============================================
# DATABASE SETUP - SQLite
# ============================================
DATABASE_URL = "sqlite:///./library.db"
engine = create_engine(DATABASE_URL, echo=True)

def get_session():
    with Session(engine) as session:
        yield session

# ============================================
# MODELS
# ============================================

class Book(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True, index=True)
    title: str = Field(index=True, min_length=1, max_length=200)
    author: str = Field(index=True, min_length=1, max_length=100)
    isbn: str = Field(unique=True, index=True)
    published_year: int = Field(ge=1000, le=datetime.now().year)
    available: bool = Field(default=True)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

class BookCreate(SQLModel):
    title: str = Field(min_length=1, max_length=200)
    author: str = Field(min_length=1, max_length=100)
    isbn: str = Field(min_length=10, max_length=13)
    published_year: int = Field(ge=1000, le=datetime.now().year)

class BookUpdate(SQLModel):
    title: Optional[str] = Field(None, min_length=1, max_length=200)
    author: Optional[str] = Field(None, min_length=1, max_length=100)
    isbn: Optional[str] = Field(None, min_length=10, max_length=13)
    published_year: Optional[int] = Field(None, ge=1000, le=datetime.now().year)
    available: Optional[bool] = None

# Create the database tables
SQLModel.metadata.create_all(engine)

# ============================================
# FASTAPI APP
# ============================================

app = FastAPI(
    title="Library API",
    description="A simple library management API",
    version="1.0.0"
)

@app.get("/")
def root():
    return {"message": "Welcome to the Library API"}

@app.post("/books", response_model=Book)
def create_book(book: BookCreate, session: Session = Depends(get_session)):
    """Create a new book"""
    db_book = Book(**book.dict())
    session.add(db_book)
    session.commit()
    session.refresh(db_book)
    return db_book

@app.get("/books", response_model=List[Book])
def list_books(
    skip: int = 0, 
    limit: int = 10, 
    available: Optional[bool] = None,
    session: Session = Depends(get_session)
):
    """List all books with optional filters"""
    query = select(Book)
    if available is not None:
        query = query.where(Book.available == available)
    return session.exec(query.offset(skip).limit(limit)).all()

@app.get("/books/{book_id}", response_model=Book)
def get_book(book_id: int, session: Session = Depends(get_session)):
    """Get a specific book by ID"""
    book = session.get(Book, book_id)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return book

@app.patch("/books/{book_id}", response_model=Book)
def update_book(
    book_id: int,
    book_update: BookUpdate,
    session: Session = Depends(get_session)
):
    """Update a book"""
    book = session.get(Book, book_id)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    
    update_data = book_update.dict(exclude_unset=True)
    for field, value in update_data.items():
        setattr(book, field, value)
    
    book.updated_at = datetime.utcnow()
    session.commit()
    session.refresh(book)
    return book

@app.delete("/books/{book_id}")
def delete_book(book_id: int, session: Session = Depends(get_session)):
    """Delete a book"""
    book = session.get(Book, book_id)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    
    session.delete(book)
    session.commit()
    return {"message": "Book deleted successfully"}