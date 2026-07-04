import multiprocessing
import os

bind = "0.0.0.0:5000"

workers = multiprocessing.cpu_count() * 2 + 1

threads = 2

timeout = 120

worker_class = "gthread"

accesslog = "-"

errorlog = "-"

loglevel = "info"

keepalive = 5

preload_app = True

max_requests = 1000

max_requests_jitter = 50