from bikeApi.models.party import Party


class Police(Party):
    def __init__(self, *args, **kwargs):
        super(Police, self).__init__(*args, **kwargs)