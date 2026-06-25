from vector2d import Vector2D
from projectile_physics import Environment,Projectile

def simulate(launchspeed, angle, mass, Cd, A, dt=0.01):
    env = Environment()
    proj = Projectile(launchspeed, angle, mass)

    while proj.position.y >= 0:
        speed = proj.velocity.magnitude()
        acceleration = Vector2D(0, -env.gravity)

        #F_D = 1/2 * Cd * p * A * v^2
        if speed > 0:
            drag_magnitude = 0.5 * Cd * env.airdensity * A * speed ** 2
            drag_accel = proj.velocity.normalize() * (-drag_magnitude / proj.mass)
            acceleration += drag_accel

        proj.velocity += acceleration * dt
        proj.position += proj.velocity * dt
        proj.history.append(Vector2D(proj.position.x, proj.position.y))
    return proj.history
