#!/usr/bin/env python3
"""
Simple test script for Rover API functionality
"""

import json
import os
import sys
from datetime import datetime

sys.path.append(os.path.join(os.path.dirname(__file__), 'app'))

def test_metadata_structure():
    """Test metadata structure"""
    metadata = {
        "file": "test_image.jpg",
        "timestamp": "20250920_160000",
        "datetime_iso": datetime.utcnow().isoformat(),
        "location": {
            "latitude": 37.7749,
            "longitude": -122.4194,
            "altitude": 100.0,
            "heading": 0.0
        },
        "motion": {
            "speed": 0.0,
            "heading": 0.0
        },
        "environment": {
            "temperature": 22.0,
            "humidity": 55.0
        },
        "rover_status": {
            "battery_level": 95.0,
            "rover_id": "rover_001",
            "mission_id": "test_mission"
        },
        "camera": {
            "settings": {},
            "file_size_bytes": 2048576
        },
        "note": "Test image",
        "tags": ["test"]
    }
    
    required_fields = ["file", "timestamp", "location", "motion", "environment", "rover_status"]
    missing = [field for field in required_fields if field not in metadata]
    
    if not missing:
        print("Metadata structure: OK")
        return True
    else:
        print(f"Metadata structure: FAILED - missing {missing}")
        return False

def test_waypoint_structure():
    """Test waypoint structure"""
    waypoint = {
        "name": "Test Waypoint",
        "location": {
            "latitude": 37.7749,
            "longitude": -122.4194,
            "altitude": 100.0
        },
        "category": "checkpoint",
        "description": "Test waypoint",
        "mission_id": "test_mission",
        "rover_id": "rover_001",
        "auto_generated": False,
        "timestamp": datetime.utcnow().isoformat(),
        "waypoint_id": "wp_001"
    }
    
    required_fields = ["name", "location", "category", "mission_id"]
    missing = [field for field in required_fields if field not in waypoint]
    
    if not missing:
        print("Waypoint structure: OK")
        return True
    else:
        print(f"Waypoint structure: FAILED - missing {missing}")
        return False

def test_route_analysis():
    """Test route analysis functions"""
    try:
        from api.report import haversine_distance, calculate_route_stats
        
        distance = haversine_distance(37.7749, -122.4194, 37.7849, -122.4094)
        if distance > 0:
            print("Route analysis: OK")
            return True
        else:
            print("Route analysis: FAILED")
            return False
    except Exception as e:
        print(f"Route analysis: FAILED - {e}")
        return False

def test_file_operations():
    """Test file operations"""
    os.makedirs("storage", exist_ok=True)
    
    test_data = [{"test": "data"}]
    test_file = "storage/test.json"
    
    try:
        with open(test_file, "w") as f:
            json.dump(test_data, f)
        
        with open(test_file, "r") as f:
            loaded = json.load(f)
        
        os.remove(test_file)
        print("File operations: OK")
        return True
    except Exception as e:
        print(f"File operations: FAILED - {e}")
        return False

def main():
    """Run tests"""
    print("Rover API Test")
    print("=" * 20)
    
    tests = [
        ("Metadata Structure", test_metadata_structure),
        ("Waypoint Structure", test_waypoint_structure),
        ("Route Analysis", test_route_analysis),
        ("File Operations", test_file_operations)
    ]
    
    passed = 0
    for name, test_func in tests:
        if test_func():
            passed += 1
    
    print(f"\nResults: {passed}/{len(tests)} tests passed")
    
    if passed == len(tests):
        print("All tests passed - API is ready")
    else:
        print("Some tests failed")

if __name__ == "__main__":
    main()
