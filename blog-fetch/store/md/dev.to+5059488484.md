If you're working with Dynamics 365 CE and deploying across multiple environments, you’ve probably run into issues with broken Power Automate flows or missing lookup data after a deployment.

This post walks through how to set up a fully automated CI/CD pipeline using Azure DevOps, so you can consistently deploy:

- Managed solutions
- Power Automate flows with working connections
- Reference or lookup data

All without needing to manually tweak things post-deployment.

## Why Bother with CI/CD?

Manually exporting solutions, updating connections, and importing data wastes time and introduces errors. CI/CD solves this by making deployments repeatable and reliable.

In our case, we’ll focus on deployments from a DEV environment to SIT/UAT/PROD using Azure DevOps pipelines and a few Microsoft tools like Power Platform CLI and Configuration Migration Tool (CMT).

## What We’re Automating

We'll automate the following:

- Exporting the solution from the DEV environment
- Exporting reference data (e.g., for lookup fields like Countries, Categories)
- Deploying the solution to the target environment
- Overriding connection references in Power Automate flows
- Importing the reference data into the target environment

This will result in a clean deployment experience, with zero manual steps.

## Tools You’ll Need

- Power Platform CLI (`pac` )
- Azure DevOps pipelines
- Configuration Migration Tool (CMT)
- Package Deployer (optional)
- PowerShell (for some glue code)

## Build Pipeline: Export from DEV

Use a DevOps task to export your managed solution. Here’s a typical configuration:

PowerPlatformExportSolution

Authentication: Service Principal

Service Connection: DevSPN

Environment URL: Dev Environment

Solution Name: MySolution

Export Format: Managed

Output File: MySolution.zip

You can also export reference data using CMT. Use the UI once to generate a schema (ConfigSchema.xml), then automate it using this PowerShell command:

DataMigrationUtility.exe /export /schema:"schemas/ConfigSchema.xml" /datafile:"reference-data.zip"

## Release Pipeline: Import to SIT/UAT/PROD

Once your solution and data are exported and published as artifacts, your release pipeline should:

1. Import the managed solution
2. Apply connection reference overrides
3. Import the reference data

Example PowerPlatformImportSolution task:

Authentication: Service Principal

Service Connection: TargetSPN

Environment URL: TargetEnv

Solution File: MySolution.zip

To import reference data:

Use DataMigrationUtility.exe with /import mode and pass the reference data zip along with your connection string.

## Handling Flow Connections (Connection Reference Overrides)

When deploying flows, they often fail due to connections that still point to DEV. You can avoid this by using connection reference overrides.

Here’s an example mapping:

shared_commondataservice_abc123 → shared_commondataservice/xyz789

This JSON file maps DEV connection references to ones available in the target environment. You can reference this during solution import.

## Wrapping It Up

With this pipeline setup, your Dynamics 365 CE deployments will include:

Your solution and customizations

Power Automate flows with working connections

Lookup/reference data used in forms or business rules

No more manually fixing things after deployment.

## Top comments (0)