from import_export import resources
from .models import TaxPayee


class TaxPayeeResource (resources.ModelResource):
    class meta:
        model = TaxPayee