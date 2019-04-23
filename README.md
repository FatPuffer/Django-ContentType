# Django-ContentType

学位课：degreecourse

|ID|Name|
|-|-|
|1|python|
|2|java|
|3|数据库|

普通课：commoncourse

|ID|Name|
|-|-|
|1|python基础|
|2|java基础|
|3|mysql|

svip课：svipcourse

|ID|Name|
|-|-|
|1|rest_framework|
|2|vue|
|3|javaee|

----------------------------------------------------------
价格策略：pricepolicy

|ID|price|period(月)|表名称|课程id|
|-|-|-|-|-|
|1|9.9|1|degreecourse|1|
|2|19.9|2|degreecourse|2|
|3|16.8|3|commoncourse|3|
|4|8.8|2|svipcourse|1|

----------------------------------------------------------
价格策略：pricepolicy

|ID|price|period|表名称|课程id|
|-|-|-|-|-|
|1|9.9|1|8|1|
|2|19.9|2|8|2|
|3|16.8|3|7|3|
|4|8.8|2|9|1|


ContentType表

|ID|应用名|模型类名(即数据库表名)|
|-|-|-|
|1|admin|logentry|
|2|auth|permission|
|3|auth|group|
|4|auth|user|
|5|contenttypes|contenttype|
|6|sessions|session|
|7|app01|commoncourse|
|8|app01|degreecourse|
|9|app01|svipcourse|
|10|app01|pricepolicy|

