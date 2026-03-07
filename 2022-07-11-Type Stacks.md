# 2022-07-11-Type Stacks# Type Stacks
- progressive type checking
- pipeline of type checkers
- input to pipeline is general and loosey-goosey
- output of pipeline is specific and checked
- each stage in the pipeline checks 1 kind of detail and passes the data on, or, sends an Error message
- compose type checker chain using smaller blocks
- no need to *abort*, just don't send data on to the next stage in case of error



![type stacks.png](images/type stacks.png)