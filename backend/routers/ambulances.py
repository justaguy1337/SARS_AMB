from fastapi import APIRouter, HTTPException
from typing import List, Dict, Any

router = APIRouter()

# Mock ambulance data
mock_ambulances = [
    {
        "id": "AMB-001",
        "vehicle_number": "DL-01-AB-1234",
        "type": "Advanced Life Support",
        "status": "available",
        "current_location": {
            "latitude": 28.5672,
            "longitude": 77.2100,
            "address": "AIIMS Hospital, New Delhi"
        },
        "driver": {
            "name": "Rajesh Kumar",
            "phone": "+91-9876543210"
        },
        "equipment": ["Defibrillator", "Oxygen", "Stretcher"]
    },
    {
        "id": "AMB-002",
        "vehicle_number": "DL-01-CD-5678",
        "type": "Basic Life Support",
        "status": "available",
        "current_location": {
            "latitude": 28.6129,
            "longitude": 77.2295,
            "address": "India Gate Area"
        },
        "driver": {
            "name": "Suresh Yadav",
            "phone": "+91-9876543211"
        },
        "equipment": ["Oxygen", "Stretcher"]
    }
]

@router.get("/")
async def get_all_ambulances() -> List[Dict[str, Any]]:
    """Get all ambulances with their current status and location"""
    return mock_ambulances

@router.get("/{ambulance_id}")
async def get_ambulance(ambulance_id: str) -> Dict[str, Any]:
    """Get specific ambulance details"""
    ambulance = next((amb for amb in mock_ambulances if amb["id"] == ambulance_id), None)
    if not ambulance:
        raise HTTPException(status_code=404, detail="Ambulance not found")
    return ambulance

@router.put("/{ambulance_id}/status")
async def update_ambulance_status(ambulance_id: str, status: Dict[str, str]) -> Dict[str, Any]:
    """Update ambulance status"""
    return {
        "success": True,
        "message": f"Ambulance {ambulance_id} status updated",
        "ambulance_id": ambulance_id,
        "new_status": status.get("status")
    }
