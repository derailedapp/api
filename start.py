import multiprocessing

from discoursy.app import app

if __name__ == '__main__':
    app.run(workers=multiprocessing.cpu_count(), backlog=1000)
