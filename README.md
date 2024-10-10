# Space Station Tracker

A simple Python application that tracks the International Space Station (ISS) in real-time, displaying its current coordinates and the distance between your location and the ISS. This application uses APIs to fetch real-time data and presents it in a graphical user interface (GUI) built with Tkinter.

## Features

- Fetch the real-time latitude and longitude of the ISS.
- Calculate the distance from your current location to the ISS using your IP address.
- Display the information in a visually appealing GUI with a background image of the ISS.

## Installation

### Prerequisites
- Python 3.x
- Required Python packages:
  - `requests`
  - `geopy`
  - `geocoder`
  - `Pillow`
  - `tkinter`

You can install the required packages using pip:

```bash
pip install requests geopy geocoder Pillow
```

### Clone the repository
```bash
git clone https://github.com/your-username/space-station-tracker.git
cd space-station-tracker
```

### Usage

1. **Download the ISS image**  
   Place an image named `iss.jpg` in the root directory of the project or update the image path in the code if necessary.

2. **Run the application**  
   After ensuring all dependencies are installed, you can run the program with:

```bash
python space_station_tracker.py
```

3. **GUI Interface**  
   The application opens a window with a button labeled **Calculate Information**. Once clicked, it will display:
   - The real-time coordinates of the ISS.
   - The distance from your current location (determined by your IP) to the ISS in kilometers.

## Code Overview

### Backend
- The backend consists of two primary functions:
  - `iss_coords()`: Fetches the current latitude and longitude of the ISS from the Open Notify API.
  - `dist_to_iss()`: Calculates the ground distance between the user's location and the ISS using geolocation.

### Frontend
- A Tkinter-based GUI is used for displaying the ISS image and the data calculated by the backend.
- The main window includes a background image of the ISS, a title label, and a button to trigger the calculations.

## Libraries Used
- **Requests**: For making API calls to fetch ISS location data.
- **Geopy**: For calculating distances between geographic coordinates.
- **Geocoder**: For determining the user's location based on their IP address.
- **Tkinter**: For building the graphical user interface.
- **Pillow**: For handling image display within the GUI.

## Future Improvements
- Add real-time ISS tracking with periodic updates.
- Implement additional features like displaying a world map with the ISS location.
- Enhance the GUI with more interactive elements.
