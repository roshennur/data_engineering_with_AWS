import boto3
import awswrangler as wr
from urllib.parse import unquote_plus

def lambda_handler(event, context):
    results = []
    
    # 1. Process every record in the trigger event
    for record in event['Records']:
        bucket = record['s3']['bucket']['name']
        key = unquote_plus(record['s3']['object']['key'])
        
        # 2. Split path logic inside the loop
        key_list = key.split("/")
        print(f'key_list: {key_list}')
        
        # Guard rail: Make sure the file path is deep enough to parse db and table
        if len(key_list) < 3:
            print(f"Skipping key {key} because it doesn't match expected deep folder structure.")
            continue
            
        db_name = key_list[len(key_list)-3]
        table_name = key_list[len(key_list)-2]
        
        print(f'Bucket: {bucket}')
        print(f'Key: {key}')
        print(f'DB Name: {db_name}')
        print(f'Table Name: {table_name}')
        
        input_path = f"s3://{bucket}/{key}"
        print(f'Input_Path: {input_path}')
        output_path = f"s3://dataeng-clean-zone1471/{db_name}/{table_name}/"
        print(f'Output_Path: {output_path}')
        
        # 3. Read raw CSV
        input_df = wr.s3.read_csv([input_path])
        
        # 4. Check & Create Glue Database cleanly
        current_databases = wr.catalog.databases()
        if db_name not in current_databases["Database"].to_list():
            print(f'- Database {db_name} does not exist ... creating')
            wr.catalog.create_database(db_name)
        else:
            print(f'- Database {db_name} already exists')
        
        # 5. Write to Parquet and update Glue Catalog
        result = wr.s3.to_parquet(
            df=input_df, 
            path=output_path, 
            dataset=True,
            database=db_name,
            table=table_name,
            mode="append"
        )
            
        print("RESULT: ")
        print(f'{result}')
        results.append(result)
        
    return {
        'statusCode': 200,
        'body': f"Successfully processed {len(results)} file(s)."
    }