import pytest
from module.Readytouse_API import ReadytouseAPI
class TestReadyToUseAPI:
    @pytest.fixture(autouse=True)
    def setup(self):
        self.api_obj=ReadytouseAPI()
    def test_total_entry(self):
        total_entry=self.api_obj.verify_total_mobile_entry()
        assert total_entry[0] == 13
        assert total_entry[1]== 200

    def test_spcefic_list_id_entries(self):
        response_data = self.api_obj.verify_to_get_details_for_id_list([5,7,8])
        assert len(response_data[0]) == 3
        assert response_data[1] == 200

    def test_create_new_entry_in_db(self):
        response_data=self.api_obj.create_new_entry_of_mobile_details()
        assert response_data[1]==200
        self.api_obj.log.info(f"new id :{response_data[0]['id']}")


