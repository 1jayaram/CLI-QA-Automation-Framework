
from workloadsim.storage import (
    create_job,
    find_job,
    get_all_jobs,
    update_job_status
)


def submit_job(job_id, cpu, memory):
    if cpu <= 0:
        raise ValueError("CPU must be greater than zero")

    if memory <= 0:
        raise ValueError("Memory must be greater than zero")

    if find_job(job_id):
        raise ValueError("Job ID already exists")

    create_job(job_id, cpu, memory)
    
    job = find_job(job_id)

    return dict(job)


def get_job_status(job_id):
    job = find_job(job_id)

    if not job:
        raise ValueError("Job not found")

    return dict(job)


def cancel_job(job_id):
    job = find_job(job_id)

    if not job:
        raise ValueError("Job not found")

    if job["status"] == "cancelled":
        raise ValueError("Job already cancelled")

    if job["status"] == "completed":
        raise ValueError("Completed job cannot be cancelled")

    update_job_status(job_id, "cancelled")
    
    job = find_job(job_id)

    return dict(job)



def list_jobs():
    return get_all_jobs()
