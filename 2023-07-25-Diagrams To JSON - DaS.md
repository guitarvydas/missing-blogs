# 2023-07-25-Diagrams To JSON - DaSstrin# Diagrams To JSON - DaS
"DaS" means Diagrams as Syntax.

In this essay, I describe what a simple diagram of program, written in draw.io, looks like when transpiled to JSON.

The repo for working code is listed in the appendix.
## Diagram
![](images/simple%20example.drawio.svg)

`make run` runs the Odin diagram compiler and executes the resulting code.  

In the process, the JSON for the input diagram ("example.drawio") is dumped to the terminal.

The text `Yield` is discarded and the box-and-arrows are converted to JSON as below.

Each `tab` in the diagram is treated as a Container.

The rectangles (blue) represent Component instances (Leaf or Container).  

The rounded rectangles on the boxes represent ports.  White ports are inputs and the green-blue-gray ports are outputs.

Rhombuses represent ports of the Container being described by the diagram.  White rhombuses represent inputs to the Container.  Blue rhombuses represent outputs from the Container.

Components are concurrent and completely isolated from one another (i.e. 0D).  The only way in which information can travel on this diagram is via port-to-port messages, represented as one-way arrows on the diagram.

Each Component instance is described by a blue rectangle representing a Component *prototype*.  Each *prototype* consists of a *name* and some *ports*.

Arrows represent one-way *Connections*.  Connections must be drawn only between ports.

At a technical level, there are 4 kinds of *connections*.  These kinds are fairly obvious to human readers, but, must be described in detail to machines.  The details are listed in the Appendix.


### What Happens Next

*[This section is not directly related to the JSON format of a diagram, but, might give context for why things are the way they are.]*

The programmer uses the Odin0D kernel and calls `reg.make_component_registry(leaves, "example.drawio")` to parse the diagram.

`make_component_registry` calls the Odin code for parsing the diagram, then assembles a *registry* of prototype components and returns that registry.

The programmer must supply a list of Leaf prototypes to `make_component_registry`. In this simple example, there are only 2 Leaf prototypes
1. Echo
2. Sleep

## JSON

The generated JSON contains the filename, tabname, children and connections for each Container specified in the diagram.

*Children* is a JSON list of {name X internal_ID} pairs.

*Connections* is a JSON list of connection triplets
1. direction
2. source
3. target.

Direction is
- 0 for Down
- 1 for Across
- 2 for Up

See the Appendix for the meaning of these directions.

Source is:
- Component Instance
- Port

Target is:
- Component Instance
- Port

A Component Instance is:
- name of the prototype Component
- an internal ID, which must be unique with respect to all other IDs used on the diagram.

In the current implementation, a *name* is a JSON string, an ID is a JSON integer, and, a Port is a JSON string.  

In this implementation, we use the JSON names "source_port" and "target_port" to differentiate the purpose of the port strings and list the ports separately from the Source and Target fields.

This is probably unnecessary, "port" should be enough and ports should be included in the "source" and "target" descriptors, but, this differentiation is historical. What is conceptually a triplet is currently, for historical reasons, a quintuplet {direction, source, source_port, target, target_port}.

### Child
*Sample*
```
{
    "name": "Echo", 
    "id": 2
}, 
```

### Connection
*Sample*
```
{
    "dir": 0, 
    "source": {
        "name": "", 
        "id": 0
    }, 
    "source_port": "yield", 
    "target": {
        "name": "Echo", 
        "id": 2
    }, 
    "target_port": "input"
}, 
```

### The Whole Shebang
```
[
    {
        "file": "example.drawio", 
        "name": "main", 
        "children": [
            {
                "name": "Echo", 
                "id": 2
            }, 
            {
                "name": "Sleep", 
                "id": 6
            }, 
            {
                "name": "Echo", 
                "id": 9
            }
        ], 
        "connections": [
            {
                "dir": 0, 
                "source": {
                    "name": "", 
                    "id": 0
                }, 
                "source_port": "yield", 
                "target": {
                    "name": "Echo", 
                    "id": 2
                }, 
                "target_port": "input"
            }, 
            {
                "dir": 0, 
                "source": {
                    "name": "", 
                    "id": 0
                }, 
                "source_port": "yield", 
                "target": {
                    "name": "Sleep", 
                    "id": 6
                }, 
                "target_port": "wait"
            }, 
            {
                "dir": 1, 
                "source": {
                    "name": "Sleep", 
                    "id": 6
                }, 
                "source_port": "output", 
                "target": {
                    "name": "Echo", 
                    "id": 9
                }, 
                "target_port": "input"
            }, 
            {
                "dir": 2, 
                "source": {
                    "name": "Echo", 
                    "id": 9
                }, 
                "source_port": "output", 
                "target": {
                    "name": "", 
                    "id": 0
                }, 
                "target_port": "output"
            }, 
            {
                "dir": 2, 
                "source": {
                    "name": "Echo", 
                    "id": 2
                }, 
                "source_port": "output", 
                "target": {
                    "name": "", 
                    "id": 0
                }, 
                "target_port": "output"
            }
        ]
    }
]
```

## Appendix - Code Repo
The example comes from working code in the repo https://github.com/guitarvydas/odin0d/tree/dissectdiagram

`make run` runs a stunted example and outputs only the `yield` case.  The Sequential Routing and Parallel Routing examples have been deleted.  They produce empty outputs `[]`

```
...
               }, 
             "target_port": "output"
            }
        ]
    }
]
--- Diagram: Sequential Routing ---
[]
--- Diagram: Parallel Routing ---
[]
--- Diagram: Yield ---
Echo (ID:5) / input = Hello Yield!
Sleep (ID:3) / wait = Hello Yield!
Echo (ID:6) / input = Hello Yield!
[{output, Hello Yield!}, {output, Hello Yield!}]```
```

## Appendix - Connection Kinds

1. Down
2. Up
3. Across
4. Through

### NC - No Connection
At this low level, NC - No Connection - is not represented explicitly.  The lack of a connection is enough - at this level.

A "type checker" might wish to check if the programmer really wanted to leave a port unconnected.  For this purpose - checking programming intent - a type checker might wish to add more kinds of connections:

5. NC_out
6. NC_in
