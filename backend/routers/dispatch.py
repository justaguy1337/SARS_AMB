from fastapi import APIRouter, HTTPException
from typing import Dict, Any

router = APIRouter()

@router.post("/")
async def dispatch_ambulance(dispatch_data: Dict[str, Any]) -> Dict[str, Any]:
    """
    Dispatch an ambulance to an emergency location
    
    Expected data:
    - ambulance_id: ID of the ambulance to dispatch
    - emergency_id: ID of the emergency
    - patient_info: Patient information
    - destination: Destination location
    """
    return {
        "success": True,
        "message": "Ambulance dispatched successfully",
        "dispatch_id": "DSP-001",
        "ambulance_id": dispatch_data.get("ambulance_id"),
        "emergency_id": dispatch_data.get("emergency_id"),
        "eta": "8 minutes"
    }

@router.get("/{dispatch_id}")
async def get_dispatch_status(dispatch_id: str) -> Dict[str, Any]:
    """Get status of a dispatch"""
    return {
        "dispatch_id": dispatch_id,
        "status": "en_route",
        "eta": "5 minutes",
        "current_location": {
            "latitude": 28.6139,
            "longitude": 77.2090
        }
    }
