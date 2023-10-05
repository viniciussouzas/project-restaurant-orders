from src.models.ingredient import Ingredient  # noqa: F401, E261, E501


# Req 1
def test_ingredient():
    salt_ingredient = Ingredient('salt')
    pepper_ingredient = Ingredient('pepper')

    assert salt_ingredient.name == 'salt'
    assert pepper_ingredient.name == 'pepper'

    assert hash(salt_ingredient) == hash('salt')
    assert hash(pepper_ingredient) == hash('pepper')

    assert salt_ingredient == salt_ingredient
    assert salt_ingredient != pepper_ingredient

    assert repr(salt_ingredient) == "Ingredient('salt')"
    assert repr(pepper_ingredient) == "Ingredient('pepper')"

    assert salt_ingredient.restrictions == set()
    assert pepper_ingredient.restrictions == set()