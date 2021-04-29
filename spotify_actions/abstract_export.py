from tqdm import tqdm


class ExportAction:
    def __init__(self, sp, title):
        self.sp = sp
        self.pb = None
        self.batch = None
        self.title = title
        self.library = list()

    def do_action(self):
        pass

    def get_first_batch(self):
        pass

    def get_next_batch(self):
        self.batch = self.sp.next(self.batch)

    def run(self):
        self.get_first_batch()
        self.do_action()

    def make_progress_bar(self, total, title):
        self.pb = tqdm(
            total=total,
            desc=title
        )

    def update_progress_bar(self, count):
        self.pb.update(count)
