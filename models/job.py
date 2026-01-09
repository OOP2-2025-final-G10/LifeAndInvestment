class Job:
    def __init__(self, job_id: int, name: str, salary: int):
        self.job_id = job_id
        self.name = name
        self.salary = salary
    
    @classmethod
    def from_name(cls, name: str):
        JOB_MASTER = {
            "会社員": cls("会社員", 3000),
            "医者": cls("医者", 8000),
            "無職": cls("無職", 0),
        }
        return JOB_MASTER.get(name)

    def to_dict(self):
        return {"job_id": self.job_id, "name": self.name, "salary": self.salary}
