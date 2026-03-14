# 2022-07-27-Structured Message Passing
---
tags: 
copied_to_pages: "true"

---

---
# Structured Message Passing
video: [Structured Message Passing](https://share.descript.com/view/pDyKpgerYRq)

---
# Structured Message Passing

"Structured message passing" implies that we must encapsulate every aspect of Components

- data flow

and 

- control-flow

---
# Scalability
Scalability comes from Structured message passing 

You can only scale a system where Components are not tangled together.

---

# Existing Languages
   - simply stop using hardware-supported CALL / RETURN for communication between Components
   - create 2 classes of Components

---

# Don't Use CALL/RETURN
- Don't use hardware-supported CALL/RETURN for communications between Components

- use FIFOs instead

- it's OK to use CALL/RETURN for code *inside* a component, but not as a means for communicating between Components

---

# 2 classes of Components
- Leaf Components (code)
- Container Components (routers)

---

Structured message passing implies that we must encapsulate every aspect of components.

That includes data flow and control flow.

We can't just concentrate on data flow.

Scalability comes from structured message passing.

You can only scale a system when components are not tangled together.

How do you do this using existing languages? Simply stop using hardware supported call return for communication between components. And create two classes of components, not one class.

So, how do you not use call return? It's simple. Just use FIFOs.

It's okay to continue using call return for code inside a component. But don't use call return as a way of communicating between components.

Creating two classes of components. I see there being leaf components for code and container components for routers that compose components and route messages between them, but they don't actually do anything.They can run other components.

Container components devolve into other container components or leaf components.  Stepping means we finally get down to a leaf and a leaf just does something and stops.