def test_many_default_azure_obcs(bucket_factory):
    bucket_factory(amount=100, interface="OC")
