from wcontrol.conf.config import BMI, BFP, MUSCLE, VISCERAL


class results(object):
    def __init__(self, control, gender):
        self.weight = ''
        self.bmi = self.get_bmi(control.bmi)
        self.fat = self.get_fat(control.fat, gender)
        self.muscle = self.get_muscle(control.muscle, gender)
        self.rmr = ''
        self.visceral = self.get_visceral(control.visceral)
        self.bodyage = ''

    def get_bmi(self, bmi):
        for limit, msg in BMI:
            if bmi <= limit:
                return msg

    def get_fat(self, fat, gender):
        for limit_w, limit_m, msg in BFP:
            if gender == 'Female' and fat <= limit_w:
                return msg
            if gender == 'Male' and fat <= limit_m:
                return msg

    def get_muscle(self, muscle, gender):
        for limit_w, limit_m, msg in MUSCLE:
            if gender == 'Female' and muscle <= limit_w:
                return msg
            if gender == 'Male' and muscle <= limit_m:
                return msg

    def get_visceral(self, visceral):
        for limit, msg in VISCERAL:
            if visceral <= limit:
                return msg

    def __getitem__(self, index):
        if index == 0:
            return self.weight
        if index == 1:
            return self.bmi
        if index == 2:
            return self.fat
        if index == 3:
            return self.muscle
        if index == 4:
            return self.visceral
        if index == 5:
            return self.rmr
        if index == 6:
            return self.bodyage
