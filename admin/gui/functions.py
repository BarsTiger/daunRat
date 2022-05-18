from data.settings import Settings
import ctypes
from ezzthread import threaded


def popup(title, text, style=0):
    """
    Styles:
    0 : OK
    1 : OK | Cancel
    2 : Abort | Retry | Ignore
    3 : Yes | No | Cancel
    4 : Yes | No
    5 : Retry | Cancel
    6 : Cancel | Try Again | Continue
    """
    return ctypes.windll.user32.MessageBoxW(0, text, title, style)


@threaded
def t_popup(title, text, style=0):
    popup(title, text, style)


def fill_settings(ui) -> None:
    settings = Settings.get_settings()
    ui.chooseAnimationBox.setCurrentText(settings.get("animation"))
    ui.pusher_app_id_edit.setText(settings.get("app_id"))
    ui.pusher_key_edit.setText(settings.get("key"))
    ui.pusher_secret_edit.setText(settings.get("secret"))
    ui.pusher_cluster_edit.setText(settings.get("cluster"))
    ui.imgurClientId.setText(settings.get("client_id"))


def update_settings(ui) -> None:
    get_text = lambda text: text if text != "" else None

    settings = {
        "animation": get_text(ui.chooseAnimationBox.currentText()),
        "app_id": get_text(ui.pusher_app_id_edit.text().strip()),
        "key": get_text(ui.pusher_key_edit.text().strip()),
        "secret": get_text(ui.pusher_secret_edit.text().strip()),
        "cluster": get_text(ui.pusher_cluster_edit.text().strip()),
        "client_id": get_text(ui.imgurClientId.text().strip())
    }
    list(map((lambda x: Settings.update(x, settings[x])), settings))
    return Settings.get_settings()
