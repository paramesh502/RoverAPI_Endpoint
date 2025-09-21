# Rover API Documentation

A comprehensive API system for rover mission data capture, analysis, and report generation. This system helps you track your rover's journey, capture important moments, and generate detailed mission reports.

## What This API Does

This API is designed for rover missions where you need to:
- Capture screenshots of what your rover sees
- Track where your rover goes and what it does
- Generate professional reports of the entire mission
- Keep detailed records of important locations and events

## Core Features

### Camera Data Capture
Capture screenshots from your rover's camera along with all the important information about that moment:
- Where the rover was (GPS coordinates, altitude, direction)
- How the rover was moving (speed, heading)
- What the environment was like (temperature, humidity)
- How much battery the rover had left
- Which mission this was part of

### Mission Documentation
Create comprehensive reports that include:
- The complete route your rover traveled
- All the photos taken during the mission
- Interactive maps showing the rover's path
- Analysis of battery usage and environmental conditions
- Professional PDF reports for presentations

### Waypoint Management
Mark important locations during your mission:
- Add waypoints manually when you find something interesting
- Let the system automatically add waypoints at regular intervals
- Categorize waypoints (checkpoints, landmarks, hazards)
- Keep track of all locations with GPS coordinates

## How to Use the API

### Starting the Server
First, start the API server:
```bash
python main.py
```
The server will run on `http://localhost:8080`

### Quick Commands
For easy use, we provide two simple commands:

**Capture rover data:**
```bash
python capture_rover_data.py
```

**Generate mission report:**
```bash
python generate_mission_report.py
```

## API Endpoints

### Camera Operations

#### Capture Screenshot
**POST** `/api/camera/capture`

Take a screenshot and save it with all the rover's data.

**What you need to send:**
- `image` (file): The photo from your rover's camera
- `latitude` (number): Where you are (GPS latitude)
- `longitude` (number): Where you are (GPS longitude)
- `altitude` (number, optional): How high up you are in meters
- `heading` (number, optional): Which direction you're facing (0-360 degrees)
- `speed` (number, optional): How fast you're moving in meters per second
- `battery_level` (number, optional): How much battery is left (0-100%)
- `temperature` (number, optional): Temperature in Celsius
- `humidity` (number, optional): Humidity percentage (0-100%)
- `note` (text, optional): Any notes about this moment
- `mission_id` (text, optional): Which mission this is part of
- `rover_id` (text, optional): Which rover this is

**What you get back:**
```json
{
  "status": "ok",
  "saved": "20250921_091616_rover_capture.jpg",
  "metadata": {
    "file": "20250921_091616_rover_capture.jpg",
    "timestamp": "20250921_091616",
    "location": {
      "latitude": 37.7749,
      "longitude": -122.4194,
      "altitude": 100.5,
      "heading": 45.0
    },
    "rover_status": {
      "battery_level": 85.0,
      "rover_id": "rover_001",
      "mission_id": "mission_001"
    }
  },
  "file_size_mb": 0.06
}
```

#### Add Waypoint
**POST** `/api/camera/waypoint`

Mark an important location during your mission.

**What you need to send:**
- `name` (text): What to call this waypoint
- `latitude` (number): GPS latitude
- `longitude` (number): GPS longitude
- `altitude` (number, optional): Altitude in meters
- `category` (text, optional): Type of waypoint (checkpoint, landmark, hazard)
- `description` (text, optional): What's special about this location
- `mission_id` (text, optional): Which mission this belongs to
- `rover_id` (text, optional): Which rover found this

**What you get back:**
```json
{
  "status": "ok",
  "waypoint_id": "wp_001",
  "waypoint": {
    "name": "Base Station",
    "location": {
      "latitude": 37.7749,
      "longitude": -122.4194,
      "altitude": 100.0
    },
    "category": "checkpoint",
    "description": "Mission starting point",
    "mission_id": "mission_001",
    "waypoint_id": "wp_001"
  }
}
```

#### Auto-Add Waypoint
**POST** `/api/camera/waypoint/auto`

Let the system automatically add a waypoint based on current location.

**What you need to send:**
- `latitude` (number): Current GPS latitude
- `longitude` (number): Current GPS longitude
- `altitude` (number, optional): Current altitude
- `mission_id` (text, optional): Current mission
- `rover_id` (text, optional): Current rover

### Data Retrieval

#### Get All Waypoints
**GET** `/api/camera/waypoints`

Get a list of all waypoints for a mission.

**Optional parameters:**
- `mission_id` (text): Filter by mission

#### Get All Metadata
**GET** `/api/camera/metadata`

Get all captured images and their data.

**Optional parameters:**
- `mission_id` (text): Filter by mission

### Report Generation

#### Generate Mission Report
**POST** `/api/report/generate_report`

Create a complete mission report with all data.

**What you need to send:**
- `mission_id` (text, optional): Which mission to report on

**What you get back:**
```json
{
  "status": "ok",
  "report_html": "storage/reports/report_20250921_091623.html",
  "report_pdf": "storage/reports/report_20250921_091623.pdf",
  "map_html": "storage/reports/map_20250921_091623.html",
  "route_analysis": {
    "total_distance_km": 2.5,
    "average_speed": 1.2,
    "total_time": 1800,
    "battery_consumed": 15.0
  }
}
```

#### Export Mission Data
**GET** `/api/report/export_data`

Download all mission data in JSON format.

**Optional parameters:**
- `mission_id` (text): Which mission to export
- `format` (text): Export format (json, csv)

#### Get Route Analysis
**GET** `/api/report/route_analysis`

Get detailed analysis of the rover's route.

**Optional parameters:**
- `mission_id` (text): Which mission to analyze

## Example Usage

### Using curl to capture data:
```bash
curl -X POST http://localhost:8080/api/camera/capture \
  -F "image=@rover_photo.jpg" \
  -F "latitude=37.7749" \
  -F "longitude=-122.4194" \
  -F "altitude=100.5" \
  -F "battery_level=85.0" \
  -F "temperature=22.0" \
  -F "mission_id=rover_challenge_001"
```

### Using curl to add a waypoint:
```bash
curl -X POST http://localhost:8080/api/camera/waypoint \
  -F "name=Checkpoint Alpha" \
  -F "latitude=37.7759" \
  -F "longitude=-122.4184" \
  -F "altitude=105.0" \
  -F "category=checkpoint" \
  -F "description=First major waypoint" \
  -F "mission_id=rover_challenge_001"
```

### Using curl to generate a report:
```bash
curl -X POST http://localhost:8080/api/report/generate_report \
  -F "mission_id=rover_challenge_001"
```

## File Structure

The API creates and manages these files:
- `storage/images/` - All captured rover photos
- `storage/reports/` - Generated HTML and PDF reports
- `storage/metadata.json` - Database of all captured data
- `storage/waypoints.json` - Database of all waypoints

## Error Handling

The API returns helpful error messages when something goes wrong:

```json
{
  "status": "error",
  "message": "Missing required parameter: latitude"
}
```

Common error scenarios:
- Missing required parameters
- Invalid file uploads
- GPS coordinates out of range
- File system errors
- Missing dependencies for PDF generation

## Requirements

Make sure you have these installed:
- Python 3.7 or higher
- Flask
- ReportLab (for PDF generation)
- Pillow (for image processing)
- Folium (for map generation)

Install everything with:
```bash
pip install -r requirements.txt
```

## Support

If you run into issues:
1. Check that all required parameters are provided
2. Make sure the server is running on port 8080
3. Verify that storage directories exist and are writable
4. Check the server logs for detailed error messages

This API is designed to be simple to use while providing powerful mission documentation capabilities for your rover projects.