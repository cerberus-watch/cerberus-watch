from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pydantic import BaseModel
from typing import Optional
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Mount the shared assets directory to serve CSS, JS, etc.
app.mount("/assets", StaticFiles(directory="assets"), name="assets")

@app.get("/")
async def read_index():
    # This is the main UI for the Athena service
    return FileResponse('heads/athena/athena.html')

@app.get("/dashboard")
async def read_dashboard():
    # Serve the main project dashboard
    return FileResponse('index.html')

# CORS middleware for local development
origins = ["http://127.0.0.1:8000"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class AnalysisInput(BaseModel):
    name: Optional[str] = None

class AthenaAnalyzer:
    def __init__(self, analysis_input: AnalysisInput):
        self.input = analysis_input
        self.search_name = self.input.name.lower() if self.input.name else None
        self.mock_profiles = {
            "john doe": {
                "status": "verified",
                "verified_on": ["LinkedIn", "Twitter"],
                "background_summary": "Public profiles show a consistent work history. No public posts with aggressive language were found."
            },
            "jane smith": {
                "status": "partially_verified",
                "verified_on": ["Facebook"],
                "background_summary": "A single public profile was found. The profile is new with limited activity."
            },
        }

    def verify_identity(self):
        if not self.search_name:
            return {"status": "unverified", "message": "A name is required for identity verification."}
        profile = self.mock_profiles.get(self.search_name)
        if profile:
            message = f"Identity {profile['status']} for {self.input.name}. Profiles found on: {', '.join(profile['verified_on'])}."
            return {"status": profile['status'], "message": message}
        return {"status": "unverified", "message": f"Could not verify identity for {self.input.name}."}

    def gather_background_info(self):
        profile = self.mock_profiles.get(self.search_name)
        return {"background_info": profile["background_summary"] if profile else "No background information found."}

    def analyze_risk(self, background_info):
        if "consistent work history" in background_info and "no public posts" in background_info.lower():
            score = "Good"
            summary = "Individual has a verifiable public presence with no identifiable risk factors."
        elif "limited activity" in background_info:
            score = "Review Recommended"
            summary = "Limited online presence makes a comprehensive assessment difficult. Caution is advised."
        else:
            score = "Caution Advised"
            summary = "Could not form a comprehensive safety assessment."
        return {"safety_score": score, "summary": summary}

@app.post("/analyze")
async def analyze(analysis_input: AnalysisInput):
    analyzer = AthenaAnalyzer(analysis_input)
    identity_result = analyzer.verify_identity()
    if identity_result["status"] == "unverified":
        return {"safety_score": "Verification Failed", "summary": identity_result["message"]}

    background_info = analyzer.gather_background_info()
    risk_analysis_result = analyzer.analyze_risk(background_info["background_info"])

    final_summary = (
        f"{identity_result['message']}<br><br>"
        f"{background_info['background_info']}<br><br>"
        f"<b>Risk Analysis:</b> {risk_analysis_result['summary']}"
    )

    return {"safety_score": risk_analysis_result["safety_score"], "summary": final_summary}
