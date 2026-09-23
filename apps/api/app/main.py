from fastapi import FastAPI

app = FastAPI(
    title="T.R.A.C.E. API",
    description="Timetable • Records • Attendance • Campus Experience",
    version="0.1.0",
)


@app.get("/api/v1/health", tags=["System"])
async def health_check() -> dict[str, str]:
    return {
        "status": "ok",
        "service": "trace-api",
    }
