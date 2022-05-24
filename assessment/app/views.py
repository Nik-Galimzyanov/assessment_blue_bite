from django.forms import ValidationError
from django.shortcuts import render, get_object_or_404
from django.db import transaction
from django.db.models import Q
from rest_framework.views import APIView
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import ParseError
import jsonschema

from . import schemas
from .objects import prepare_objects, get_object_by_id_response, get_objects_by_params_response
from .models import Objects, Batch


class ObjectsHandlerView(APIView):
    '''
    API-endpoint for creating new objects
    :param: 
    :return:
    '''

    def post(self, request, *args, **kw):

        # Parsing the request
        request_data = JSONParser().parse(request)

        # Validate according to JSON schema
        try:
            jsonschema.validate(request_data, schemas.create_objects_schema)
        except jsonschema.ValidationError as error:
            detail = {
                "Error": error.message,
                "Path": error.path
            }
            raise ParseError(detail=detail)

        # Check if we have at least one object, if not - raise Parse Error
        if not request_data['objects']:
            response = {
                "Message": f"No objects for Batch ID - {request_data['batch_id']}"
            }
            raise ParseError(detail=response)

        # Do we want to store objects with valid data, and collect ids for ones with empty data?
        objects_pool = []
        # For each object check if there is a data, if yes - save in the db
        batch = Batch.objects.create(batch_id=request_data['batch_id'])
        for object in request_data['objects']:
            if not object['data']:
                response = {
                    "Message": f"No data for Object ID - {object['object_id']}"
                }
                raise ParseError(detail=response)
                
            ready_objects = prepare_objects(object['object_id'], object['data'], batch)
            objects_pool += ready_objects
        
        # Save objects to the db
        Objects.objects.bulk_create(objects_pool)

        response = {
            "Message": f"Batch with ID - {request_data['batch_id']} successfully created"
        }

        return Response(response, status=status.HTTP_201_CREATED)


class GetObjectById(APIView):
    '''
    API-endpoint to get object by ID
    :param:
    :return:
    '''

    def get(self, request, object_id):
        
        data = Objects.objects.filter(object_id=object_id).values_list('data', flat=True)

        # Check if there is at least one matching object
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

        return Response(response, status=status.HTTP_200_OK)


class GetObjectByParams(APIView):
    '''
    API-endpoint to get objects by parameters
    :param:
    :return:
    '''

    def get(self, request,  *args, **kw):

        # Parsing the request
        request_data = JSONParser().parse(request)

        # Validate according to JSON schema
        try:
            jsonschema.validate(request_data, schemas.get_objects_by_params_schema)
        except jsonschema.ValidationError as error:
            detail = {
                "Error": error.message,
                "Path": error.path
            }
            raise ParseError(detail=detail)

        objects_ids = set()

        # Go through params and append object ids to the pool
        for param in request_data:
            q = Q()
            if param.get('key'):
                q &= Q(data__key=param['key'])
            if param.get('value'):
                q &= Q(data__value=param['value'])

            if not q: 
                response = {
                    "Message": f"There should be at least one key or a value in the request."
                }
                return Response(response, status=status.HTTP_400_BAD_REQUEST)
            
            objects_ids |= set(Objects.objects.filter(q).values_list('object_id', flat=True).distinct())

        # Check if there's at least one matching object 
        if not objects_ids:
            response = {
                "Message": f"Objects for given parameters not found."
            }
            return Response(response, status=status.HTTP_404_NOT_FOUND)

        response = get_objects_by_params_response(objects_ids)

        return Response(response, status=status.HTTP_200_OK)
        