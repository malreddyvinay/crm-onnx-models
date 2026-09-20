APIs make the digital world go round. According to Gartner, they are an essential element of every digital strategy. They enable systems and applications to interact, connecting disparate data sources and bridging access protocols. APIs can unlock your organisation’s digital assets and allow them to be consumed in a controlled manner.

However, simply exposing your systems and enterprise applications via an API layer presents some formidable challenges, for example:

- How do you shield your backend systems from being overrun with numerous requests?
- How do you avoid an unmanageable mess of tightly-coupled point-to-point connections?
- How do you ensure that consumers only have access to the data they should?

The answer may be a **Digital Integration Hub (DIH)**.

#### The Problem with a Traditional API Integration Architecture

Modern enterprises will typically have invested in a well-conceived integration architecture for their APIs, introducing multiple layers that serve the data through a request-based integration layer:

*Image from* *"Turbocharge Your API Platform with a Digital Integration Hub – Gartner (G00360082, Jul 2018)*

The primary role of the integration platform is to field requests from the APIs and deliver data from the source systems. Depending on the complexity of the systems, the underlying data structures, and the expected load from the API consumers, this solution may work reasonably well. 

The problem is that even though the integration layer abstracts the underlying systems from the consumers, there is still a degree of coupling:

- Backend systems ultimately bear the burden of responding to API requests – even if asynchronously. 
- Changes to the backend systems will necessarily impact the APIs and, consequently, the consumers.
- The data returned by the APIs is typically bound to the data structures of the backend systems as opposed to a non-proprietary business model.
- Whilst the API Gateway may perform coarse level authorisation, it is unlikely to filter data at a granular level. 

In this conventional model, the last two points can only be addressed at the cost of highly complex API service logic – hence the term “macroservices” used by Gartner. 

One might represent this coupling as a collection of meshed gears, whereby moving any one will force movement in the others:


#### Digital Integration Hub to the Rescue

The problems mentioned above can be resolved by introducing a **High-Performance Data Store** (HPDS) which sits between the integration and the services layer:

*Image from* *"Turbocharge Your API Platform with a Digital Integration Hub – Gartner (G00360082, Jul 2018)*

The main purpose of this layer is to create an aggregated replica of the system of record data, fed via the integration layer which ideally operates in an event-based fashion (for example, Change Data Capture). This enables several significant improvements:

- The APIs can deliver a much more responsive user experience as they draw from the HPDS instead of competing with the core processing functions of the target System of Record (SoR).
- The SoRs can concentrate resources on their primary activities rather than serving API requests.
- Complete decoupling of the APIs from the SoRs affords potential 24/7 availability, as well as shielding consumers from replacement of a legacy system.
- The heavy lifting of normalising and aggregating data can be delegated to the HPDS instead of the microservices.
- Reporting and analytics can also draw from the HPDS, providing business insight whilst again relieving the load on the primary SoRs.

The HPDS can be implemented in many different ways; for example, it may include a data lake, a data warehouse, an MDM, etc. The key is that it is *highly performant*, and a good metadata management solution would be essential to support a domain-driven design. 

The integration layer should also support multiple patterns, although these will vary according to the organisation’s requirements. Example patterns would include:

- Event brokering / messaging
- Extract Transform & Load (ETL)
- Change Data Capture (CDC)
- Integration Patterns (ESB, iPaaS)
- Stream processing (Spark, Flint)

#### Example Architecture

There are few (if any) products that will give you a full Digital Integration Hub out of the box. In all likelihood, it requires an assembly of multiple products, possibly from different vendors. 

That said, Microsoft provides an Azure DIH Accelerator to facilitate building a DIH architecture in the cloud. Hosted in GitHub, it provides a pre-configured development environment with a sample application, as well as build and deployment automation.

The architecture is fairly basic, but it is a starting point which supports injection of your own business logic, as well as swapping out components (for example, substituting a SQL Database for the provided PostgreSQL database). 

*Image from Microsoft, DIH Accelerator on GitHub*

In this sample, the front-end APIs are implemented via API Gateway and Azure Functions, the integration layer is comprised of Logic Apps and Event Grid, and a data layer consists of a PosgreSQL database. It also provides monitoring via App Insights and Log Analytics. Although not included in the sample, Azure Synapse can easily be bolted on to provide analytics.

#### Challenges

A Digital Integration Hub is not a simple architecture by any means and would typically be suited to a large mature enterprise that is going through a digital transformation. Some of the key challenges include:

- Complexity of rolling out a high-performance data management technology (e.g. NoSQL DBMS or in-memory data grid)
- Supporting bidirectional, event-driven synchronization between the HPDS and SoR applications
- Designing a canonical data model for the DIH business entities that supports multiple channels
- Implementing appropriate metadata management to support discovery and introspection of data entities and relationships represented across multiple data sources
- Designing, building, and managing the complex distributed architecture of a DIH

Any organisation that aspires to setting up a DIH would do well to follow these recommendations:

- Determine if the organisation needs a DIH and if it has the skills to support it.
- Know its data and consumer requirements.
- Understand the integration patterns that will be required.
- Design its APIs to be abstracted from the underlying systems (“API First” approach).
- Consider using a technology partner for implementation.

#### Summary

API-based access to disparate data services is costly from a performance and maintenance perspective. A **Digital Integration Hub** enables enhanced performance in accessing your organisational data, while ensuring effective protection of your backend systems. A DIH architecture also provides increased scalability, greater flexibility, and better insights.