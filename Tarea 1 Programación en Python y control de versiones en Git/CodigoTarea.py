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
        return robot_name

    def get_articulacion(articulacion_nombre):
        return articulacion_nombre.Articulaciones_Robot

    def get_pose(Pose_robot):
        return Pose_robot.Pose

 #   def main(self):
 #       self.Articulaciones_Robot = ['Base_Robot', 'art1', 'art2', 'art3', 'art4', 'art5']
  #      self.Pose = [0.0, 2.0, 3.0, 1.0, 2.0, 3.0]
   #     self.nombre_Robot = 'RobotEjemplo'
   #     print(f"Las caracteristicas del robot son. Articulaciones: {self.nombre_Robot} , pose: {self.Pose} y su nombre es: {self.nombre_Robot}")
        
if __name__ == '__main__':
    try:
        main(self)
        self.Articulaciones_Robot = ['Base_Robot', 'art1', 'art2', 'art3', 'art4', 'art5']
        self.Pose = [0.0, 2.0, 3.0, 1.0, 2.0, 3.0]
        self.nombre_Robot = 'RobotEjemplo'
        print(f"Las caracteristicas del robot son. Articulaciones: {self.nombre_Robot} , pose: {self.Pose} y su nombre es: {self.nombre_Robot}")

        
        pass
