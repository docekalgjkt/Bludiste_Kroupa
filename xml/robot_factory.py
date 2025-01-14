from robot import Robot
from robot_vykresleni import RobotView
from vykresleni import BludisteCanvas

class AbstractRobotFactory:
    """Abstraktní továrna pro vytváření robotů a jejich zobrazení."""
    def create_robot(self, bludiste):
        raise NotImplementedError

    def create_robot_view(self, canvas, robot):
        raise NotImplementedError


class BasicRobotFactory(AbstractRobotFactory):
    """Konkrétní továrna pro základního robota."""
    def create_robot(self, bludiste):
        return Robot(bludiste)

    def create_robot_view(self, canvas, robot):
        return RobotView(canvas, robot)