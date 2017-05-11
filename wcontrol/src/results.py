from wcontrol.conf.config import BMI


class results(object):
    def __init__(self, control):
        self.bmi = self.get_bmi(control.bmi)

    def get_bmi(self, bmi):
        for limit, msg in BMI:
            if bmi <= limit:
                return msg
