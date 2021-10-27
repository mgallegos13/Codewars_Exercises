class Calculator:
    @staticmethod
    def average(*args):
        if not args:
            return 0
        else:
            return sum(args) / len(args)
