from app.main import app
import ray
import uvicorn

ray.init(dashboard_host='localhost')
uvicorn.run(app, host="localhost", port=8080)
# load_dotenv()
# app.run(host="localhost", port=8080)
