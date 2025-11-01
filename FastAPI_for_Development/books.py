import json
from fastapi import FastAPI, HTTPException, Path
from pydantic import BaseModel, Field

class Book(BaseModel):
    id: str  # changed from UUID to str
    title: str = Field(..., example="The Great Gatsby")
    author: str = Field(..., example="F. Scott Fitzgerald")
    description: str = Field(..., example="A novel by F. Scott Fitzgerald")
    rating: int = Field(gt=1, lt=100, example=4)
    
def load_data():
    try:
        with open("data.json", "r") as file:
            data = json.load(file)
            return [Book(**item) for item in data]
    except FileNotFoundError:
        return []

def save_data(data):
    with open('data.json', 'w') as file:
        json.dump([book.dict() for book in data], file, indent=4)

BOOKS = load_data()
app = FastAPI()

@app.get('/')
def read_api():
    return BOOKS

@app.get('/book/{book_id}')
def read_book(book_id: str = Path(..., description="The ID of the book to retrieve")):
    for book in BOOKS:
        if book.id == book_id:
            return book
    raise HTTPException(status_code=404, detail="Book not found")

@app.post('/')
def create_book(book: Book):
    # Optional: check if ID already exists
    for b in BOOKS:
        if b.id == book.id:
            raise HTTPException(status_code=400, detail="Book ID already exists")
    BOOKS.append(book)
    save_data(BOOKS)
    return book

@app.put('/{book_id}')
def update_book(book_id: str, book: Book):
    for index, existing_book in enumerate(BOOKS):
        if existing_book.id == book_id:
            BOOKS[index] = book
            save_data(BOOKS)
            return BOOKS[index]
    raise HTTPException(status_code=404, detail="Book not found")

@app.delete('/{book_id}')
def delete_book(book_id: str):
    for index, existing_book in enumerate(BOOKS):
        if existing_book.id == book_id:
            deleted_book = BOOKS.pop(index)
            save_data(BOOKS)
            return {"message": f"Book with id {deleted_book.id} deleted"}
    raise HTTPException(status_code=404, detail="Book not found")
