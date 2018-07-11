## Feature Table


### GET /api/feature_table/?\<params>

This method gets feature tables from DB. If you doesn't put any parameter, so it will return all.
- Parameters:
    - f_table_name (optional) (text): the feature table name (e.g. 'layer_X').
- Examples:
     - Get all feature tables: http://localhost:8888/api/feature_table/
     - Get one feature table by name: http://localhost:8888/api/feature_table/?f_table_name=layer
- Send (in Body):
- Send (in Header):
- Response: a JSON that contains the resources selected. Example:
    ```javascript
    {
        'features': [
            {
                'type': 'FeatureTable',
                'f_table_name': 'layer_1003',
                'properties': {'name': 'text', 'id': 'integer', 'end_date': 'timestamp without time zone',
                               'geom': 'geometry', 'version': 'integer', 'changeset_id': 'integer',
                               'start_date': 'timestamp without time zone'},
                'geometry': {
                    'crs': {'type': 'name', 'properties': {'name': 'EPSG:4326'}},
                    'type': 'MULTILINESTRING'
                }
            }
        ],
        'type': 'FeatureCollection'
    }
    ```
- Error codes:
    - 404 (Not Found): Not found any resource.
    - 500 (Internal Server Error): Problem when get a resource. Please, contact the administrator.
- Notes:


### POST /api/feature_table/create/

This method creates a new feature table described in a JSON.
- Parameters:
- Examples:
    - Create a feature_table: ```POST http://localhost:8888/api/feature_table/create```
- Send (in Body): a JSON describing the resource. Example:
    ```javascript
    {
        'type': 'FeatureTable',
        'f_table_name': 'addresses',
        'properties': {'start_date': 'timestamp', 'end_date': 'timestamp',
                       'address': 'text', 'count': 'int'},
        'geometry': {
            'crs': {'type': 'name', 'properties': {'name': 'EPSG:4326'}},
            'type': 'MULTIPOINT'
        }
    }
    ```
- Send (in Header):
    - Send an "Authorization" header with a valid Token.
- Response:
- Error codes:
     <!--- 400 (Bad Request): Attribute already exists.-->
     <!--- 400 (Bad Request): Some attribute in JSON is missing. Look the documentation!-->
     - 401 (Unauthorized): It is necessary an Authorization header valid.
     - 500 (Internal Server Error): Problem when create a resource. Please, contact the administrator.
- Notes:


### DELETE

A feature table is automatically removed when a layer is deleted.