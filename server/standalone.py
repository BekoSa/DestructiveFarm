import threading
import werkzeug.serving


from server import app, database
from server.models import FlagStatus
from server.huey_config import huey
from server.submit_loop import run_loop

with app.app_context():
    db = database.get(context_bound=False)

if db.execute("SELECT COUNT(*) FROM flags WHERE status = ?", (FlagStatus.QUEUED.name,)).fetchone()[0] > 0:
    run_loop()
