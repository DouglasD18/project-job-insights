# from src.sorting import sort_by
from src.sorting import sort_by
import pytest


def list_dicts():
    return [
        {"date_posted": "2021-11-09", "min_salary": 3000, "max_salary": 7740},
        {"date_posted": "2022-08-18", "min_salary": 3500, "max_salary": 9750},
        {"date_posted": "2020-10-18", "min_salary": 5000, "max_salary": 8000}
    ]


def test_sort_by_criteria():
    jobs = list_dicts()
    "Testa se funciona corretamente"
    sort_by(jobs, "max_salary")
    assert jobs[1]["max_salary"] == 8000

    "Testa resultado passando um critério errado"
    with pytest.raises(ValueError):
        sort_by(jobs, "salary")
