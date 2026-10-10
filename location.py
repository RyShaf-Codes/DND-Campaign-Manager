class Location:
    def __init__(self, location_name, location_type, location_region, location_description):
        self.location_name = location_name
        self.location_type = location_type
        self.location_region = location_region
        self.location_description = location_description

    def to_dict(self):
        return {
            "location_name": self.location_name,
            "location_type": self.location_type,
            "location_region": self.location_region,
            "location_description": self.location_description
        }