import emoji

code_groups = [
    (range(200, 233), ":cloud_with_lightning_and_rain:"),
    (range(300, 322), ":cloud_with_rain:"),
    (range(500, 532), ":cloud_with_rain:"),
    (range(600, 623), ":snowflake:"),
    (range(701, 762), ":fog:"),
    (762, ":volcano:"),
    (771, ":wind_face:"),
    (781, ":tornado:"),
    (800, ":sun:"),
    (801, ":sun_behind_small_cloud:"),
    (range(802, 805), ":cloud:"),
]

def get_emoji(code: int) -> str:
    for code_range, emoji_str in code_groups:
        if isinstance(code_range, range):
            if code in code_range:
                return emoji.emojize(emoji_str)
        elif code == code_range:
            return emoji.emojize(emoji_str)
    return None

class ConditionCodes:
    def __init__(self):
        self.codes = {str(code): get_emoji(code) for code in range(200, 805)}

    def get_condition(self, code: int) -> str:
        if code < 200 or code > 804:
            return None
        return self.codes.get(str(code), None)