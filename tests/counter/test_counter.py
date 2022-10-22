# from src.counter import count_ocurrences
from src.counter import count_ocurrences
import pytest

path = 'src/jobs.csv'


def test_counter():
    "Testa retorno para a palavra Batista"
    assert count_ocurrences(path, "Batista") == 30

    "Testa retorno para a palavra baTista"
    assert count_ocurrences(path, "baTista") == 30

    "Testa resultado passando um número"
    with pytest.raises(AttributeError):
        count_ocurrences(path, 18)
