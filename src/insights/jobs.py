from functools import lru_cache
from typing import List, Dict
import csv


@lru_cache
def read(path: str) -> List[Dict]:
    with open(path) as file:
        jobs = csv.DictReader(file)
        return [job for job in jobs]


def get_unique_job_types(path: str) -> List[str]:
    data = read(path)
    return set(unique_jobs["job_type"] for unique_jobs in data)


def filter_by_job_type(jobs: List[Dict], job_type: str) -> List[Dict]:
    return [job for job in jobs if job["job_type"] == job_type]
