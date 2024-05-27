class Book():
    title = None
    price = None
    price_with_rate = None
    universal_product_code = None
    stok = None
    reviews = None
    
    @classmethod
    def from_dict(cls, args):
        return cls(**args)
    
    def __init__(self, **kwargs):
        for key, val in kwargs.items():
            setattr(self, key, val)
            
    def to_dict(self):
        return {key: getattr(self, key) for key in self.__dict__ if not key.startswith('__')}