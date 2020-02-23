import datetime

class Bike:
    def __init__(self, license_number: int = None, color: str = None, type: str = None, owner_id: int = None,
                 id: int = None,
                 created_by: int = None,
                 created_at: datetime = None,
                 update_by: int = None,
                 updated_at: datetime = None):
        self.id: int = id
        self.license_number: int = license_number
        self.color: str = color
        self.type: str = type
        self.owner_id: int = owner_id
        self.created_by: int = created_by
        self.created_at: datetime = created_at
        self.update_by: int = update_by
        self.updated_at: datetime = updated_at
