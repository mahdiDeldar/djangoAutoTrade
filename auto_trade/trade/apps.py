from django.apps import AppConfig


class TradeConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'trade'

    def ready(self):
        from .job_schedule import schedule_interval
        schedule_interval.update_totally()
        # schedule_interval.update_eur1()
        # schedule_interval.update_eur5()
        # schedule_interval.update_xau1()
        # schedule_interval.update_gbp1()
        # schedule_interval.update_gbp5()
