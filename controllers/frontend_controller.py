#フロントエンドへの「通知専用」
class FrontendController:

    @staticmethod
    def send_scroll_position(x: int, y: int):
        print(f"[Frontend] Scroll position -> x:{x}, y:{y}")

    @staticmethod
    def send_money_update(before: int, after: int):
        diff = after - before
        print(f"[Frontend] Money update -> {before} → {after} (diff: {diff})")

    @staticmethod
    def send_roulette_angle(angle: float):
        # degree（0〜360）
        print(f"[Frontend] Roulette angle -> {angle:.2f}")

    @staticmethod
    def send_roulette_result(value: int):
        print(f"[Frontend] Roulette result -> {value}")
