import json


class Settings:
    @staticmethod
    def animation():
        from PyQt5.QtCore import QEasingCurve
        with open("data/settings.json", "r") as file:
            settings = json.load(file)

        animation = QEasingCurve.InOutQuart
        timing = 300
        match settings["animation"]:
            case "InOutQuart":
                animation = QEasingCurve.InOutQuart
            case "InOutBack":
                animation = QEasingCurve.InOutBack
            case "InOutBounce":
                animation = QEasingCurve.InOutBounce
            case "OutBack":
                animation = QEasingCurve.OutBack
            case "OutElastic":
                animation = QEasingCurve.OutElastic
                timing = 1000

        return {
            "animation": animation,
            "timing": timing
        }
