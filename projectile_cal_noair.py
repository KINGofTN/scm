import numpy as np
import plotly.graph_objects as go

# === 1. DEFINE INPUTS ===
v0 = 50      # Initial velocity (m/s)
theta_deg = 45 # Launch angle (degrees)
g = 9.8      # Acceleration due to gravity (m/s^2)

# === 2. BREAK DOWN VELOCITY ===
# NumPy's trig functions need the angle in radians, not degrees
theta_rad = np.radians(theta_deg)

# Calculate initial x and y components
v_x0 = v0 * np.cos(theta_rad)
v_y0 = v0 * np.sin(theta_rad)

# === 3. CALCULATE TIME OF FLIGHT ===
# We use the formula from the article 
t_f = (2 * v_y0) / g

# === 4. CREATE TIME STEPS ===
# Create an array of 100 time points from 0 to the final time
# 'np.linspace' is perfect for this.
t = np.linspace(0, t_f, 100)

# === 5. CALCULATE (X, Y) POSITIONS ===
# This is the power of NumPy! We apply the formulas to the
# entire 't' array at once.
x = v_x0 * t
y = (v_y0 * t) - (0.5 * g * t**2)

# === 6. PLOT WITH PLOTLY ===
# Create a figure
fig = go.Figure()

# Add the (x, y) data as a line plot (scatter plot)
fig.add_trace(go.Scatter(
    x=x, 
    y=y, 
    mode='lines', 
    name=f'Trajectory (v0={v0} m/s, angle={theta_deg}°)'
))

# Update the layout to add titles and make it look clean
fig.update_layout(
    title='Ideal Projectile Motion (No Air Resistance)',
    xaxis_title='Displacement in x-direction (m)',
    yaxis_title='Displacement in y-direction (m)',
    # This forces the x and y axes to have the same scale
    yaxis=dict(scaleanchor="x", scaleratio=1)
)

# Show the interactive plot
fig.show()