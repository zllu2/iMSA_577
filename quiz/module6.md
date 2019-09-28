Format:
Question: ...  
Type: Multiple Choice (Single Correct Answer),  Multiple Choice (Multiple Correct Answers), Free Response (Text Answers, Code Expression)
Answer: ...  
Choices: ...  

# Lesson 1:
- Question 1.1: True or False? Tokenization is a process to break down a paragraph of text to smaller chunks, normally a single word or a phrase, which are called tokens.
  - Type: Multiple choice (single correct response)
  - Answer: True
  - Choices: True; False
- Question 1.2: Which string function converts the string to lower case?
  - Type: Multiple choice (single correct response)
  - Answer: lower()
  - Choices: lower(); upper(); islower(); split()
- Question 1.3: Which string function splits the string to a list of words?
  - Type: Multiple choice (single correct response)
  - Answer: split()
  - Choices: lower(); upper(); islower(); split()

- Question 2.1: Which module is stopword defined in?
  - Type: Multiple choice (single correct response)
  - Answer: nltk.corpus
  - Choices: nltk.corpus; nltk.stem; sklearn.feature_extraction.text
- Question 2.1: Which module is PotterStemmer defined in?
  - Type: Multiple choice (single correct response)
  - Answer: nltk.stem
  - Choices: nltk.corpus; nltk.stem; sklearn.feature_extraction.text

- Question 3.1: What does each row in a document term matrix represent?
  - Type: Multiple choice (single correct response)
  - Answer: a piece of text
  - Choices: a piece of text; a single word;
- Question 3.2: A column name in a document term matrix is a:?
  - Type: Multiple choice (single correct response)
  - Answer: token; paragraph of text;
  - Choices: token; paragraph of text
- Question 3.3: True or False? Most elements in a document term matrix are 0.
  - Type: Multiple choice (single correct response)
  - Answer: True
  - Choices: True; False
- Question 4.1: Which module is CountVectorizer defined in?
  - Type: Multiple choice (single correct response)
  - Answer: sklearn.feature_extraction.text
  - Choices: nltk.corpus; nltk.stem; sklearn.feature_extraction.text
- Question 4.2: Which module is TfidfVectorizer defined in?
  - Type: Multiple choice (single correct response)
  - Answer: sklearn.feature_extraction.text
  - Choices: nltk.corpus; nltk.stem; sklearn.feature_extraction.text
- Question 5.1: If word A and word B appear for same times in a piece of text T, but word A appears more than word B in the whole corpus. How do the frequencies of word A and B for the text T compare in a document term matrix created by CountVectorizer?
  - Type: Multiple choice (single correct response)
  - Answer: Same
  - Choices: Same; Frequency of A is greater than B; Frequency of A is less than B
- Question 5.2: If word A and word B appear for same times in a piece of text T, but word A appears more than word B in the whole corpus. How do the frequencies of word A and B for the text T compare in a document term matrix created by TfidfVectorizer?
  - Type: Multiple choice (single correct response)
  - Answer: Frequency of A is less than B
  - Choices: Same; Frequency of A is greater than B; Frequency of A is less than B

# Lesson 2:

- Question 6.1: Trur of False? Bayes Theorem describes the probability of an event, based on prior knowledge of conditions that might be related to the event.
  - Type: Multiple choice (multiple correct response)
  - Answer: True
  - Choices: True; False
- Question 6.2: Which module is MultinomialNB defined in?
  - Type: Multiple choice (multiple correct response)
  - Answer: sklearn.naive_bayes
  - Choices: sklearn.naive_bayes; nltk.naive_bayes

- Question 7.1: Which text data set is a CountVectorizer object fit on?
  - Type: Multiple choice (single correct response)
  - Answer: training text data
  - Choices: training text data; testing text data; both training and texting data
- Question 7.2: Which text data set is a TfidfVectorizer object fit on?
  - Type: Multiple choice (single correct response)
  - Answer: training text data
  - Choices: training text data; testing text data; both training and texting data

# Lesson 3:
- Question 8.1: True or False? You can define your own stopword list for a text classification.
  - Type: Multiple choice (single correct response)
  - Answer: True
  - Choices: True, False  
- Question 8.2: True or False? Applying stopword always improves the classification accuracy.
  - Type: Multiple choice (single correct response)
  - Answer: False
  - Choices: True, False  

- Question 9.1: True or False? Applying n-grams INCREASES number of columns in a document term matrix.
  - Type: Multiple choice (single correct response)
  - Answer: True
  - Choices: True, False  
- Question 9.2: True or False? Applying n-grams may improve classification accuracy but it will slow down the training process.
  - Type: Multiple choice (single correct response)
  - Answer: True
  - Choices: True, False  

- Question 10.1: True or False? Sentiment Analysis is an application of text classification.
  - Type: Multiple choice (single correct response)
  - Answer: True
  - Choices: True, False  
- Question 10.2: True or False? Applying stemming in text classification will shorten the training time?
  - Type: Multiple choice (single correct response)
  - Answer: False
  - Choices: True, False  
