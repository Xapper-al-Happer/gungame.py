import os
import ursina


class Wall(ursina.Entity):
    def __init__(self, position):
        super().__init__(
            position=position,
            scale=2,
            model="cube",
            texture=os.path.join("assets", "A5A.mp4"),
            origin_y=-0.5
        )
        # used to be  self.texture.filtering = None
        self.collider = ursina.BoxCollider(self, size=ursina.Vec3(1, 2, 1))


class Map:
    def __init__(self):
        for y in range(1, 4, 2):
            Wall(ursina.Vec3(17, y, 0))
            Wall(ursina.Vec3(17, y, 0))
            Wall(ursina.Vec3(17, y, 2))
            Wall(ursina.Vec3(17, y, 4))
            Wall(ursina.Vec3(17, y, 6))
            Wall(ursina.Vec3(17, y, 8))
            Wall(ursina.Vec3(17, y, 10))
            Wall(ursina.Vec3(17, y, 12))
            Wall(ursina.Vec3(17, y, 14))
            Wall(ursina.Vec3(17, y, 16))
            Wall(ursina.Vec3(17, y, 18))
# was (6, y, 0)

            Wall(ursina.Vec3(10, y, 18))
            Wall(ursina.Vec3(16, y, 18))
            Wall(ursina.Vec3(8, y, 18))
            Wall(ursina.Vec3(6, y, 18))
            Wall(ursina.Vec3(10, y, 18))
            Wall(ursina.Vec3(4, y, 18))
