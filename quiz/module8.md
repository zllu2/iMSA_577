Format:
Question: ...  
Type: Multiple Choice (Single Correct Answer),  Multiple Choice (Multiple Correct Answers), Free Response (Text Answers, Code Expression)
Answer: ...  
Choices: ...  

# Lesson 1
- Question 1.1: What is the starting point for time data (epoch)?
  - Type: Multiple choice (single correct response)
  - Answer: January 1, 1970
  - Choices:January 1, 1970, January 1, 0000, January 1, 1950
- Question 1.2: True or False? Epoch time is defined in UTC timezone.
  - Type: Multiple choice (single correct response)
  - Answer: True
  - Choices: True; False

- Question 2.1: What library effectively deals with dates and times from around the world?
  - Type: Multiple choice (single correct response)
  - Answer: datetime
  - Choices: datetime, numpy, pandas
- Question 2.2: Which function or class allows you to perform math operations on times and dates?
  - Type: Multiple choice (single correct response)
  - Answer: datetime.timedelta
  - Choices: datetime.timedelta, datetime, datetime.datetime, date.time.math
- Question 2.3: In which module is timedelta defined?
  - Type: Multiple choice (single correct response)
  - Answer: datetime
  - Choices: datetime, date, time, pandas

- Question 3.1: Which datetime function allows you to convert a datetime object to a datetime string representation?
  - Type: Multiple choice (single correct response)
  - Answer: strftime
  - Choices: strftime, strptime
- Question 3.2: Which datetime function allows you to convert a datetime string to a datetime object?
  - Type: Multiple choice (single correct response)
  - Answer: strptime
  - Choices: strftime, strptime

- Question 4.1: If d_day is a datetime object for June 6, 1944, what date is d_day + timedelta(days=1)?
  - Type: Multiple choice (single correct response)
  - Answer: June 7, 1944
  - Choices: June 5, 1944; June 6, 1944; June 7, 1944
- Question 4.2: If d_day is a datetime object for June 6, 1944, what date is d_day - timedelta(days=2)?
  - Type: Multiple choice (single correct response)
  - Answer: June 4, 1944
  - Choices: June 4, 1944; June 6, 1944; June 8, 1944

- Question 5.1: If d_day is a datetime object for June 6, 1944, what string is d_day.strftime('%m/%d/%Y')?
  - Type: Multiple choice (single correct response)
  - Answer: 06/06/1944
  - Choices: June 6, 1944; 06/06/1944; 1944-06-06
- Question 5.2: If d_day is a datetime object for June 6, 1944, what string is d_day.strftime('%Y-%m-%d')?
  - Type: Multiple choice (single correct response)
  - Answer: 1944-06-06
  - Choices: June 6, 1944; 06/06/1944; 1944-06-06

- Question 6.1: Which pandas function convert a column of datetime string to a column of datetime object?
  - Type: Multiple choice (single correct response)
  - Answer: to_datetime()
  - Choices: to_datetime(); strptime()
- Question 6.2: True or False? Pandas to_datetime() function can handle any datetime format by default.
  - Type: Multiple choice (single correct response)
  - Answer: False
  - Choices:True; False

# Lesson 2
- Question 7.1: Which pandas function convert a column of datetime object to a datetime index?
  - Type: Multiple choice (single correct response)
  - Answer: DatetimeIndex()
  - Choices: to_datetime(); strptime(); DatetimeIndex()
- Question 7.2: True or False? A time series data is a series of data points indexed in time order.
  - Type: Multiple choice (single correct response)
  - Answer: True
  - Choices:True; False

- Question 8.1: Which DataFrame function returns a rolling object of a time series dataframe?
  - Type: Multiple Choice (Single Correct Answer)
  - Answer: rolling()
  - Choices: rolling(); sampling(); resample();
- Question 8.2: Which DataFrame function resample a time series dataframe?
  - Type: Multiple Choice (Single Correct Answer)
  - Answer: resample()
  - Choices: rolling(); sampling(); resample();

- Question 9.1: Which resample code represents "business day frequency"?
  - Type: Multiple Choice (Single Correct Answer)
  - Answer: B
  - Choices: B; D; W; BMS;
- Question 9.2: Which resample code represents "business month start frequency"?
  - Type: Multiple Choice (Single Correct Answer)
  - Answer: BMS
  - Choices: B; D; W; BMS;

- Question 10.1: In seasonal decomposition, what is the repeating short-term cycle in the series?
  - Type: Multiple Choice (Single Correct Answer)
  - Answer: Seasonality
  - Choices: Level; Trend; Seasonality; Noise
- Question 10.2: In seasonal decomposition, what is the random variation in the series?
  - Type: Multiple Choice (Single Correct Answer)
  - Answer: Noise
  - Choices: Level; Trend; Seasonality; Noise
