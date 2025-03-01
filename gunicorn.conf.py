port = 8000
bind = f"0.0.0.0:{port}"
workers = 8
# accesslog = "./log/access_log.log"
errorlog = "./log/error_log.log"
worker_class = "uvicorn.workers.UvicornWorker"
