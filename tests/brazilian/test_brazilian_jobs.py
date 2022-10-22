# from src.brazilian_jobs import read_brazilian_file
from src.brazilian_jobs import read_brazilian_file

path = 'tests/mocks/brazilians_jobs.csv'


def test_brazilian_jobs():
    "Testa o retorno dos headers"
    dic = read_brazilian_file(path)[0]
    keys = list(dic)
    assert keys[0] == 'title'
    assert keys[1] == 'salary'
    assert keys[2] == 'type'
