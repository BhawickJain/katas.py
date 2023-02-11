import matplotlib.pyplot as plt  # type: ignore


class herons_root:
    def __init__(self, square: int, accuracy: float):
        self.square = square
        self.accuracy = accuracy
        self.guesses: list[float] = []

    def solve(self) -> float:
        """
        Heron of Alexandria's algorithm to find the square of root of x
        """
        guess = float(3)
        guess_square = guess**2
        self.guesses.append(guess)
        while not self.__accurate_enough(guess_square, self.square, self.accuracy):
            print("guess", guess)
            guess = (guess + self.square / guess) / 2
            guess_square = guess**2
            self.guesses.append(guess)

        return guess

    def __accurate_enough(self, value: float, target: float, accuracy: float) -> bool:
        return (target - accuracy < value) and (value < target + accuracy)

    def plot(self, has_labels=False) -> None:
        # location
        image_path = "./notebook/plots"

        # define data
        x = range(len(self.guesses))
        y = list(map(lambda x: x**2, self.guesses))
        labels = self.guesses

        # style
        plt.style.use("dark_background")

        # create scatterplot with axis labels

        # target
        plt.axhline(y=self.square, color="white", linestyle="--")

        # guesses
        for x_, y_, label in zip(x, y, labels):
            plt.plot(x_, y_, "o", color="#ff00ff")
            if has_labels == True:
                plt.text(x_ * (1 + 0.01), y_ * (1 + 0.01), label, fontsize=8)

        # plt.scatter(x, y)
        plt.xlabel("iteration")
        plt.ylabel("g_squared")

        # save figure to SVG file
        plt.savefig(f"{image_path}/herons-root_{self.square}_a-{self.accuracy:.2E}.svg")

        # clear buffer to prevent unexpected behavior
        plt.clf()
