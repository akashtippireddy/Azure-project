# Architecture

## Overview

The solution combines Azure cost data, workload inventory, commitment analysis, purchase governance, and ongoing monitoring.

```mermaid
flowchart LR
    Usage[Azure compute usage] --> Cost[Cost Management exports]
    Inventory[Resource inventory] --> Analysis[Coverage and commitment analysis]
    Cost --> Analysis
    Analysis --> Decision{Purchase model}
    Decision --> RI[Reserved Instance]
    Decision --> SP[Savings Plan for Compute]
    Decision --> PAYG[Pay-as-you-go]
    RI --> Monitor[Utilization and savings monitoring]
    SP --> Monitor
    PAYG --> Monitor
    Monitor --> Review[Monthly optimization review]
    Review --> Analysis
```

## Main Components

1. Azure Cost Management provides usage and charge data.
2. Azure Resource Graph or inventory exports identify eligible resources.
3. Analysis scripts calculate baseline cost, expected commitment, coverage, and risk.
4. Azure Reservations and Savings Plan APIs or portal workflows support purchasing.
5. Cost Management dashboards and scheduled reviews measure results.

## Design Principles

- Commit only against demonstrated, durable usage.
- Separate technical eligibility from financial suitability.
- Preserve flexibility for workloads that may change region, family, or service.
- Review utilization and effective savings after implementation.
