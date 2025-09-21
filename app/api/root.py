from flask import Blueprint, jsonify

bp = Blueprint("root", __name__)

@bp.route("/", methods=["GET"])
def root():
    return jsonify({
        "message": "Rover API is running",
        "version": "1.0.0",
        "endpoints": {
            "camera_capture": "/api/camera/capture",
            "add_waypoint": "/api/camera/waypoint",
            "generate_report": "/api/report/generate_report",
            "system_health": "/api/doctor",
            "logs": "/api/logs",
            "test": "/api/test"
        }
    })
