def rocket_trajectory(thrust, drag_coefficient, cross_sectional_area, initial_velocity, 
                      initial_height, mass, time_step, total_time):
    g = 9.81  # Gravity acceleration (m/s²)
    air_density = 1.225  # Air density (kg/m³)
    velocity = initial_velocity
    height = initial_height

    for t in range(0, total_time, time_step):
        gravity_force = mass * g
        drag_force = 0.5 * air_density * drag_coefficient * cross_sectional_area * velocity ** 2
        net_force = thrust - gravity_force - drag_force
        acceleration = net_force / mass

        velocity += acceleration * time_step
        height += velocity * time_step

        if height <= 0:
            break

    return height, velocity

# Example usage
final_height, final_velocity = rocket_trajectory(thrust=10000, drag_coefficient=0.75,
                                                 cross_sectional_area=1, initial_velocity=0,
                                                 initial_height=0, mass=1000, time_step=1,
                                                 total_time=100)
print("Final Height:", final_height, "meters")
print("Final Velocity:", final_velocity, "m/s")