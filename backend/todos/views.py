from flask import request

from .app import app
from .cache import cache
from .database import db
from .models import Todo, TodoSchema


@app.get("/todos")
@cache.cached()
def all_todos():
    return TodoSchema().dump(Todo.query.all(), many=True)


@app.get("/todos/<int:id>")
def single_todo(id: int):
    return TodoSchema().dump(Todo.query.get(id))


@app.post("/todos")
def create_todo():
    todo = TodoSchema().load(request.json, transient=True)
    db.session.add(todo)
    db.session.commit()
    cache.clear()

    response = {
        "message": f"Todo saved successfully",
        "todo": TodoSchema().dump(todo),
    }

    return response, 201


@app.put("/todos/<int:id>")
def update_todo(id: int):
    todo = TodoSchema().load(
        data=request.json,
        instance=Todo.query.get(id),
        session=db.session,
    )

    db.session.commit()
    cache.clear()

    return {"message": "Todo updated successfully"}


@app.delete("/todos/<int:id>")
def delete_todo(id: int):
    todo = Todo.query.get_or_404(id)
    db.session.delete(todo)
    db.session.commit()
    cache.clear()

    return {"message": "Todo deleted successfully"}
