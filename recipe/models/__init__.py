from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# Import models to avoid circular imports
from recipe.models.user import User  
from recipe.models.recipe import Recipe
