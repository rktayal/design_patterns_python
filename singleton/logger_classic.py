import datetime


class Logger(object):
    log_file = None

    @staticmethod
    def instance():
        if '_instance' not in Logger.__dict__:
            Logger._instance = Logger()
        return Logger._instance

    def open_log(self, path):
        if self.log_file is None:
            self.log_file = open(path, mode='w')

    def write_log(self, log_record):
        now = str(datetime.datetime.now())
        record = '%s: %s' % (now, log_record)
        self.log_file.writelines(record)

    def close_log(self):
        self.log_file.close()


logger = Logger()
logger.open_log('my.log')
logger.write_log('Logging with Classic Singleton pattern')
logger.close_log()

with open('my.log', 'r') as f:
    for line in f:
        print(line)
