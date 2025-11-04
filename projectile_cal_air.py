import numpy as np
import plotly.graph_objects as go

# === 1. DEFINE CONSTANTS (from the paper) ===
g = 9.8      # Acceleration due to gravity (m/s^2)
m = 2.0      # Mass of the ball (kg) [cite: 160]
c_d = 0.45   # Drag coefficient for a sphere [cite: 160]
r = 0.5      # Radius of the ball (m) [cite: 160]
rho_air = 0.0175 # Density of air [cite: 160] (Note: paper's code calls this ro_mars [cite: 318])
A = np.pi * r**2 # Cross-sectional area (m^2) [cite: 317]

# === 2. DEFINE INITIAL LAUNCH PARAMETERS ===
v0 = 100      # Initial velocity (m/s)
theta_deg = 45 # Launch angle (degrees)

# === 3. DEFINE SIMULATION PARAMETERS ===
dt = 0.01  # The "tiny time step" (in seconds)

# === 4. INITIALIZE SIMULATION (for Drag Model) ===
# Convert angle to radians for numpy
theta_rad = np.radians(theta_deg)

# Set starting position
x = 0.0
y = 0.0

# Set starting velocity components
v_x = v0 * np.cos(theta_rad)
v_y = v0 * np.sin(theta_rad)

# Create lists to store the path as we build it
x_points = [x]
y_points = [y]

# === 5. RUN THE SIMULATION (The "Game Loop") ===
# Keep running as long as the ball is above the ground (y >= 0)
while y >= 0:
    
    # --- Calculate Forces at this moment ---
    
    # 1. Calculate current speed and drag force
    #    v = sqrt(v_x^2 + v_y^2)
    v = np.sqrt(v_x**2 + v_y**2)
    
    #    F_air = 0.5 * c_d * rho * A * v^2  
    F_air = 0.5 * c_d * rho_air * A * (v**2)
    
    # 2. Break drag force into x and y components
    #    This is the trickiest part. The force opposes the velocity vector.
    F_drag_x = -F_air * (v_x / v)  # Opposes horizontal velocity
    F_drag_y = -F_air * (v_y / v)  # Opposes vertical velocity
    
    # 3. Calculate gravity force (only in y-direction)
    F_g = -m * g
    
    # 4. Calculate TOTAL force in each direction
    F_total_x = F_drag_x
    F_total_y = F_g + F_drag_y # Gravity and Drag combine
    
    # --- Update motion based on this time step 'dt' ---
    
    # 1. Calculate acceleration (a = F / m)
    a_x = F_total_x / m
    a_y = F_total_y / m
    
    # 2. Update velocity (new_v = old_v + a * dt)
    v_x = v_x + (a_x * dt)
    v_y = v_y + (a_y * dt)
    
    # 3. Update position (new_pos = old_pos + v * dt)
    x = x + (v_x * dt)
    y = y + (v_y * dt)
    
    # --- Store this new point ---
    x_points.append(x)
    y_points.append(y)


# === 6. CALCULATE IDEAL PATH (for comparison) ===
# We use the simple formulas from the previous example
v_x0_ideal = v0 * np.cos(theta_rad)
v_y0_ideal = v0 * np.sin(theta_rad)
t_f_ideal = (2 * v_y0_ideal) / g

# Create time steps
t_ideal = np.linspace(0, t_f_ideal, len(x_points))
x_ideal = v_x0_ideal * t_ideal
y_ideal = (v_y0_ideal * t_ideal) - (0.5 * g * t_ideal**2)


# === 7. PLOT WITH PLOTLY ===
fig = go.Figure()

# Add the "Gravity and Drag" path
fig.add_trace(go.Scatter(
    x=x_points, 
    y=y_points, 
    mode='lines', 
    name='Gravity and Drag',
    line=dict(color='blue', dash='dot')
))

# Add the "Gravity Only" path
fig.add_trace(go.Scatter(
    x=x_ideal, 
    y=y_ideal, 
    mode='lines', 
    name='Gravity Only (Ideal)',
    line=dict(color='black', dash='dot')
))

# Update layout (similar to the paper's graphs)
fig.update_layout(
    title=f'Trajectory (v0={v0} m/s, angle={theta_deg}°) - With vs. Without Air Resistance',
    xaxis_title='Displacement in x-direction (m)',
    yaxis_title='Displacement in y-direction (m)',
    legend_title='Simulation Model',
    yaxis=dict(scaleanchor="x", scaleratio=1, range=[0, None]) # Enforce same scale and start y-axis at 0
)

fig.show()