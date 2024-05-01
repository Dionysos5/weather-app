import emoji

code_groups = {
    range(200, 233): ":cloud_with_lightning_and_rain:",
    range(300, 322): ":cloud_with_rain:",
    range(500, 505): ":cloud_with_rain:",
    range(511, 512): ":snowflake:",
    range(520, 532): ":cloud_with_rain:",
    range(600, 617): ":snowflake:",
    615: ":cloud_with_snow:",
    616: ":cloud_with_snow:",
    range(620, 623): ":snowflake:",
    701: ":fog:",
    711: ":smoke:",
    721: ":fog:",
    range(731, 772): ":wind_face:",
    741: ":fog:",
    762: ":volcano:",
    781: ":tornado:",
    800: ":sun:",
    801: ":sun_behind_small_cloud:",
    range(802, 805): ":cloud:",
}

def get_emoji(code):
    for code_range, emoji_str in code_groups.items():
        if (
            isinstance(code_range, range) and code in code_range
            or code == code_range
        ):
            return emoji.emojize(emoji_str)
    return None

codes = {str(code): get_emoji(code) for code in range(200, 805)}

class ConditionCodes:
    def __init__(self):
        self.codes = codes

    def get_condition(self, code: int):
        return self.codes.get(str(code), None)