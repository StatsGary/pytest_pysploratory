from typing import List

class Band:
    def __init__(self, max_member_size:int):
        self.bands: List[str] = []
        self.members: List[str] = []
        self.max_member_size = max_member_size

    def add_band_name(self,band_name: str):
        self.bands.append(band_name)
    
    def number_of_bands(self) -> int:
        return len(self.bands)

    def number_of_members(self) -> int:
        return len(self.members)

    def get_bands(self) -> List[str]:
        return self.bands

    def add_members(self, member_name):
        if self.number_of_members() == self.max_member_size:
            raise OverflowError('Cannot add more members')
        self.members.append(member_name)

    def get_members(self) -> List[str]:
        for memb in self.members:
            print(f'Band member is: {memb}')
        return self.members


