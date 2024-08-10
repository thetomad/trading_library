BAR_LENGTH_DEFAULT = 30


class ProgressBar:
    
    def __init__(self, index: int, total: int, bar_lenght: int = BAR_LENGTH_DEFAULT) -> None:
        """
        This class will define a progress bar that prints a dynamic progress bar.
        
        :param index:       The current index of the progress bar iteration.
        :param total:       The total number of iterations.
        :param bar_lenght:  The bar lenght displayed.
        """
        
        self.index = index
        self.total = total
        self.bar_lenght = bar_lenght
        self.milestones_crossed = int(self.index / self.total * self.bar_lenght)
        print(self.__str__())
    
    def __str__(self) -> str:
        "Returning the bar."
        return "\033[F\033[K" + " " * 40 + "\r" + "█" * self.milestones_crossed + " " * (self.bar_lenght - self.milestones_crossed) + " "
    
    def __repr__(self) -> str:
        "Returning the bar."
        return "\033[F\033[K" + " " * 40 + "\r" + "█" * self.milestones_crossed + " " * (self.bar_lenght - self.milestones_crossed) + " "


class PercentProgressBar(ProgressBar):
    def __init__(self, index: int, total: int, bar_lenght: int = BAR_LENGTH_DEFAULT, text_type: str = "percent") -> None:
        self.text_type = text_type
        super().__init__(index, total, bar_lenght)
        
    def __str__(self) -> str:
        prev_string = super().__str__()
        try:
            if self.text_type == "percent":
                return prev_string + f" {(self.index / self.total * 100):.2f}%"
            elif self.text_type == "text":
                return prev_string + f" {self.index} out of {self.total} completed."
            elif self.text_type == "text percent":
                return prev_string + f" {(self.index / self.total * 100):.2f}%" + " | " + f" {self.index} out of {self.total} completed."
            
            raise ValueError("Not recognized text_type value.")
        except ValueError as e:
            raise ValueError("The type for PercentProgressBar object is not recognized.\nThe text_type be one of the following ['text', 'percent', 'text percent']") from e
            
            
            