from apscheduler.schedulers.background import BackgroundScheduler
from .jobs import *


def update_totally():
    scheduler = BackgroundScheduler()
    scheduler.add_job(check_all_symbole, 'interval', seconds=15)
    scheduler.start()


def update_eur1():
    scheduler = BackgroundScheduler()
    scheduler.add_job(get_data_euro_m1, 'interval', seconds=10)
    scheduler.start()


def update_eur5():
    scheduler = BackgroundScheduler()
    scheduler.add_job(get_data_euro_m5, 'interval', seconds=10)
    scheduler.start()


def update_xau1():
    scheduler = BackgroundScheduler()
    scheduler.add_job(get_data_xau_m1, 'interval', seconds=9)
    scheduler.start()


def update_gbp1():
    scheduler = BackgroundScheduler()
    scheduler.add_job(get_data_gbp_m1, 'interval', seconds=9)
    scheduler.start()


def update_gbp5():
    scheduler = BackgroundScheduler()
    scheduler.add_job(get_data_gbp_m5, 'interval', seconds=9)
    scheduler.start()
