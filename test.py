from fastapi import FastAPI
app = FastAPI()

@app.route('/')
def index():
  return {"message":"heello from onwords fastapi"}
