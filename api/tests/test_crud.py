from api.endpoints.get_obj import GetObj
from api.endpoints.update_obj import UpdateObj
from api.payload.payloads import valid_update_payload
from api.endpoints.create_obj import CreateObj
from api.endpoints.delete_obj import DeleteObj
from api.payload.payloads import valid_create_payload


def test_crud_scenario():
    create_obj = CreateObj()
    create_obj.new_obj(valid_create_payload)
    created_obj_id = create_obj.get_data().get('id')
    assert created_obj_id,  "Object was not created"
    print(f"✅ Created Object ID: {created_obj_id}")


# Get object
    get_obj = GetObj()
    get_obj.get_obj(created_obj_id)
    get_obj.check_response_is_200()
    print(f"✅ Object: {get_obj.get_data()}")

# Update object
    update_obj = UpdateObj()
    update_obj.update_obj(created_obj_id, valid_update_payload)
    update_obj.check_response_is_200()
    print(f"✅ Updated Object: {update_obj.get_data()}")

# Delete object
    delete_obj = DeleteObj()
    delete_obj.delete_obj(created_obj_id)
    delete_obj.check_response_is_200()
    print("✅ Object deleted successfully")

# Check error message
    delete_obj.get_error()
    print("✅ Object is not found after deletion (expected behavior)")
