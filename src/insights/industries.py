from typing import List, Dict
from src.insights.jobs import read


def get_unique_industries(path: str) -> List[str]:
    data = read(path)
    industries = [jobs["industry"] for jobs in data if jobs["industry"]]
    return set(industries)


def filter_by_industry(jobs: List[Dict], industry: str) -> List[Dict]:
    return [job for job in jobs if job["industry"] == industry]
