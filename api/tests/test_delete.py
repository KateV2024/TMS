from api.endpoints.delete_obj import DeleteObj


def test_delete_obj(create_obj_with_data):
    id_obj = create_obj_with_data
    delete_obj = DeleteObj()
    delete_obj.delete_obj(id_obj)
    delete_obj.check_response_is_200()
    delete_obj.validate(delete_obj.get_data())

    assert 'deleted' in delete_obj.get_data()['message'], "Incorrect message after object delete"
    delete_obj.delete_obj(id_obj)