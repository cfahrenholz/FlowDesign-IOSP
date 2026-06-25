Fragen und Diskussion eines Entwicklers mit Ralf Westphal zu IODA und IOSP, PoMO.
Developer:
I am still trying to understand how all the concepts of IODA, IOSP fit together. I have read all the articles and your flow design book.
But this seems like violating PoMO and to loosen the IOSP?
And if you introduce the library calls in your operation code/functions don´t you introduce functional dependencies? But I guess your argument against this is, that the library code is a well tested black box which you do not count as functional dependency then?
I think you also introduce complexity, especially for testing when you need to instantiate and inject the library components.
And if the library code is behind a contract and you mock the implementation you loose the benefits of IOSP.
So I guess to solve all my concerns, the solution is to call to the library on the integration method above the operation and just pass then the data to the operation.
I am little bit confused :(
Ralf Westphal:
The PoMO was at the beginning, before IOSP. The IOSP is actually helping to implement the PoMO: thru integration the integrated functional units can be oblivious of each other.
Over time, though, the PoMO moved into the background. The IOSP is simpler to explain.
Calls to libraries are logic. Whether that's calls to standard libraries, 3rd party libraries or even operators of a programming language. Also calls to libraries you write yourself but treat as black boxes are considered logic.
The point is: Logic is what you take as being correct in itself. But you need to test its usage, ie. the composition of different parts of logic.
Because it needs to be tested, logic should be confined to operations. Logic should not itself be functional dependent on other logic.
Injection introduces complexity. It cannot be avoided, but should be done only as much as really necessary.
> So I guess to solve all my concerns, the solution is to call to the library on the integration method above the operation and just pass then the data to the operation.
I disagree! A library call is a matter of an operation. That's crucial!
The integration then integrates this operation with other functional units (operations or yet more integrations).
Developer:
Thanks for taking time to answer!
> Calls to libraries are logic.
Does this mean when I do a call to another software cell, this call is always considered as logic and must reside in an operation? So calls to other software cells should not happen from integration methods?
> Because it needs to be tested, logic should be confined to operations. Logic should not itself be functional dependent on other logic.
If I understand this right, you mean logic should not itself be functional dependent on other (non binary) logic of my own codebase, correct?
>I disagree! A library call is a matter of an operation. That's crucial!
Ok. But also here the question, when I do a call to another software cell, should these calls then typically done within operations from Providers that I implement or can these calls made directly from my (domain) operation?
Ralf Westphal:
> Does this mean when I do a call to another software cell, this call is always considered as logic
What is this call? Only the API function call does actually call the other software cell, a fetch() in Typescript. The function containing this called must be an operation.
> logic should not itself be functional dependent on other (non binary) logic of my own codebase, correct?
Yes.
(What does non-binary mean?)
But: This does not scale. Hence you can wrap logic in your own libraries/packets/componets. Put it in an arbitrarily deep hierarchy of integrations and operations. And still you can call the top integration function as logic in a operation in a calling library. You just need to treat your own code as a black box.
> should these calls then typically done within operations
Always. Only. A fetch() is logic.
> done within operations from Providers that I implement or can these calls made directly from my (domain) operation
Correct. Providers are operational modules.
Developer:
I appreciate your answers! They help me to get a better understanding of the topic.
>What is this call? Only the API function call does actually call the other software cell, a fetch() in Typescript.
In my case (.NET Desktop) I was thinking of calling a library that is a component (something like a manager or service component) that I would have seen as a software cell. But maybe such a component is not what you would consider as a software cell because in my case it is not hosted in a separate process or cloud or container service?
>What does non-binary mean?
The C# source code (files) of my Visual Studio solution, so code that I do not reference from binaries (assemblies, nuget packages).
>But: This does not scale.
I am not 100% sure what you mean by "this does not scale", but I guess you mentioned something similar in your IODA dotnetPro update 2020. Where you say someting like this: In IOSP < 2.0 it was not possible to call integration methods from operations but when your code base grows you could achieve this by modularizing/aggreagte the code to be called into a (binary, e.g. nuget) package.
Ralf Westphal:
> is not what you would consider as a software cell because in my case it is not hosted in a separate process or cloud or container service
Correct! Software cells are running at least on their own thread. Usually in their own process.
> non-binary
Non-binary to me never is a library, package or component. It's always part of a solution in VS. Therefore it's under your immediate control. It's a white box. It cannot be used in operations.
> but when your code base grows you could achieve this by modularizing/aggreagte the code to be called into a (binary, e.g. nuget) package.
Correct.