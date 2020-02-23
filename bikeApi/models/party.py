import datetime


class Party:
    def __init__(self, first_name: str = None, last_name: str = None,
                 id: int = None,
                 created_by: int = None,
                 created_at: datetime = None,
                 update_by: int = None,
                 updated_at: datetime = None):
        self.id: int = id
        self.first_name: int = first_name
        self.last_name: str = last_name
        self.created_by: int = created_by
        self.created_at: datetime = created_at
        self.update_by: int = update_by
        self.updated_at: datetime = updated_at
