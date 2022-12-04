# Time Translator

**Time Translator is a Python UI tool to convert static amount of time into a better shape.** It can convert hours to weeks, or even seconds to months.

## Examples of uses
We will use 3 situations where we can convert a certain amount of time into a better-looking sentence.

- 52 hours : 2 days and 4 hours               
![Snipaste_2022-12-04_12-02-08](https://user-images.githubusercontent.com/66722031/205504753-6dc5cb46-1505-4fba-a75c-46978479b4bb.png)


- 200 seconds : 3 minutes and 20 seconds      
![Snipaste_2022-12-04_12-02-34](https://user-images.githubusercontent.com/66722031/205504748-1b8cca3c-7c94-468a-9711-b2cd9320f82c.png)


- 98504 seconds : 1 day, 3 hours, 21 minutes and 44 seconds
![Snipaste_2022-12-04_12-04-29](https://user-images.githubusercontent.com/66722031/205504858-e54570a7-ef44-4b49-8a06-396ae0a8eabf.png)


## How to use

You can indicate your time with this format to convert it : **[Number] [Type]**

[Number] represents your time, for example, 500 in 500 seconds.
[Type] represents the type of time. Here is a list of the different types the program can deal with :
- S for seconds
- Min for minutes
- H for hours
- D for days
- W for weeks
- M for months

Examples : 
- 80H -> 80 hours 
- 9Min -> 9 minutes
- 61W -> 61 weeks 
- 870S -> 870 seconds

After using it once, the program will automatically ask for a new input, without deleting the past outputs.
