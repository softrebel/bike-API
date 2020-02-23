from sanic import Sanic
from sanic.response import json
from dotenv import load_dotenv

app = Sanic()
load_dotenv(verbose=True)
from pathlib import Path
env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

@app.route("/")
async def test(request):
    return json({"hello": "world"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)