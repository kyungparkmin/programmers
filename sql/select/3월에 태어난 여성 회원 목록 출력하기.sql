SELECT MEMBER_ID, MEMBER_NAME, GENDER, date_format(DATE_OF_BIRTH, '%Y-%m-%d') as date_or_birth
from MEMBER_PROFILE
where gender = "W" and NOT TLNO IS NULL and substring(DATE_OF_BIRTH, 6, 2) = '03'
order by MEMBER_ID asc;