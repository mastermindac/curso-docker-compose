from typing import Callable

from flask import Blueprint

from .auth import auth


def apply(middleware: Callable, blueprints: Blueprint | list[Blueprint]):
    if not isinstance(blueprints, list):
        blueprints = [blueprints]
    
    for blueprint in blueprints:
        blueprint.before_request(middleware)
