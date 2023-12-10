from datetime import datetime


class Operation:
    def __init__(
            self,
            num_id: int,
            date: str | datetime,
            state: str,
            operation_amount: dict,
            description: str,
            from_: str,
            to: str
    ) -> object:
        self.num_id = num_id
        self.date = date
        self.state = state
        self.operation_amount = operation_amount
        self.description = description
        self.from_ = from_
        self.to = to

