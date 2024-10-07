from vendors.google_vendor import GoogleVendor
from vendors.openai_vendor import OpenAIVendor

class VendorGetter:
    def __init__(self):
        pass

    def get_vendor(self, vendor_name):
        return {
            "google": GoogleVendor(),
            "openai": OpenAIVendor()
        }.get(vendor_name, GoogleVendor())