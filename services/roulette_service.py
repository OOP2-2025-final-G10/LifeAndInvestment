# 1〜10・回転式・角速度減衰ルーレット
import random
import time
from controllers.frontend_controller import FrontendController


class RouletteService:

    @staticmethod
    def spin():
        angle = 0.0
        angular_velocity = random.uniform(20.0, 40.0)  # 初期角速度（deg/frame）
        decay = random.uniform(0.90, 0.97)              # 減衰率

        while angular_velocity > 0.1:
            angle += angular_velocity
            angle %= 360.0

            # フロントエンドへ現在角度を通知
            FrontendController.send_roulette_angle(angle)

            angular_velocity *= decay
            time.sleep(0.02)  # フレーム間隔（約50fps）

        # 360度を10分割 → 1〜10
        result = int(angle / 36) + 1

        FrontendController.send_roulette_result(result)
        return result
