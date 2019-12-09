#Open, reading, writing files and error handling 

Topics Covered:
- open()
- try & except
- with & finally 
- exceptions and error handling 

    ``
    All that can go wrong, will go wrong - Mr Murphy 
    ``
 ## Error Handling 
 Assuming things will break and handling your errors when they do, providing adequate feedback whilst failing with grace
 
 When you handle errors your code can continue to run. (Which is a good thing)
 
 
 ## Definitions:
 
 ### try: / except: / finally:
 These blocks of code are used in conjunction to error handling 
 
    ``
    try:
        (block of code)
        (block of code)
    except <error you want to accept > as <alias/ palceholder>:
        (block of code)
        (block of code)
     
    finally:
       block that runs after so maybe a print
     
    ``
 ## Using open() and with()
 When using open() you need to close the files you actually open 
 
  - you can skip this step using 'with:'
    ``
     with open() as <placeholder>:
     <placeholder>:
        <placeholder>.readlines()
    ``
 
 ### Exceptions
 These occur when an error occurs 