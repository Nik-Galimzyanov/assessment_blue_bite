from .models import Objects
from rest_framework.response import Response
from rest_framework import status


def prepare_objects(object_id, objects, batch):
    '''
    Prepare objects to be saved to the db
    :param:
    :return:
    '''
    bulk = []
    for object in objects:
        if object:
            o = Objects(
                object_id=object_id,
                data=object,
                batch=batch
            )
            bulk.append(o)
    
    return bulk


def get_object_by_id_response(object_id):
    '''
    Get object by id
    :param:
    :return:
    '''
    data = Objects.objects.filter(object_id=object_id).values_list('data', flat=True)

    if not data:
        response = {
            "Message": f"Object with ID - {object_id} not found."
        }
        return Response(response, status=status.HTTP_404_NOT_FOUND)

    response = {
        "object_id": object_id,
        "data": [

        ]
    }
    for single_data in data:
        response['data'].append(
            single_data
        )

    return response


def get_objects_by_params_response(object_ids):
    '''
    Get objects by parameters
    :param:
    :return:
    '''
    response = []
    for o_id in object_ids:
        object = get_object_by_id_response(o_id)
        response.append(object)
    
    return response
    