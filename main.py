from pydantic import BaseModel
from fastapi import FastAPI, HTTPException, status

app = FastAPI()


class Post(BaseModel):
    id: int
    content: str


# Prepopulate dictionary of posts
posts_db = {
    1: Post(id=1, content="Hello FastAPI!"),
    2: Post(id=2, content="Writing my second post!"),
}


@app.get("/")
def read_root() -> str:
    return "Hello, world!"


@app.get("/about")
def read_about() -> str:
    return "This is a simple HTTP API."


@app.get("/posts")
def list_posts() -> list[Post]:
    return list(posts_db.values())


@app.get("/posts/{post_id}")
def get_post(post_id: int) -> Post:
    if post_id in posts_db:
        return posts_db[post_id]
    raise HTTPException(status_code=404, detail="Post not found")


@app.post("/posts", status_code=status.HTTP_201_CREATED)
def create_post(post: Post):
    if post.id in posts_db:
        raise HTTPException(status_code=400, detail="Post with this ID already exists")
    posts_db[post.id] = post
    return post


@app.put("/posts/{post_id}")
def update_post(post_id: int, updated_post: Post) -> Post:
    if post_id not in posts_db:
        raise HTTPException(status_code=404, detail="Post not found")
    posts_db[post_id] = updated_post
    return updated_post


@app.delete("/posts/{post_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(post_id: int) -> None:
    if post_id not in posts_db:
        raise HTTPException(status_code=404, detail="Post not found")
    del posts_db[post_id]
    return None  # 204 = No Content
