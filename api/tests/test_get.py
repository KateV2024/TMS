from api.endpoints.get_obj import GetObj


def test_get_obj(create_obj_with_data):
    id_obj = create_obj_with_data
    get_obj = GetObj()
    get_obj.get_obj(id_obj)
    get_obj.check_response_is_200()
    get_obj.validate(get_obj.get_data())
