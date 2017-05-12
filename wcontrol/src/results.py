from wcontrol.conf.config import BMI, BFP, MUSCLE


class results(object):
    def __init__(self, control, gender):
        self.bmi = self.get_bmi(control.bmi)
        self.fat = self.get_fat(control.fat, gender)
        self.muscle = self.get_muscle(control.muscle, gender)

    def get_bmi(self, bmi):
        for limit, msg in BMI:
            if bmi <= limit:
                return msg

    def get_fat(self, fat, gender):
        for limit_w, limit_m, msg in BFP:
            if gender == 'Feminine' and fat <= limit_w:
                return msg
            if gender == 'Masculine' and fat <= limit_m:
                return msg

    def get_muscle(self, muscle, gender):
        for limit_w, limit_m, msg in MUSCLE:
            if gender == 'Feminine' and muscle <= limit_w:
                return msg
            if gender == 'Masculine' and muscle <= limit_m:
                return msg
