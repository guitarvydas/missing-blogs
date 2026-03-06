# 2022-10-19-REGEX Cryptic


# Original Email
from: mike.austin.1024@gmail.com
subject: [PiLuD] Sometimes the API is just right

```
"{name}: {age}"

str.replace(/\{(\w*)\}/g, (_, p) => env[p])

This will replace all occurrences of {var} with the environment (scoped) value. I remember in the past doing this in a loop or reduce(), but it really can be done in just one function. Is the regex cryptic? Maybe, but it's very small.
```
# My Comments
FWIW, I like this, but, agree that REGEXPs can be cryptic.  Looking at this in 4 dimensions:
1. Human readable - No
2. Human writeable - Yes
3. Machine readable - No
4. Machine writeable - No