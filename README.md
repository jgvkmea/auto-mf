# auto-mf

auto-mf automate to update account information of money forward.

## Usage

local

```
$ export AWS_ACCOUNT_ID=<YOUR_ACCOUNT_ID>
$ export AWS_REGION=<YOUR_REGION>
$ make build
$ make run
$ curl -d '{"email":"<your email>", "password": "<password>"}' http://localhost:9000/2015-03-31/functions/function/invocations
```
