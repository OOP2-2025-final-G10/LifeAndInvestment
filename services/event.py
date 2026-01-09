from models.user import User
from models.job import Job
from controllers.frontend_controller import FrontendController


class Event:

    #所持金を変更する
    @staticmethod
    def change_money(user: User, amount: int):
        user.money += amount

    #職業を変更する
    @staticmethod
    def change_job(user: User, new_job_name: str):
        user.job =  Job.from_name(new_job_name)

    #給料を支払う
    @staticmethod
    def give_salary(user: User):
        if not user.job:
            return
        user.money += user.job.salary
    
    
