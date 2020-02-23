from bikeApi.models.party import Party


class User(Party):
    def __init__(self, *args, **kwargs):
        super(User, self).__init__(*args, **kwargs)
