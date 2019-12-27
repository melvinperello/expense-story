#### atm_user
A user that will use the application with a username and password, each user can be associated to have multiple funds.

| Constraints | Name | Type | Length | Null | Default | References |
|:----------:|------|------|--------|:----:|:--------:|------------|
| **PK** | **id** | integer |  | N | **Auto**| |
|  | username | varchar | 255 | Y | | |
|  | password | varchar | 255 | Y | | |

#### atm_fund
The fund to to record, each fund is owned by only one user, a fund can have multiple fund transactions.

| Constraints | Name | Type | Length | Null | Default | References |
|:----------:|------|------|--------|:----:|:--------:|------------|
| **PK** | **id** | integer |  | N | **Auto**| |
| FK | user_id | integer |  | N | Ref | *atm_user*.**id**|
|  | description | varchar | 255 | Y | | |


#### atm_fund_transaction
A fund will then have a transaction, everytime a fund is created it should always have a starting transaction which will debit the initial value of the fund.

| Constraints | Name | Type | Length | Null | Default | References |
|:----------:|------|------|--------|:----:|:--------:|------------|
| **PK** | **id** | integer |  | N | **Auto**| |
| FK | fund_id | integer |  | N | Ref | *atm_fund*.**id**|
|  | amount | money |  | N | | |
|  | debit_credit | varchar | 50 | Y | credit | |
|  | description | varchar | 255 | Y | | |


#### atm_transaction_tag
Each transaction can be optionally tag for post transaction reporting using different tag as expense category.

| Constraints | Name | Type | Length | Null | Default | References |
|:----------:|------|------|--------|:----:|:--------:|------------|
| **PK** | **id** | integer |  | N | **Auto**| |
|  | name | varchar | 50 | Y | | |
|  | description | varchar | 255 | Y | | |


#### atm_fund_transaction_tag
**atm_fund_transaction** (atm_fund_transaction_tag) as *Many to Many* Relationship with **atm_transaction_tag**

| Constraints | Name | Type | Length | Null | Default | References |
|:----------:|------|------|--------|:----:|:--------:|------------|
| **PK** | **id** | varchar(50) |  | N | CONCAT(*atm_fund_transaction*.**id** , "-" , *atm_tag*.**id**)| |
| FK | transaction_id | integer |  | N | Ref | *atm_fund_transaction*.**id**|
| FK | tag_id | integer |  | N | Ref | *atm_transaction_tag*.**id**|
|  | name | varchar | 50 | Y | | |
|  | description | varchar | 255 | Y | | |


#### AUDIT COLUMNS
Each table should have this columns that will server for audit trails.

| Constraints | Name | Type | Length | Null | Default | References |
|:----------:|------|------|--------|:----:|:--------:|------------|
|  | created_by | varchar | 255 | N | *user* | |
|  | created_at | timestamp |  | N | *database timestamp*  | |
|  | updated_by | varchar | 255 | N | *user* | |
|  | updated_at | timestamp |  | N | *database timestamp*  | |
