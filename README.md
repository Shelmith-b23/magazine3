# Magazine Author-Article System

This project demonstrates a simple **Python object-oriented system** to manage Authors, Magazines, and Articles. It models **many-to-many relationships**:  

- An **Author** can write multiple **Articles**.  
- A **Magazine** can have articles from multiple **Authors**.  

---

## Folder Structure


---

## Classes

### 1. Author

- Attributes:
  - `name` — Author's name
- Methods:
  - `add_article(magazine, title)` — Create a new Article for the author
  - `articles()` — List all articles written by the author
  - `magazines()` — List all magazines the author has written for
  - `topic_areas()` — List unique magazine categories the author has written in

### 2. Magazine

- Attributes:
  - `name` — Magazine name
  - `category` — Magazine category (topic)

### 3. Article

- Attributes:
  - `author` — Author instance
  - `magazine` — Magazine instance
  - `title` — Article title
- Class Attributes:
  - `all` — List of all Article instances

---

## Usage

1. Open terminal and navigate to the project folder:

```bash
cd /path/to/magazine3
Liscence
MIT liscense
