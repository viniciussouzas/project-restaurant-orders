from src.models.dish import Dish  # noqa: F401, E261, E501
from src.models.ingredient import Ingredient
import pytest


# Req 2
def test_dish():
    spaghetti = Dish('Spaguetti', 27.90)
    baby_beef = Dish('Baby Beef', 35.90)

    assert spaghetti.name == 'Spaguetti'
    assert baby_beef.name == 'Baby Beef'

    assert hash(spaghetti) == hash(repr(spaghetti))
    assert hash(baby_beef) == hash(repr(baby_beef))
    assert hash(spaghetti) != hash(repr(baby_beef))

    assert spaghetti == spaghetti
    assert spaghetti != baby_beef

    assert repr(spaghetti) == "Dish('Spaguetti', R$27.90)"
    assert repr(baby_beef) == "Dish('Baby Beef', R$35.90)"

    spaghetti.add_ingredient_dependency(Ingredient('Pasta'), 1)
    baby_beef.add_ingredient_dependency(Ingredient('Beef'), 1)

    assert spaghetti.recipe == {Ingredient('Pasta'): 1}
    assert spaghetti.get_ingredients() == set(spaghetti.recipe.keys())
    assert spaghetti.get_restrictions() == set()

    assert baby_beef.recipe == {Ingredient('Beef'): 1}
    assert baby_beef.get_ingredients() == set(baby_beef.recipe.keys())
    assert baby_beef.get_restrictions() == set()

    with pytest.raises(TypeError, match="Dish price must be float"):
        Dish('Spaguetti', '1')

    with pytest.raises(ValueError, match="Dish price must be greater then zero"):
        Dish('Spaguetti', 0)
