import math

def pro_mot(velo, angle):
    g = 9.81
    angle_rad = math.radians(angle)  
    
    R = (velo**2 * math.sin(2 * angle_rad)) / g
    H = (velo**2 * (math.sin(angle_rad)**2)) / (2 * g)  
    
    return R, H

# Example usage
dist, height = pro_mot(11.0, 20.0)
print("Horizontal distance:", dist)  
print("Maximum height:", height)
