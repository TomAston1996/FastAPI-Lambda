from fastapi import FastAPI, HTTPException, status
from fastapi.encoders import jsonable_encoder
import random
import os
import json
from pydantic import BaseModel
from typing import Optional, Literal
from uuid import uuid4

### uvicorn main:app --reload

app = FastAPI()

class Book(BaseModel): 
    name: str
    price: float
    genre: Literal['fiction', 'non-fiction'] #list to choose from
    book_id: Optional[str] = uuid4().hex #unique id


BOOKS_FILE = 'books.json'
BOOK_DATABASE = []
if os.path.exists(BOOKS_FILE): 
    with open(BOOKS_FILE, 'r') as f: 
        BOOK_DATABASE = json.load(f)


@app.get('/')
async def home():
    return {'message': 'root'}


@app.get('/list-books')
async def list_books(): 
    return {'books': BOOK_DATABASE}


@app.get('/book-by-index/{item_id}')
async def book_by_index(item_id: int):
    try:
        book = BOOK_DATABASE[int(item_id)]
    except: 
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail = 'item_id not found')
    return {'book': book}


@app.get('/get-random-book')
async def get_random_book(): 
    return random.choice(BOOK_DATABASE)


@app.post('/add-book')
async def add_book(book: Book):
    book.book_id = uuid4().hex
    json_book = jsonable_encoder(book)
    BOOK_DATABASE.append(json_book)
    with open(BOOKS_FILE, 'w') as f: 
        json.dump(BOOK_DATABASE, f)

    return {'detail': f'Book {book.name} added', 'book_id': book.book_id}

@app.get('/get-book')
async def get_book(book_id: str): 
    print('1') 
    for book in BOOK_DATABASE:
        if book['book_id'] == book_id: 
            return book
        
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail='book_id not found')