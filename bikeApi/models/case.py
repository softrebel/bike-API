import datetime


class Case:
    def __init__(self, bike_id: int = None, police_id: int = None,
                 descriptions: str = None,
                 resolve: bool = None,
                 created_by: int = None,
                 created_at: datetime = None,
                 update_by: int = None,
                 updated_at: datetime = None):
        self.id: int = id
        self.bike_id: int = bike_id
        self.police_id: int = police_id
        self.descriptions: str = descriptions
        self.resolve: str = resolve
        self.created_by: int = created_by
        self.created_at: datetime = created_at
        self.update_by: int = update_by
        self.updated_at: datetime = updated_at
