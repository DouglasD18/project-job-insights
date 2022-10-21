from src import jobs


def get_unique_job_types(path):
    infos = jobs.read(path)
    job_types = []
    for content in infos:
        types = content["job_type"]
        if types and types not in job_types:
            job_types.append(types)

    return job_types


def filter_by_job_type(jobs, job_type):
    same_jobs = []
    for job in jobs:
        if job["job_type"] == job_type:
            same_jobs.append(job)
    return same_jobs


def get_unique_industries(path):
    infos = jobs.read(path)
    industry = []
    for content in infos:
        types = content["industry"]
        if types and types not in industry:
            industry.append(types)

    return industry


def filter_by_industry(jobs, industry):
    same_industry = []
    for job in jobs:
        if job["industry"] == industry:
            same_industry.append(job)
    return same_industry


def get_max_salary(path):
    infos = jobs.read(path)
    max_salary = -1
    for info in infos:
        if info["max_salary"].isnumeric():
            value = int(info["max_salary"])
            if value > max_salary:
                max_salary = value

    return max_salary


def get_min_salary(path):
    infos = jobs.read(path)
    min_salary = []
    for info in infos:
        if info["min_salary"].isnumeric():
            value = int(info["min_salary"])
            min_salary.append(value)

    return min(min_salary)


def matches_salary_range(job, salary):
    if (
        "min_salary" not in job
        or "max_salary" not in job
    ):
        raise ValueError()

    min_salary = job["min_salary"]
    max_salary = job["max_salary"]

    if (
        not isinstance(min_salary, int)
        or not isinstance(max_salary, int)
        or int(min_salary) > int(max_salary)
        or not isinstance(salary, int)
    ):
        raise ValueError()

    if int(min_salary) <= salary <= int(max_salary):
        return True
    else:
        return False


def try_valid_jobs(job, salary):
    try:
        if matches_salary_range(job, salary):
            return job
    except ValueError:
        return None


def filter_by_salary_range(jobs, salary):
    valid_salaries = []
    for job in jobs:
        valid = try_valid_jobs(job, salary)
        if valid is not None:
            valid_salaries.append(job)

    return valid_salaries
