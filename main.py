from fastapi import FastAPI 
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="Choose Your Own Adventure Game API"
)