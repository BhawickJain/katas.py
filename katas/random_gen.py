import random
import math  # added


class RandomGen(object):
    # Values that may be returned by next_num()
    _random_nums: list[int] = []
    # Probability of the occurrence of random_nums
    _probabilities: list[float] = []
    # Memoised Cumulative Probability
    _cumulative: list[float] = []

    def __init__(
        self, random_nums: list[int], probabilities: list[float], random=random.random
    ):
        """Initialise a random generator that samples a list of numbers with a
        discrete probability of each.

        Args:
            random_nums: values to be sampled from when randomly chosen
            probabilities: respective probability random_num at index being chosen
            random (optional): pseudo random generator from 0-1, default is python's random.random

        Returns:
            An initialised random generator with a population of values to sample with their
            respective probability of being chosen.
        """
        # input validation
        if (len(random_nums) == 0) | (len(probabilities) == 0):
            raise ValueError("received empty list in one or more arguments")
        if len(random_nums) != len(probabilities):
            raise ValueError("length of number list does not match probability list")
        if not all_items_numeric(random_nums):
            raise ValueError(
                "random_nums has non-numeric items, only numeric items expected"
            )
        if not all_items_numeric(probabilities):
            raise ValueError(
                "probabilities has non-numeric items, only numeric items expected"
            )

        self._random_nums = random_nums
        self._probabilities = probabilities
        self._cumulative = RandomGen.get_cumulative(probabilities)
        self._random = random

    def next_num(self) -> int:
        """Returns one of the random_nums. When this method is called multiple
        times over a long period, it should return the numbers roughly
        with the initialized probabilities.

        Returns:
            a single item sampled from the random_nums list

        Notes:
        Implemented using the Roulette Selection method, described in:
        https://keithschwarz.com/darts-dice-coins/
        """
        random_number = self._random()
        print(random_number)
        ceil_index = RandomGen.find_index_ceiling(random_number, self._cumulative)
        return self._random_nums[ceil_index]

    @classmethod
    def find_index_ceiling(
        cls, random_number: float, cumulative_probability: list[float]
    ) -> int:
        """Returns the lowest index position in the cumulative probability
        where the random number less than or equal to the value at index.

        time: O(log(n))

        Args:
            random_number: a value between 0,1 chosen by a random generator
            cumulative_probability: a list of floats which cumulatively add up to 1

        Returns:
            the lowest index position along the cumulative_probability list which
            equal or encloses the random_number argument.
        """
        low = 0
        high = len(cumulative_probability) - 1
        index_ceiling = len(cumulative_probability) - 1
        while low <= high:
            mid = math.floor((low + high) / 2)
            if random_number <= cumulative_probability[mid]:
                if mid < index_ceiling:
                    index_ceiling = mid
                high = mid - 1
            else:
                low = mid + 1
        return index_ceiling

    @classmethod
    def get_cumulative(cls, probabilities: list[float]) -> list[float]:
        """Returns a cumulative array of probabilities from a given probability
        array.

        time: O(n)

        Args:
            probabilities: list of float representing a probability distribution

        Returns:
            a list of float representing a cumulative distribution
        """
        cumulative: list[float] = [0]
        for p in probabilities:
            # validation
            if p < 0:
                raise ValueError("probability array input contains negative numbers")
            cumulative.append(p + cumulative[-1])

        # math.isclose
        # take away helper value 0 at start
        cumulative = cumulative[1:]

        # validation
        if cumulative[-1] != 1:
            raise ValueError("probabilities do not cumulatively add to 1")

        return cumulative


# utility function for tests
def is_accurate_enough(
    val: int | float, target: int | float, accuracy_bound: float
) -> bool:
    """Returns true is val is inclusively within +/- accuracy_bound

    Args:
        val: value to be checked if it is accurate enough
        target: accurate target value
        accuracy_bound: float which defined the +/- bound around the target

    Returns:
        True if val is within or at the accuracy boundary of the target value.
    """
    if val > (target + accuracy_bound):
        return False
    if val < (target - accuracy_bound):
        return False
    return True


# utility function for input validation
def all_items_numeric(array_of_item: list) -> bool:
    """Returns true is all items in the array are of numeric type (int | float)

    time: O(n)

    Args:
        array_of_item: list of items that is to be evaluated

    Returns:
        True all items in the list are of numeric type
    """
    for item in array_of_item:
        if not isinstance((item), (float | int)):
            return False
    return True
