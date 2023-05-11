from flask import Blueprint, g, request

from flasktodos import middlewares
from flasktodos.cache import cache
from flasktodos.database import db
from flasktodos.models import Todo, TodoSchema


blueprint = Blueprint("todos", __name__)
blueprint.before_request(middlewares.auth)


def cache_key():
    return f"{g.user.id}/todos"


@blueprint.get("/")
def all_todos():
    if cache.has(cache_key()):
        return cache.get(cache_key())

    todos = TodoSchema().dump(g.user.todos, many=True)
    cache.set(cache_key(), todos)

    return todos


@blueprint.get("/<int:id>")
def single_todo(id: int):
    todo = Todo.query.filter_by(id=id, user_id=g.user.id).first_or_404()
    return TodoSchema().dump(todo)


@blueprint.post("/")
def create_todo():
    todo = TodoSchema().load(request.json, transient=True)
    g.user.todos.append(todo)
    db.session.commit()
    cache.delete(cache_key())

    response = {
        "message": f"Todo saved successfully",
        "todo": TodoSchema().dump(todo),
    }

    return response, 201


@blueprint.put("/<int:id>")
def update_todo(id: int):
    todo = TodoSchema().load(
        data=request.json,
        instance=Todo.query.filter_by(id=id, user_id=g.user.id).first_or_404(),
        session=db.session,
    )

    db.session.commit()
    cache.delete(cache_key())

    return {"message": "Todo updated successfully"}


@blueprint.delete("/<int:id>")
def delete_todo(id: int):
    todo = Todo.query.filter_by(id=id, user_id=g.user.id).first_or_404()
    db.session.delete(todo)
    db.session.commit()
    cache.delete(cache_key())

    return {"message": "Todo deleted successfully"}
