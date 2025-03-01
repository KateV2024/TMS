import pytest
from api.endpoints.get_obj import GetObj
from api.endpoints.delete_obj import DeleteObj
from api.payload.payloads import valid_create_payload, valid_update_payload
from api.endpoints.create_obj import CreateObj
from api.endpoints.update_obj import UpdateObj


@pytest.fixture
def create_obj():
   return CreateObj()

@pytest.fixture
def get_obj():
    new_obj = CreateObj()
    new_obj.new_obj(valid_create_payload)
    created_obj_id = new_obj.get_data()['id']
    yield created_obj_id
    get_obj_instance = GetObj()
    get_obj_instance.get_obj(created_obj_id)

@pytest.fixture
def create_obj_with_data():
    new_obj = CreateObj()
    new_obj.new_obj(valid_create_payload)
    created_obj_id = new_obj.get_data()['id']
    yield created_obj_id
    delete_obj = DeleteObj()
    delete_obj.delete_obj(created_obj_id)

@pytest.fixture(params=[
    (valid_create_payload, True)
])
def test_data(request):
    return request.param

@pytest.fixture
def update_obj_with_data():
    new_obj = CreateObj()
    new_obj.new_obj(valid_create_payload)
    created_obj_id = new_obj.get_data().get('id')  # ✅ Use .get() to prevent KeyError
    assert created_obj_id, "❌ Object creation failed, no ID returned!"

    update_obj = UpdateObj()
    update_obj.update_obj(created_obj_id, valid_update_payload)  # ✅ Update object

    yield created_obj_id  # ✅ Pass the correct object ID
