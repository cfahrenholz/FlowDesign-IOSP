<!-- Page 1 of 39 -->


IODA
Architecture
Model
DECOUPLING CONCERNS EVEN MORE BY GET TING RID OF
F UNCTIONAL DEPENDENCIES


---


<!-- Page 2 of 39 -->


Agenda
• Identifying Problems/Critics of Common Architecture Models
• Monolith code example
• Trying to solve with layers
• Decoupling of layers
• Layers in shells
• IODA Architecture Model
13/11/2023
2


---


<!-- Page 3 of 39 -->


Code Example - Requirements
Write a program that
• Counts all words in a text
• Counts all distinct words
• Consider a stop word list (separate file to exclude words)
• Read text from user input or file
• Use the file name as a program argument
Just a simple example that has some user interface (console), business logic and data access
Do you already have a basic code, architecture, or system design in mind?
13/11/2023 3


---


<!-- Page 4 of 39 -->


In the beginning there was the Monolith without Structure
• It is functional correct
• Understandable? Why Not?
• Testable?
Can you identify all the
responsibilities?
Note: Regex checks if it is an alphanumeric word including dash.
13/11/2023 4


---


<!-- Page 5 of 39 -->


Mixed / Confused Responsibilities
13/11/2023 5


---


<!-- Page 6 of 39 -->


Splitting up the Monolith in Layers – Layered Architecture
Improved:
• Understandability
• Clarity of responsibilities and relations
13/11/2023 6


---


<!-- Page 7 of 39 -->


Splitting up the Monolith in Layers – Layered Architecture
The rough responsibilities are
basically nicely separated
Dependencies neatly aligned
But actual business logic is still
not easy to test
Functional Dependency exists:
BL calls other logic from DAL
13/11/2023 7


---


<!-- Page 8 of 39 -->


Decoupling of Layers
• DIP – Dependency Inversion Principle
• High-level modules should not depend on low-level
modules. Both should depend on abstractions.
• Abstractions should not depend on details. Details
should depend on abstractions.
Trick: Split compile/design time
• Enables focused testing of a layer
dependency from runtime dependency
without DIP with DIP
13/11/2023 8


---


<!-- Page 9 of 39 -->


Decoupling of Layers
Layered Architecture with DIP Interfaces are decoupling layers
13/11/2023 9


---


<!-- Page 10 of 39 -->


Decoupling of Layers
• Inversion of Control – IoC
• Inject concrete dependency during runtime
• Diagram not so easy anymore
• With DIP dependencies are different
during compile time and runtime
• Additional artifacts -> Interfaces
• Functional Dependency still exists
=> Complexity increased for testability
13/11/2023 10


---


<!-- Page 11 of 39 -->


Why…?
• … should the BL depend on the DAL?
• … should the BL know how to load and save data?
• … should the BL be responsible to control the data access?
=> There seems to be some confusion of responsibilities!?
13/11/2023 11


---


<!-- Page 12 of 39 -->


Layers in Shells – To the Rescue?
• In 2005 the industry realized there is
something wrong
• Concentric architecture patterns came up
• Hexagonal Architecture (HA)
• Onion Architecture (OA)
• Clean Architecture (CA)
from Robert C. Martin Clean Code Author
• Try a different organization of
responsibilities; different kinds
• Core differs from
outer parts of the software
• Still clear direction of
dependencies like in Layered
Architecture
13/11/2023 12


---


<!-- Page 13 of 39 -->


Layers in Shells – Problems solved?
• Dependencies direction from
outside -> inside
• BL does not control the DAL, it seems so
• The further out a shell, the more
• it deals with technical/peripheral details
• volatile it is
• The further inside a responsibility, the more
• central it is
• timeless, constant and quiet it is
• increases the policies/rules
-> sounds good
• increases the abstraction
-> good idea?
13/11/2023 13


---


<!-- Page 14 of 39 -->


Layers in Shells - Clean Architecture (CA)
• Adapters
• Outer shell
• Hardware/Resources access (keyboard, display, hard disk, network, …)
• Presentation Layer Logic is now split
• Controller: delegates user actions to Use Cases shell
• Presenter: used by Use Cases shell to display results
• Use Cases
• Shell between core/domain and outer shell
• Orchestrate the flow of data to and from the domain
• Defines it`s (compile time) dependencies as abstractions to access data (ITexts)
and UI (IPresenter)
• Domain
• Core
• Entities, Services
• Defines it`s (compile time) dependency as abstraction to access data (IStopwords)
13/11/2023 14


---


<!-- Page 15 of 39 -->


Layers in Shells - Clean Architecture (CA) – Clean?
Orchestration in Use Case
• Retrieve data from Controller, call BL, display results
• CA requirement satisfied -> compile time
dependencies point from outside to inside!
• At runtime…?
(see later)
• Maybe Complex?
13/11/2023 15


---


<!-- Page 16 of 39 -->


Layers in Shells - Clean Architecture (CA) – Clean?
•
Functional dependency still exists
• logic from DAL located in logic from BL
•
CA requirement satisfied -> compile time dependencies
point from outside to inside!
•
But at run time: call from an inner shell to outer shell
•
Compared to Layered Architecture:
• 5 classes instead of 3
• 5 interfaces instead of 3, must be defined on two levels
• Core
• Use Case shell
Robert C. Martin
=> The price for clean architecture is
complexity? Really?
Dependencies clean and decoupled with DIP
13/11/2023 16


---


<!-- Page 17 of 39 -->


Layers in Shells - Clean Architecture (CA) – Clean?
•
At design time the dependencies looked cleanly aligned
• But the truth at runtime is inner shells are depending on
outer shells
Conclusion:
•
Good:
• stable rules and policies in the inner core
• volatility / communication with outside world is located
at the outer shells
•
Bad:
• too much focus on compile time -> complexity
• more artefacts (interfaces, classes, files)
• testing more complex (setup mocks, injection)
13/11/2023 17


---


<!-- Page 18 of 39 -->


The IODA Architecture Model
13/11/2023 18


---


<!-- Page 19 of 39 -->


Goals for an improved Architecture Pattern
• Keep the advantages from previous patterns
• Have defined default responsibilities, and to be able to separate them
• Improve understandability and testability
• Awareness of cleanly directed dependencies
• Fix the disadvantages from previous patterns
• Avoid functional dependencies that are hard to test
• Avoid additional complexity because of decoupling efforts
13/11/2023 19


---


<!-- Page 20 of 39 -->


Functional Dependencies - The Elephant in the Room
If in a function,
LOGIC and calls to other functions of your sources are co-
located / mixed in the same function, then that’s a
FUNCTIONAL DEPENDENCY.
When a Mock is required to test LOGIC of your codebase.
What is LOGIC?
• Code where the action happens
• Creates software behavior for the user
(Customer don´t care about code
structure, comments, whitespace or variable declarations or function definitions or classes)
• Transformations / Operators: <, ++, -
• Control structures: if-else, for, try-catch
• I/O or general API-Calls: Console.Write(), File.OpenRead()
• Another definition: Functions in binary form (black box)
• Operators of your programming language
• 3rd party packages
• Package references of your software project
(not DLLs/csproj, since that
source code is near and could easily create FDs, but Packages need some effort to test and
build, changes much less, is more stable and versioned)
13/11/2023 20


---


<!-- Page 21 of 39 -->


Functional Dependencies – Todays State of the Art?
Switching between logic and function calls
• Each LOGIC easy testable?
• DIP and mocks to the rescue?
• Effort for new Interface
• Effort to code + configure the mock
• Inject mock (IoC)
• Increased complexity
• When test fails, in which part of the LOGIC blocks?
Or maybe an error in the mock?
FDs contradict clean SW-Development
• Hurts SRP
• Create behavior via Operations in LOGIC
• Integration of other functions
• Hurts SLA
• By nature, logic is on a lower abstraction level
than function calls
• => Bad understandability
=> The classic architecture models do not address this problem
13/11/2023 21


---


<!-- Page 22 of 39 -->


Functional Dependencies – Formal Responsibilities / Testability
• Extract method does not help
• Just deepens the logic
• Harder debugging sessions
• Harder to see how behavior is produced
• At least n + 2 responsibilities
(formal code structure, not regarding content)
• n: the number of FDs
-> Logic before each call (g, h)
• +1: Logic after last call
• +1: Integration of function calls
• Testability
• Depends on number of FDs
• The more responsibilities, the more difficult to test
• Testability = 1 / Number of Responsibilities
• 1 is best
• Near 0 is difficult
13/11/2023 22


---


<!-- Page 23 of 39 -->


Functional Dependencies
• Common/classic architecture models
• Functions are not a concern. They are all from the same kind.
• Logic is not a concern
• Have hybrid functions with two responsibilities (mix of operation
(logic) and integration), only a few operations at bottom
• Always hard to test. DIP/IoC do not help.
13/11/2023 23


---


<!-- Page 24 of 39 -->


New Architecture Pattern - Resolve Functional Dependencies
• Of course, functions are needed and are necessary to resolve FDs
• Operations
• Functions just containing logic
• Do not call other functions you can easily access of your own source code base
• A function composed only of calls to functions in another code base
• BCL (File.ReadAllLines, Console, …)
• Code elements of your programming language (for, if, ++, …)
• Blackbox code -> Binaries (DLLs, Packages, …)
• The leaves of the function call tree
IOSP:
• No FD
Integration
• Easy to test
Operation
Segregation
• Integrations
Principle
• Functions without logic
• Integrate calls to other Integrations or Operations
• No FD
• Often the integration code is easy to understand, less tests required
• Only a few integration tests on the top level code necessary
• Less mocks or maybe without any mocks
13/11/2023 24


---


<!-- Page 25 of 39 -->


New Architecture Pattern – Connect Operations
• Another problem in the common architecture models
• No place for DATA
• Not visible in the shells, layers
• Data should be explicitly addressed
• How do Operations interact/communicate when they do not know each other?
• Operations depend on DATA, either
• DATA flows between them via their parent Integrations
• or they share state (not flowing)
• Data structures / classes
• Without methods -> No FD
• Data classes can have Operations
• Only Operations for data access & consistency
• E. g. Stack, Queue, see also IODA sample (slide 33)
• This is not a problematic FD when accessed by Operations
13/11/2023 25


---


<!-- Page 26 of 39 -->


New Architecture Pattern – Connection to the Environment
• Communication with the outside world is another special • A new architecture pattern should also highlight the
aspect the concentric architectures have improved compared access to the environment and make the separation clear
to the layer models
• Easy in a call hierarchy without FDs
• I/O-Operations, API calls to libs, frameworks, external
• API calls are considered as logic -> Operations
systems/services
• Problematic for tests • Dependencies to black “fundament”/APIs only in red
Operations
• Performance
• Effort to code
• External libs may change or may be replaced
• DIP/IoC help in such situations
• Isolate these API calls in just a few code fragments
• Concentric architectures locate this aspect at the outer shell
• Adapter in Hexagonal Architecture
• Controller, Gateways, Presenter in Clean Architecture
13/11/2023 26


---


<!-- Page 27 of 39 -->


IODA – A new Architecture Pattern
• Generic architecture for all kinds of software systems
(Games, CRM, industrial SW, …)
• initially no content-related responsibilities (as it is the case in
the common patterns – Domain, Presenter, Gateway…), only
formal on the 4 levels
• Defines how code should be structured
• Focus on Functions, behavior of the software, transform
data
• Improves Understandability (Integration code easier to read)
• Improves Testability (Operations have less dependencies)
13/11/2023 27


---


<!-- Page 28 of 39 -->


IODA – Software Cell and Content related Responsibilities
• Software Cell:
• Concentric Software System
• Membrane: The border to the environment (black outer circle)
• Core: Domain
• Code you write is the membrane, the core and code between
both
• Fundamental responsibilities
• At the black outer circle / boundaries of the system
• Category: Adapters (blue squares, green triangles)
• Adapter
• Encapsulates: IO-logic, other API calls (libs)
• Connects the environment (users, other software cells/systems)
• Portals and Providers
• Via Portals the system is accessed by the environment
• Users/Other systems trigger actions and provide input data
• Returns output data
• Via Providers the system access the resources it depends
on the environment
• No FDs!
13/11/2023 28


---


<!-- Page 29 of 39 -->


IODA – 2-Dimensional Architecture
• Fundamental structure/dimension
(at the bottom)
• Enables: No FDs in the above dimension
• Hierarchy of modules/functions
• Formal responsibilities (Integration, Operation)
• Defines how the code is organized
• Recursive: Pattern repeats in all parts of the software
• Software Cell
• Defines system architecture
• Content-related responsibilities
• Distinction between formal- and content-related
responsibilities
13/11/2023 29


---


<!-- Page 30 of 39 -->


IODA - Sample
• Adapters
• Encapsulate APIs in portals and providers
• Commandline: Handles “API” string[] args
• UI: Communication with User via standard-Input/-Output
• Data
• Connects Operations (see previous slides)
• IODA architecture enforces to consider it
• WordCountResult
• Entry points
• Controller (Application)
• Integrates Portal with the top-level/main Integrations
(Processors)
• No aspect in the common architecture models
• What´s missing?
• Interfaces (of course needed, maybe in adapters, but less)
• No/less DIP, less complexity, runtime vs compile time
• IoC: Maybe to replace adapters in Integration tests
13/11/2023 30


---


<!-- Page 31 of 39 -->


IODA - Sample
• Object initialization
• IoC prepares for a potential DIP that may be
necessary later
• Could be done in separate Construction class, if
needed with IoC-Container
• Controller / Application
• Just integration
– app.Run
• UI
• Has no interface from the beginning
• Could be added if needed
• IODA model does not enforce abstraction with
DIP as CA is doing it upfront. Grows with
requirements
13/11/2023 31


---


<!-- Page 32 of 39 -->


IODA - Sample
• Just Integration
• Composition of multiple parts
• Creates abstraction on the higher
functions/modules
• IODA approach is
• Function-first (data flow first)
• Composition-first
• Aggregation-second: categorization via
classes/modules in second step to organize
functions
• When app grows, Integrations can be moved easily
to other classes
• No logic
• How to avoid logic in Integration code?
• Continuations / Delegates (see yellow parts)
• Logic in Operations easier testable (no FDs)
13/11/2023 32


---


<!-- Page 33 of 39 -->


IODA - Sample
ShredderedText
•
• Data class
• Connects Operations
(Shred and Filter)
• Also contains Operations
•
When called by other Operations -> no problematic FD
•
No need to mock such classes in tests
•
Still easy to understand, no additional complexity
•
Can be used sometimes to move logic to data class to avoid
mix of integration and logic code
What else to see?
•
• BL is static. Why?
• No signal for instance methods
•
No common state
•
No API calls e. g. to data access like in other models, nothing
to mock in this case
• Easy to test the logic
• Improved understandability (no instantiation, no
shared state)
• No interface necessary
(maybe in future)
13/11/2023 33


---


<!-- Page 34 of 39 -->


IODA Structure - Functions
• Green functions
• without logic
• Referencing other functions
• Red functions
• Logic
• Leaves
• No outgoing arrows / no references to the sources
of your solution
• Typically
• Integrations compose 3-5 functions
• When growing -> compose new Integration and
push the others to it on a lower level
• Sometimes the opposite needed – lift lower
methods up and remove their previous Integration
• When logic in Operation needs to be extracted the
original Operation becomes an Integration ->
“Refactoring to IOSP”
13/11/2023 34


---


<!-- Page 35 of 39 -->


IODA Structure - Classes
• Green classes
• Integration character / less or no logic
• Referencing other classes
• Red classes
• Logic
• BL discrepancy? Mix of Integration and Operation
• More Operational character
(see Sample Count_words on previous slide)
• Purple class
• Data
• IODA architecture model is recursive
• Operation can call other Integration when in binary
format (package reference see slide FD)
• Or Integration calls other Integration which integrates
Operations
13/11/2023 35


---


<!-- Page 36 of 39 -->


Special Integration Patterns
Rough process of creating behavior and data flow
•
Portal receives data from environment
•
Additional data may be collected from Provider
•
Domain is processing the data and storing it via Provider
•
Environment gets data presented
•
NOTE: Functions do not know each other
• Interactor variations
Integration needed
•
• Application (Desktop app)
Provider and Domain Core are the “work horses”
•
• Controller (Web)
Portal collects / projects data
• • Processor
Integration needed -> Interactor
• But Interactor not testable (dependency to Portal: UI, web framework) • The heart of IODA
•
Acceptance tests can start here
•
No UI/web framework dependencies
•
Can be reused in any other application
13/11/2023 36


---


<!-- Page 37 of 39 -->


Finally - Sleepy Hollow Architecture
Head
•
• Integrates Portal and Body via Application
Body
•
• Integrates the Domain core and Providers via
Processors
Head and Body can be hosted in different
•
threads, processes
13/11/2023 37


---


<!-- Page 38 of 39 -->


Summary
• Keeps the advantages and removes the disadvantages from the concentric architecture models
• Software Cell
• Detect and locate default responsibilities (Adapters)
• Identify environment communication
• Protect the domain core from dependencies on peripheral aspects, e. g. 3rd party libs, IO-technologies (UI, DB, network, file
access,…)
• Design-time and runtime relationships are different
• IOSP: Avoid FDs to improve changeability and testability
• Reduce complexity of DIP / IoC, less interfaces, only used where necessary
• Data gets visible in the model
• Categorization of software modules / classes arise naturally
• not upfront
• functions and compositions first (compose/integrate functions to create new behavior)
• aggregation second (organize similar things together)
• Can be used as a basic model in any software
• Even in brown field it can help
• Use IODA structure as a target or NorthStar for refactoring and new features
13/11/2023 38


---


<!-- Page 39 of 39 -->


Links / Resources
Slides based on blogs, publications and articles by Ralf Westphal (Coach, Consultant, Speaker in
•
Germany/Bulgaria)
• “Die IODA Architektur im Vergleich”-Update 2020 (dnp dotnetpro magazine 2018-2020)
• https://www.dotnetpro.de/hefte_data_1550430.html
• https://www.dotnetpro.de/hefte_data_1557946.html
• https://www.dotnetpro.de/hefte_data_1579489.html
• Book http://leanpub.com/ioda-architektur-im-vergleich-dnp
• Related books
•
Test-first Codierung - Programming with Ease - Teil 1
•
Softwareentwurf mit Flow-Design - Programming with Ease - Teil 2
• English content
•
https://ralfwestphal.substack.com/p/ioda-architecture
•
Sleepy Hollow Architecture - No application should be without it - ralfw-de
•
https://ralfwestphal.substack.com/s/clean-code-development
• https://ralfwestphal.substack.com/p/iosp-20
• https://ralfwestphal.substack.com/p/functional-dependencies
• https://github.com/ralfw/architecture-variations
•
Terminus Architecture - ralfw-de
Other resources with similar approach
•
• A-Frame Architecture
13/11/2023 39