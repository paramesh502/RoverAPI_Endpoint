# Rover API - Mission Data Capture and Report Generation

A comprehensive Flask-based API system for rover mission data capture, analysis, and report generation.

## Features

### 1. Camera Data Capture
- Screenshot capture with comprehensive metadata
- GPS coordinates, altitude, and heading tracking
- Battery level and environmental monitoring
- Motion data (speed, direction)
- Mission and rover ID tracking

### 2. Mission Documentation
- Route analysis with distance and speed calculations
- PDF report generation with embedded images
- Interactive HTML maps with waypoints
- Waypoint management with coordinates
- Data export in JSON format

## Quick Start

### Installation
```bash
pip install -r requirements.txt
```

### Usage

#### Start the API Server
```bash
python main.py
```
Server runs on `http://localhost:8080`

#### Capture Rover Data
```bash
python capture_rover_data.py
```

#### Generate Mission Report
```bash
python generate_mission_report.py
```

## API Endpoints

- `POST /api/camera/capture` - Capture image with metadata
- `POST /api/camera/waypoint` - Add waypoint
- `POST /api/camera/waypoint/auto` - Auto-add waypoint
- `GET /api/camera/waypoints` - Get all waypoints
- `GET /api/camera/metadata` - Get all metadata
- `POST /api/report/generate_report` - Generate mission report
- `GET /api/report/export_data` - Export mission data
- `GET /api/report/route_analysis` - Get route statistics

## Project Structure

```
RoverAPI_Endpoint-master/
├── main.py                    # Flask server entry point
├── capture_rover_data.py      # Data capture script
├── generate_mission_report.py # Report generation script
├── test_api.py               # API testing script
├── requirements.txt          # Dependencies
├── app/
│   ├── api/
│   │   ├── camera.py         # Camera capture endpoints
│   │   ├── report.py         # Report generation
│   │   └── root.py          # Health check
│   └── py_types.py          # Type definitions
└── storage/
    ├── images/              # Captured images
    └── reports/             # Generated reports
```

## Dependencies

- Flask >= 3.1.1
- Folium >= 0.20.0
- ReportLab >= 4.0.0
- Pillow >= 10.0.0
- Werkzeug >= 3.0.0

## License

MIT License