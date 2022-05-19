import json


class Settings:
    @staticmethod
    def fix() -> None:
        settings = {
            "animation": "InOutQuart",
            "app_id": None,
            "key": None,
            "secret": None,
            "cluster": None,
            "client_id": None
        }
        with open("data/settings.json", "w") as file:
            json.dump(settings, file)

    @staticmethod
    def get_settings() -> dict:
        try:
            with open("data/settings.json", "r") as file:
                return json.load(file)
        except:
            Settings.fix()
            Settings.get_settings()

    @staticmethod
    def animation() -> dict:
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

    @staticmethod
    def update(key: str, value: str) -> dict:
        with open("data/settings.json", "r") as file:
            settings = json.load(file)

        settings[key] = value

        with open("data/settings.json", "w") as file:
            json.dump(settings, file)

        return settings
