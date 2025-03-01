from api.endpoints.get_obj import GetObj
from api.endpoints.update_obj import UpdateObj
from api.payload.payloads import valid_update_payload


def test_update_obj(update_obj_with_data):
    id_obj = update_obj_with_data
    get_obj = GetObj()
    get_obj.get_obj(id_obj)
    update_obj = UpdateObj()
    updated_response = update_obj.update_obj(id_obj, valid_update_payload)
    update_obj.check_response_is_200()
    update_obj.validate(updated_response)
