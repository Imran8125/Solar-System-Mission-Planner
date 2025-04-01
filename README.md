# Solar System Mission Planner

## Overview

The Solar System Mission Planner is an interactive Python application that visualizes planetary positions and calculates optimal interplanetary trajectories using Hohmann transfer orbits. This tool helps understand the basics of orbital mechanics and mission planning for space travel between planets.

![Solar System Visualization](screenshots/solar_system.png)

## Features

- **Accurate Planet Visualization**: Displays the current positions of all planets in the solar system
- **Interactive Mission Planning**: Select any planet as a destination to see the optimal trajectory from Earth
- **Launch Window Calculation**: Determines the best time to launch for fuel efficiency
- **Travel Time Estimation**: Calculates mission duration based on orbital mechanics
- **Arrival Prediction**: Shows where the target planet will be when the spacecraft arrives

## Requirements

- Python 3.x
- NumPy
- Matplotlib

## Installation

1. Clone this repository:
```bash
git clone https://github.com/yourusername/solar-system-mission-planner.git
cd solar-system-mission-planner
```

2. Install the required dependencies:
```bash
pip install -r requirements.txt
```

## Usage

Run the application:
```bash
python main.py
```

When prompted, enter the name of your target planet (or press Enter to view the solar system without mission planning):

```
Solar System Mission Planner
Available planets: Mercury, Venus, Mars, Jupiter, Saturn, Uranus, Neptune
Enter target planet (or press Enter to skip mission planning): Mars
Generating Solar System visualization...
```

## How It Works

The application uses simplified orbital mechanics to calculate transfer orbits:

1. **Planet Positions**: Calculates the current positions of planets based on orbital periods and semi-major axes
2. **Hohmann Transfer**: Implements the efficient Hohmann transfer orbit algorithm for minimum energy trajectories
3. **Launch Window**: Determines the optimal phase angle between Earth and the target planet for departure
4. **Travel Time**: Calculates the time of flight along the transfer ellipse

## Technical Details

- Planet positions are calculated using approximate orbital elements and periods
- The visualization assumes circular orbits for simplicity
- Hohmann transfer orbits are displayed as ellipses connecting Earth's orbit to the target planet's orbit
- The application calculates approximate launch dates and arrival times based on current planetary positions

## Limitations

- Uses simplified circular orbits rather than actual elliptical paths
- Does not account for orbital inclinations (2D visualization)
- Approximates orbital mechanics without planetary perturbations
- Currently optimized for transfers to outer planets (Mars and beyond)

## Future Enhancements

- Add support for inner planet transfers (Venus and Mercury)
- Implement 3D visualization with orbital inclinations
- Add animation to show spacecraft trajectory over time
- Include more accurate planetary ephemeris
- Support for more complex mission types (gravity assists)

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Based on fundamental principles of orbital mechanics and Hohmann transfer orbits
- Planet data from NASA/JPL planetary fact sheets

---

Created by [Your Name] - April 2025
```

You can replace "[Your Name]" with your actual name and update any other details as needed. You might also want to create a "screenshots" folder and add a screenshot of the application in action when you have one available.

Remember to create a LICENSE file if you're using the MIT license or another open-source license for your project.# filepath: f:\Projects2025\Python\PlanetsPositions\README.md
# Solar System Mission Planner

## Overview

The Solar System Mission Planner is an interactive Python application that visualizes planetary positions and calculates optimal interplanetary trajectories using Hohmann transfer orbits. This tool helps understand the basics of orbital mechanics and mission planning for space travel between planets.

![Solar System Visualization](screenshots/solar_system.png)

## Features

- **Accurate Planet Visualization**: Displays the current positions of all planets in the solar system
- **Interactive Mission Planning**: Select any planet as a destination to see the optimal trajectory from Earth
- **Launch Window Calculation**: Determines the best time to launch for fuel efficiency
- **Travel Time Estimation**: Calculates mission duration based on orbital mechanics
- **Arrival Prediction**: Shows where the target planet will be when the spacecraft arrives

## Requirements

- Python 3.x
- NumPy
- Matplotlib

## Installation

1. Clone this repository:
```bash
git clone https://github.com/yourusername/solar-system-mission-planner.git
cd solar-system-mission-planner
```

2. Install the required dependencies:
```bash
pip install -r requirements.txt
```

## Usage

Run the application:
```bash
python main.py
```

When prompted, enter the name of your target planet (or press Enter to view the solar system without mission planning):

```
Solar System Mission Planner
Available planets: Mercury, Venus, Mars, Jupiter, Saturn, Uranus, Neptune
Enter target planet (or press Enter to skip mission planning): Mars
Generating Solar System visualization...
```

## How It Works

The application uses simplified orbital mechanics to calculate transfer orbits:

1. **Planet Positions**: Calculates the current positions of planets based on orbital periods and semi-major axes
2. **Hohmann Transfer**: Implements the efficient Hohmann transfer orbit algorithm for minimum energy trajectories
3. **Launch Window**: Determines the optimal phase angle between Earth and the target planet for departure
4. **Travel Time**: Calculates the time of flight along the transfer ellipse

## Technical Details

- Planet positions are calculated using approximate orbital elements and periods
- The visualization assumes circular orbits for simplicity
- Hohmann transfer orbits are displayed as ellipses connecting Earth's orbit to the target planet's orbit
- The application calculates approximate launch dates and arrival times based on current planetary positions

---

Created by [Your Name] - April 2025

