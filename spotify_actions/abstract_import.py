from tqdm import tqdm


class ImportAction:
    def __init__(self, sp, items, title):
        self.sp = sp
        self.pb = None
        self.items = items
        self.title = title

    def do_action(self):
        pass

    def run(self):
        self.make_progress_bar(len(self.items), self.title)
        self.do_action()
        self.pb.close()

    def make_progress_bar(self, total, title):
        self.pb = tqdm(
            total=total,
            desc=title
        )

    def update_progress_bar(self, count):
        self.pb.update(count)
