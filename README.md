# data-mesh

I'm learning how to implement a data mesh using docker and python.

### Why create a data mesh?

Imagine that I'm working with a movie and streaming platform, and they want to improve their recommendation system. However, the data could be utilized in a better way.

A data mesh is an alternative approach to the current paradigm of handling and processing big data. Rather than having a team of specialized data engineers that only handle the ETL portion of the data journey and who are sometimes unaware of where the data is coming from or how it will be used, i.e., its final output. The data mesh will allow for a decentralized way to access data.

### Potential users of the data mesh

- Team of data scientists/analysts who need a product for movies
- Team of data scientists/analysts who need a product for tv series
- Team of data scientists/analysts who need a product for users
- Team of data scientists/analysts who need a product for payment methods

### Initial Configs

The data products within a data mesh should be discoverable. I'll create a mini catalog that works as a centralized location for data scientists/analysts, data engineers, or other stakeholders. Each newly created data product will be stored in the catalog, and the header of the catalog should include...

- ID
- Location
- Created By
- Name
- Creation Date
- Functionality
- Department
- Schema
