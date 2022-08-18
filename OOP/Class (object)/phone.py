class Phone:
    '''This class represents phone's specs'''

    def __init__(self, company, model, screen, SOC):
        self.company = company
        self.model = model
        self.screen = screen
        self.SOC = SOC

    def __del__(self):
        print("All information is gone")
