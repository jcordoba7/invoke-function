import io
import json
import oci
from fdk import response

def handler(ctx, data: io.BytesIO=None):
    try:
        body = json.loads(data.getvalue())
        function_endpoint = body.get("https://ncjgmq4tscq.us-phoenix-1.functions.oci.oraclecloud.com")
        function_ocid = body.get("ocid1.fnfunc.oc1.phx.aaaaaaaaqtmw7jyllvkqxqnb2k7yiq3evloyy5zqj7kswuqn2u62cflchaya")
        function_body = body.get("")
    except (Exception) as ex:
        print('ERROR: Missing key in payload', ex, flush=True)
        raise
    
    signer = oci.auth.signers.get_resource_principals_signer()
    client = oci.functions.FunctionsInvokeClient(config={}, signer=signer, service_endpoint=function_endpoint)
    resp = client.invoke_function(function_id=function_ocid, invoke_function_body=function_body)
    print(resp.data.text, flush=True)

    return response.Response(
        ctx, 
        response_data=resp.data.text,
        headers={"Content-Type": "application/json"}
    )