from typing import Union, List, Dict
from .jobs import read


def get_max_salary(path: str) -> int:
    data = read(path)
    salaries = [
        int(job["max_salary"]) for job in data
        if job["max_salary"].isdigit()
    ]
    return max(salaries)


def get_min_salary(path: str) -> int:
    data = read(path)
    salaries = [
        int(job["min_salary"]) for job in data
        if job["min_salary"].isdigit()
    ]
    return min(salaries)


def matches_salary_range(job: Dict, salary: Union[int, str]) -> bool:
    try:
        if "min_salary" not in job or "max_salary" not in job:
            raise ValueError("Values not found")

        min_salary = int(job["min_salary"])
        max_salary = int(job["max_salary"])
        search_salary = int(salary)

        if min_salary > max_salary:
            raise ValueError("Minimal salary cannot be higher than maximum")

        return min_salary <= search_salary <= max_salary

    except (ValueError, TypeError, KeyError):
        raise ValueError("Something went wrong")


def filter_by_salary_range(
    jobs: List[dict],
    salary: Union[str, int]
) -> List[Dict]:
    """Filters a list of jobs by salary range
    Parameters
    ----------
    jobs : list
        The jobs to be filtered
    salary : int
        The salary to be used as filter
    Returns
    -------
    list
        Jobs whose salary range contains `salary`
    """
    raise NotImplementedError
