import threading
 
class DiningPhilosophers:
    def __init__(self):
        # List of semaphores, one for each fork
        self.forks = [threading.Semaphore(1) for _ in range(5)]
 
    # call the functions directly to execute, for example, eat()
    def wantsToEat(self,
                   philosopher: int,
                   pickLeftFork: 'Callable[[], None]',
                   pickRightFork: 'Callable[[], None]',
                   eat: 'Callable[[], None]',
                   putLeftFork: 'Callable[[], None]',
                   putRightFork: 'Callable[[], None]') -> None:
        # Take the right fork, then left fork
        self.forks[philosopher].acquire()
        self.forks[(philosopher + 1) % 5].acquire()
 
        # Eat!
        pickRightFork()
        pickLeftFork()
        eat()
        putRightFork()
        putLeftFork()
 
        # Release right fork, then left fork
        self.forks[philosopher].release()
        self.forks[(philosopher + 1) % 5].release()