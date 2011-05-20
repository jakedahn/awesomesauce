import openstack.compute
import settings


def get_compute_api():
    api = openstack.compute.Compute(username=settings.OSAPI_USER,
                                    apikey=settings.OSAPI_KEY,
                                    auth_url=settings.OSAPI_URL)
    api.authenticate()
    return api
