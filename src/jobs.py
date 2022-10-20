from functools import lru_cache
import csv


@lru_cache
def read(path):
    with open(path, encoding="utf-8") as file:
        content = csv.DictReader(file)
        infos = []
        for info in content:
            infos.append(info)

    return infos
