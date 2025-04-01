import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as mpatches
from datetime import datetime, timedelta
import matplotlib.animation as animation

def calculate_hohmann_transfer(source_radius, target_radius):
    """Calculate parameters for a Hohmann transfer orbit"""
    # Transfer orbit semi-major axis
    a_transfer = (source_radius + target_radius) / 2
    
    # Velocity needed to enter transfer orbit from source
    v_departure = np.sqrt(2 * target_radius / (source_radius + target_radius) * source_radius)
    
    # Time of flight (half the orbital period of the transfer ellipse)
    tof = np.pi * np.sqrt(a_transfer**3)  # in units where G*M_sun = 1
    
    # Convert to Earth days (rough approximation)
    tof_days = tof * 365.25 / (2 * np.pi)
    
    return a_transfer, v_departure, tof_days

def plot_solar_system(target_planet=None):
    # Set up the figure with dark gray background 
    fig, ax = plt.subplots(figsize=(12, 10), facecolor='gray')
    ax.set_facecolor('lightgray')  # Set the actual plot area to light gray
    
    # Define the planets and their orbital characteristics (semi-major axis in AU)
    planets = {
        'Mercury': {'a': 0.387, 'color': 'gray', 'size': 5},
        'Venus': {'a': 0.723, 'color': 'darkorange', 'size': 5},
        'Earth': {'a': 1.0, 'color': 'blue', 'size': 5},
        'Mars': {'a': 1.524, 'color': 'red', 'size': 5},
        'Jupiter': {'a': 5.203, 'color': 'brown', 'size': 8},
        'Saturn': {'a': 9.582, 'color': 'gold', 'size': 8},
        'Uranus': {'a': 19.201, 'color': 'lightblue', 'size': 5},
        'Neptune': {'a': 30.047, 'color': 'darkblue', 'size': 5},
    }
    
    # Define approximate orbital periods (in Earth years)
    orbital_periods = {
        'Mercury': 0.24,
        'Venus': 0.62,
        'Earth': 1.0,
        'Mars': 1.88,
        'Jupiter': 11.86,
        'Saturn': 29.46,
        'Uranus': 84.01,
        'Neptune': 164.8,
    }
    
    # Get the current time as fraction of a year (for simple orbital calculation)
    current_day = datetime.now().timetuple().tm_yday
    year_fraction = current_day / 365.25
    
    # Plot the Sun at the center
    ax.plot(0, 0, 'yo', markersize=15, label='Sun')
    
    # Calculate and plot planet positions
    max_dist = 0
    planet_positions = {}
    
    for name, properties in planets.items():
        a = properties['a']
        color = properties['color']
        size = properties['size']
        
        # Simple orbital angle calculation (assuming circular orbits and Jan 1, 2000 as reference)
        period = orbital_periods[name]
        # Offset angles to better approximate real positions
        if name == 'Mercury': offset = 0.1
        elif name == 'Venus': offset = 2.5
        elif name == 'Earth': offset = 1.0
        elif name == 'Mars': offset = 0.5
        elif name == 'Jupiter': offset = 3.2
        elif name == 'Saturn': offset = 4.8
        elif name == 'Uranus': offset = 0.7
        else: offset = 1.2
        
        angle = (year_fraction / period * 2 * np.pi + offset) % (2 * np.pi)
        
        # Calculate x and y coordinates
        x = a * np.cos(angle)
        y = a * np.sin(angle)
        
        # Store planet position
        planet_positions[name] = {'x': x, 'y': y, 'a': a, 'angle': angle, 'period': period}
        
        max_dist = max(max_dist, a)
        
        # Draw orbit circle
        orbit = plt.Circle((0, 0), a, fill=False, linestyle='--', alpha=0.3, color='white')
        ax.add_patch(orbit)
        
        # Plot the planet
        ax.plot(x, y, 'o', color=color, markersize=size)
        ax.text(x, y, name, fontsize=8, color='white')
    
    # If a target planet is specified, calculate and draw the Hohmann transfer orbit
    if target_planet and target_planet in planets and target_planet != 'Earth':
        source_radius = planets['Earth']['a']
        target_radius = planets[target_planet]['a']
        
        # Get Earth and target planet positions
        earth_pos = planet_positions['Earth']
        target_pos = planet_positions[target_planet]
        
        # Calculate Hohmann transfer parameters
        a_transfer, v_departure, tof_days = calculate_hohmann_transfer(source_radius, target_radius)
        
        # Calculate optimal launch angle (180 degrees ahead/behind target depending on inner/outer planet)
        if target_radius > source_radius:  # Outer planet
            # We need to launch when the target is angle_diff ahead of Earth
            angle_diff = np.pi * (1 - np.sqrt((source_radius + target_radius)**3 / (8 * target_radius**3)))
            optimal_earth_angle = (target_pos['angle'] - angle_diff) % (2 * np.pi)
            
            # Calculate days until optimal launch window
            current_angle = earth_pos['angle']
            angle_to_travel = (optimal_earth_angle - current_angle) % (2 * np.pi)
            days_to_launch = angle_to_travel / (2 * np.pi) * 365.25
            
            # Draw the transfer orbit (semi-ellipse)
            ellipse = mpatches.Ellipse((0, 0), 2*a_transfer, 2*a_transfer*np.sqrt(1-(source_radius**2+target_radius**2)/(4*a_transfer**2)), 
                                      angle=np.degrees(optimal_earth_angle), fill=False, 
                                      color='lime', linestyle='-', alpha=0.7)
            ax.add_patch(ellipse)
            
            # Calculate future position of target at arrival
            target_arrival_angle = (target_pos['angle'] + (tof_days/365.25) * (2*np.pi/target_pos['period'])) % (2*np.pi)
            target_x_arrival = target_radius * np.cos(target_arrival_angle)
            target_y_arrival = target_radius * np.sin(target_arrival_angle)
            
            # Mark arrival point
            ax.plot(target_x_arrival, target_y_arrival, 'x', color='lime', markersize=10)
            
            # Add launch and arrival info to the plot
            launch_date = (datetime.now() + timedelta(days=days_to_launch)).strftime("%Y-%m-%d")
            arrival_date = (datetime.now() + timedelta(days=days_to_launch + tof_days)).strftime("%Y-%m-%d")
            
            info_text = f"Mission to {target_planet}:\n"
            info_text += f"Optimal launch: {launch_date}\n"
            info_text += f"Travel time: {tof_days:.1f} days\n"
            info_text += f"Arrival: {arrival_date}"
            
            # Place text in top left corner
            ax.text(0.02, 0.98, info_text, transform=ax.transAxes, fontsize=10,
                   verticalalignment='top', color='white', bbox=dict(facecolor='darkgray', alpha=0.7))
    
    # Set up the axis limits
    ax.set_xlim(-max_dist * 1.2, max_dist * 1.2)
    ax.set_ylim(-max_dist * 1.2, max_dist * 1.2)
    
    # Add labels and title with white text for better visibility on gray background
    ax.set_xlabel('X (AU)', color='white')
    ax.set_ylabel('Y (AU)', color='white')
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    title = f'Solar System Planet Positions\n{current_time}'
    if target_planet:
        title += f' - Mission Planning to {target_planet}'
    ax.set_title(title, color='white')
    
    # Equal aspect ratio ensures circles look like circles
    ax.set_aspect('equal')
    
    # Add a legend
    legend_elements = [mpatches.Patch(color=planet['color'], label=name) 
                      for name, planet in planets.items()]
    legend_elements.insert(0, mpatches.Patch(color='yellow', label='Sun'))
    if target_planet:
        legend_elements.append(mpatches.Patch(color='lime', label='Transfer Orbit'))
    
    legend = ax.legend(handles=legend_elements, loc='upper right')
    legend.get_frame().set_facecolor('darkgray')
    plt.setp(legend.get_texts(), color='white')
    
    # Add white grid for better visibility on gray background
    ax.grid(alpha=0.3, color='white')
    
    # Change tick color to white for visibility
    ax.tick_params(axis='both', colors='white')
    
    plt.tight_layout()
    plt.show()

def main():
    """Main function to select target planet and run visualization"""
    print("Solar System Mission Planner")
    print("Available planets: Mercury, Venus, Mars, Jupiter, Saturn, Uranus, Neptune")
    target = input("Enter target planet (or press Enter to skip mission planning): ").strip().title()
    
    if target and target not in ["Mercury", "Venus", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]:
        print(f"Invalid planet '{target}'. Showing regular solar system view.")
        target = None
    
    print("Generating Solar System visualization...")
    plot_solar_system(target)

if __name__ == "__main__":
    main()