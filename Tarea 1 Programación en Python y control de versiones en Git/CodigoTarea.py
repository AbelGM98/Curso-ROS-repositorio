
class Robot:
    Articulaciones_Robot = ['Base_Robot', 'art1', 'art2', 'art3', 'art4', 'art5']
    ValorArt_Robot = [0.0, 2.0, 3.0, 1.0, 2.0, 3.0]
    nombre_Robot = 'RobotEjemplo'

    x = 0
    y = 0
    z = 0
    rxr = 0
    ryr = 0
    rzr = 0
    base = 0
    Pose = [x, y, z, rxr, ryr, rzr]

    def set_name(robot_name):
        robot_name.nombre_Robot='Nuevo_Robot'

    def get_articulacion(articulacion_nombre):
        return articulacion_nombre.Articulaciones_Robot

    def get_Pose(Pose_robot):
        return Pose_robot.Pose

if __name__=='__main__':

    def main():
        print()

        return 0

