class Processor:
    def __init__(self, name, count):
        self.name = name
        self.count = count

    def process_input(self):
        print("I am processing input")


intel_processor = Processor("Intel", 4)


class Computer:
    def __init__(self, computer_name, processor):
        self.computer_name = computer_name
        self.abc = processor

    def process(self):
        self.abc.process_input()

    def another_level(self):
        self.process()


computer = Computer("my computer", intel_processor)
computer.another_level()
