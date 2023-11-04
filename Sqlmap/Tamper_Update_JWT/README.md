## Description 

Tamper and postprocess script to update the JWT token when the server returns a certain http code, preventing sqlmap from stopping.

## Steps to Use

1. Create the following empty file in the execution directory:  `touch __init__.py`
2. Modify `postprocess_generate_token.py` with the HTTP code which indicates the need to refresh the JWT token, for example 401.
3. With sqlmap call the scripts and prevent it from quit when encountering an HTTP 401 code `--tamper=tamper_update_token.py --postprocess=postprocess_generate_token.py --ignore-code 401

Example of real exploitation:

```bash
sqlmap -u "foo_endpoint_vulnerable"  --data="{\"Vulnerable_Field\":\"sqli*\"}" --proxy="http://127.0.0.1:8080" --headers="Authorization: Bearer foo_token_eyJh...bY=" --tamper=tamper_update_token.py --postprocess=postprocess_generate_token.py --ignore-code 401
```


## REFERENCES

- [Sqlmapproject Postprocess](https://github.com/sqlmapproject/sqlmap/wiki/Usage#postprocess-response)
- [Tamper to refresh token in every request](https://blog.telspace.co.za/2020/05/bypassing-refresh-tokens-with-sqlmaps_20.html)
- [Sqlmapproject Preprocess and Postprocess example](https://github.com/sqlmapproject/sqlmap/issues/5221)
