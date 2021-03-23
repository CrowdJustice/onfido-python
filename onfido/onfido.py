from .resources.applicants import Applicants
from .resources.documents import Documents
from .resources.address_picker import Addresses
from .resources.checks import Checks
from .resources.reports import Reports
from .resources.live_photos import LivePhotos
from .resources.live_videos import LiveVideos
from .resources.webhooks import Webhooks
from .resources.sdk_tokens import SdkToken
from .resources.extraction import Extraction
from .regions import Region
from .exceptions import OnfidoRegionError


class Api:
    def __init__(self, api_token, region, timeout=None):
        self.applicant = Applicants(api_token, region, timeout)
        self.document = Documents(api_token, region, timeout)
        self.address = Addresses(api_token, region, timeout)
        self.check = Checks(api_token, region, timeout)
        self.report = Reports(api_token, region, timeout)
        self.sdk_token = SdkToken(api_token, region, timeout)
        self.webhook = Webhooks(api_token, region, timeout)
        self.live_photo = LivePhotos(api_token, region, timeout)
        self.live_video = LiveVideos(api_token, region, timeout)
        self.extraction = Extraction(api_token, region, timeout)
    
        valid_regions = [Region.EU, Region.US, Region.CA]

        if region not in valid_regions:
            raise OnfidoRegionError("region must be one of Region.EU, Region.US or Region.CA")
