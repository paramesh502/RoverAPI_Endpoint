# Rover API - Camera & Documentation System

## Overview
Rover API provides camera screenshot capture with metadata, waypoint management, and automated report generation with route analysis.

## Features

### Camera Screenshot Capture
- Save screenshots with comprehensive metadata
- GPS coordinates, altitude, heading, speed tracking
- Environmental data (temperature, humidity)
- Rover status monitoring (battery, mission ID)
- Camera settings recording
- File size tracking

### Waypoint Management
- Manual waypoint creation with categories
- Automatic waypoint generation
- Waypoint categorization (general, auto, checkpoint, landmark)
- Mission-based organization

### Report Generation
- Interactive HTML reports with modern styling
- Route analysis and statistics
- Interactive maps with color-coded routes
- Battery consumption analysis
- Environmental condition tracking
- PDF export capability

## API Endpoints

### Camera Operations

#### POST `/api/camera/capture`
Capture a screenshot with metadata.

**Parameters:**
- `image` (file): Image file to save
- `latitude` (float): GPS latitude
- `longitude` (float): GPS longitude
- `altitude` (float, optional): Altitude in meters
- `heading` (float, optional): Compass heading in degrees
- `speed` (float, optional): Speed in m/s
- `battery_level` (float, optional): Battery percentage (0-100)
- `temperature` (float, optional): Temperature in Celsius
- `humidity` (float, optional): Humidity percentage (0-100)
- `note` (string, optional): Additional notes
- `mission_id` (string, optional): Mission identifier
- `rover_id` (string, optional): Rover identifier
- `camera_settings` (JSON string, optional): Camera settings
- `tags` (string, optional): Comma-separated tags

**Example:**
```bash
curl -X POST http://localhost:5000/api/camera/capture \
  -F "image=@screenshot.jpg" \
  -F "latitude=37.7749" \
  -F "longitude=-122.4194" \
  -F "altitude=100.5" \
  -F "heading=45.0" \
  -F "speed=2.5" \
  -F "battery_level=85.0" \
  -F "temperature=22.5" \
  -F "humidity=60.0" \
  -F "note=Checkpoint reached" \
  -F "mission_id=mission_001" \
  -F "rover_id=rover_001" \
  -F "tags=checkpoint,important"
```

#### GET `/api/camera/metadata`
Retrieve image metadata.

**Parameters:**
- `mission_id` (string, optional): Filter by mission ID

### Waypoint Operations

#### POST `/api/camera/waypoint`
Add a waypoint with coordinates.

**Parameters:**
- `name` (string, required): Waypoint name
- `latitude` (float, required): GPS latitude
- `longitude` (float, required): GPS longitude
- `altitude` (float, optional): Altitude in meters
- `category` (string, optional): Waypoint category (general, checkpoint, landmark)
- `description` (string, optional): Waypoint description
- `mission_id` (string, optional): Mission identifier
- `rover_id` (string, optional): Rover identifier

**Example:**
```bash
curl -X POST http://localhost:5000/api/camera/waypoint \
  -F "name=Base Camp" \
  -F "latitude=37.7749" \
  -F "longitude=-122.4194" \
  -F "altitude=100.0" \
  -F "category=checkpoint" \
  -F "description=Starting point of mission" \
  -F "mission_id=mission_001"
```

#### POST `/api/camera/waypoint/auto`
Auto-add waypoint at current position.

**Parameters:**
- `latitude` (float, required): GPS latitude
- `longitude` (float, required): GPS longitude
- `altitude` (float, optional): Altitude in meters
- `mission_id` (string, optional): Mission identifier
- `rover_id` (string, optional): Rover identifier

#### GET `/api/camera/waypoints`
Retrieve waypoints.

**Parameters:**
- `mission_id` (string, optional): Filter by mission ID

### Report Operations

#### POST `/api/report/generate_report`
Generate mission report.

**Parameters:**
- `mission_id` (string, optional): Generate report for specific mission

**Response includes:**
- HTML report file path
- PDF report file path (if available)
- Route analysis statistics
- Interactive map

#### GET `/api/report/export_data`
Export mission data in JSON or CSV format.

**Parameters:**
- `mission_id` (string, optional): Export specific mission data
- `format` (string, optional): Export format (json, csv)

#### GET `/api/report/reports`
List generated reports.

#### GET `/api/report/download/<filename>`
Download report file.

#### GET `/api/report/route_analysis`
Get route analysis.

**Parameters:**
- `mission_id` (string, optional): Analyze specific mission

## Data Structure

### Image Metadata
```json
{
  "file": "20250920_150513_screenshot.jpg",
  "timestamp": "20250920_150513",
  "datetime_iso": "2025-09-20T15:05:13.123456",
  "location": {
    "latitude": 37.7749,
    "longitude": -122.4194,
    "altitude": 100.5,
    "heading": 45.0
  },
  "motion": {
    "speed": 2.5,
    "heading": 45.0
  },
  "environment": {
    "temperature": 22.5,
    "humidity": 60.0
  },
  "rover_status": {
    "battery_level": 85.0,
    "rover_id": "rover_001",
    "mission_id": "mission_001"
  },
  "camera": {
    "settings": {},
    "file_size_bytes": 2048576
  },
  "note": "Checkpoint reached",
  "tags": ["checkpoint", "important"]
}
```

### Waypoint Data
```json
{
  "name": "Base Camp",
  "location": {
    "latitude": 37.7749,
    "longitude": -122.4194,
    "altitude": 100.0
  },
  "category": "checkpoint",
  "description": "Starting point of mission",
  "mission_id": "mission_001",
  "rover_id": "rover_001",
  "auto_generated": false,
  "timestamp": "2025-09-20T15:05:13.123456",
  "timestamp_readable": "2025-09-20 15:05:13 UTC",
  "waypoint_id": "wp_001"
}
```

## Route Analysis Features

### Distance Calculation
- Haversine formula for accurate distance calculation
- Total distance traveled
- Distance between waypoints

### Speed Analysis
- Average speed calculation
- Maximum and minimum speeds
- Speed-based route color coding

### Battery Analysis
- Initial and final battery levels
- Battery consumption tracking
- Battery level color coding in reports

### Environmental Analysis
- Temperature range and averages
- Humidity monitoring
- Environmental condition tracking

## Report Features

### Interactive Maps
- Folium-based interactive maps
- Color-coded waypoints by category
- Speed-based route color coding
- Popup information for waypoints

### Modern HTML Reports
- Responsive design with modern CSS
- Statistics cards and grids
- Comprehensive metadata display
- Professional styling

### PDF Export
- Optional PDF generation (requires pdfkit and wkhtmltopdf)
- Full report export capability

## Installation & Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. For PDF export, install wkhtmltopdf:
```bash
# Ubuntu/Debian
sudo apt-get install wkhtmltopdf

# macOS
brew install wkhtmltopdf

# Windows
# Download from https://wkhtmltopdf.org/downloads.html
```

3. Run the application:
```bash
python main.py
```

## Usage Examples

### Complete Mission Workflow

1. **Start Mission:**
```bash
curl -X POST http://localhost:5000/api/camera/waypoint \
  -F "name=Mission Start" \
  -F "latitude=37.7749" \
  -F "longitude=-122.4194" \
  -F "category=checkpoint" \
  -F "mission_id=exploration_001"
```

2. **Capture Screenshots:**
```bash
curl -X POST http://localhost:5000/api/camera/capture \
  -F "image=@screenshot1.jpg" \
  -F "latitude=37.7849" \
  -F "longitude=-122.4094" \
  -F "mission_id=exploration_001" \
  -F "note=First checkpoint reached"
```

3. **Auto-add Waypoints:**
```bash
curl -X POST http://localhost:5000/api/camera/waypoint/auto \
  -F "latitude=37.7949" \
  -F "longitude=-122.3994" \
  -F "mission_id=exploration_001"
```

4. **Generate Report:**
```bash
curl -X POST http://localhost:5000/api/report/generate_report \
  -F "mission_id=exploration_001"
```

5. **Export Data:**
```bash
curl "http://localhost:5000/api/report/export_data?mission_id=exploration_001&format=json"
```

## File Storage

- **Images:** `storage/images/`
- **Reports:** `storage/reports/`
- **Metadata:** `storage/metadata.json`
- **Waypoints:** `storage/waypoints.json`

## Error Handling

All endpoints return appropriate HTTP status codes:
- `200`: Success
- `400`: Bad Request (invalid parameters)
- `404`: Not Found (file/report not found)
- `500`: Internal Server Error

Error responses include descriptive error messages:
```json
{
  "error": "Invalid latitude or longitude"
}
```

## Performance Considerations

- Image files are stored with timestamps for easy organization
- Metadata is stored in JSON format for fast access
- Route calculations use efficient algorithms
- Reports are generated on-demand to save storage space

## Security Notes

- File uploads are validated and sanitized
- JSON data is properly escaped
- File paths are secured against directory traversal
- Input validation prevents injection attacks
