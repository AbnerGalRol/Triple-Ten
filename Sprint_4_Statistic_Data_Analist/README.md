# Which plan is better?

You work as an analyst for the telecommunications operator Megaline. The company offers its customers two prepaid plans, Surf and Ultimate. The marketing department wants to know which of the plans generates more revenue in order to adjust the advertising budget.

You will conduct a preliminary analysis of the plans based on a relatively small selection of customers. You will have data from 500 Megaline customers: who they are, where they are from, which plan they use, as well as the number of calls they made and text messages they sent in 2018. Your job is to analyze customer behavior and determine which prepaid plan generates more revenue.

Before analyzing our hypotheses, let's analyze the behavior of users of each plan to find differences or similarities in their needs. We will analyze the messaging, minutes, and monthly gigabytes needs of users of each plan, as well as the monthly revenue per user of each plan. All this in order to understand the behavior of users in each plan and to know which one is generating higher revenues.

## Hypotheses to analyze:

- The mean monthly revenues of each plan are different.
- The mean monthly revenues of users from the NY-NJ sector and those from other sectors are different.

## Description of the plans

Note: Megaline rounds seconds to minutes and megabytes to gigabytes. For calls, each individual call is rounded up: even if the call lasted only one second, it will count as one minute. For web traffic, individual web sessions are not rounded up. Instead, the total for the month is rounded up. If someone uses 1025 megabytes this month, they will be charged for 2 gigabytes.

**Surf**

Monthly payment: $20
500 minutes per month, 50 SMS, and 15 GB of data
If package limits are exceeded:
1 minute: 3 cents
1 SMS: 3 cents
1 GB of data: $10

**Ultimate**

Monthly payment: $70
3000 minutes per month, 1000 SMS, and 30 GB of data
If package limits are exceeded:
1 minute: 1 cent
1 SMS: 1 cent
1 GB of data: $7

## Data Description

Don't forget! Megaline rounds seconds to minutes and megabytes to gigabytes. For calls, each individual call is rounded up: even if the call lasted only one second, it will count as one minute. For web traffic, individual web sessions are not rounded up. Instead, the total for the month is rounded up. If someone uses 1025 megabytes this month, they will be charged for 2 gigabytes.

**The users table (data about the users):**

user_id — unique user identifier
first_name — user's first name
last_name — user's last name
age — user's age (in years)
reg_date — subscription date (dd, mm, yy)
churn_date — the date the user stopped using the service (if the value is missing, the tariff was being used when these data were retrieved)
city — user's city of residence
plan — name of the plan

**The calls table (data about the calls):**

id — unique call identifier
call_date — call date
duration — call duration (in minutes)
user_id — user identifier who made the call

**The messages table (data about the SMS messages):**

id — unique message identifier
message_date — message date
user_id — user identifier who sent the message

**The internet table (data about the web sessions):**

id — unique session identifier
mb_used — volume of data spent during the session (in megabytes)
session_date — web session date
user_id — user identifier

**The plans table (data about the plans):**

plan_name — plan name
usd_monthly_fee — monthly payment in US dollars
minutes_included — minutes included per month
messages_included — SMS included per month
mb_per_month_included — data included per month (in megabytes)
usd_per_minute — price per minute after exceeding the package limits (for example, if the package includes 100 minutes, the operator will charge for minute 101)
usd_per_message — price per SMS after exceeding the package limits
usd_per_gb — price per gigabyte of extra data after exceeding the package limits (1 GB = 1024 megabytes)














