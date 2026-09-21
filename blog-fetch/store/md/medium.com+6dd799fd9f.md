# Dynamics CRM Plugin: IPlugin and IServiceProvider

We’ve discussed the most general concept of D365 Plugin here. Now we’re going to break it down technically before writing our first Plugin code. We need to understand the very fundamental library that we’ll use and what does it do. This is very important (at least for me at the beginning) as I used to question everything as I’m working on a more complex business requirement.

### The Microsoft Starting Point

Basically, a D365 Plugin is just this:

```
using System;
public interface IPlugin
{
     void Execute(IServiceProvider serviceProvider);
}
```
So any class that implements this IPlugin interface is its own Plugin class. What you need to do to implement your first Plugin is just this:

```
using System;
using Microsoft.Xrm.Sdk;
namespace TestPlugin
{
    public class TestPlugin : IPlugin
    {
        public void Execute(IServiceProvider serviceProvider)
        {
        }
    }
}
```
If you have this class on your project, build it, and register the assembly (.dll file) to your D365 environment, it will automatically detect that you’re trying to register a plugin called TestPlugin.

### What is IServiceProvider?

So the only thing that’s being handed out to us from the CRM platform is just IServiceProvider object, and from this, we have to manually dig out other objects that we’re going to use for our Plugins. There are 3 of the most fundamental objects we usually use:

1. **IPluginExecutionContext**
Contains all information about a specific execution context. who triggered, what message (Create/Update/Delete), which entity, which stage (Pre-Validation / Pre-Operation / Post-Operation), input/output parameters, pre-images, post-images, depth, correlation id, shared variables, etc. (more)
2. **ITracingService**
To create trace logs that show up in the CRM trace log. (more)
3. **IOrganizationServiceFactory**
Contains IOrganizationService, which is the actual CRUD API to talk back to CRM. (more)

### Why does Microsoft give us one blob (IServiceProvider) instead of just passing the three objects directly into Execute?

Think of IServiceProvider as a menu. Microsoft hands you the menu and you order what you need. If they add new dishes later, the menu grows but the way you order stays the same, and your existing code keeps working.

Here’s how you get those 3 objects from IServiceProvider, and see how we use them:

```
using System;
using Microsoft.Xrm.Sdk;
namespace TestPlugin
{
    public class TestPlugin : IPlugin
    {
        public void Execute(IServiceProvider serviceProvider)
        {
            // ITracingService
            ITracingService tracingService = serviceProvider.GetService(typeof(ITracingService)) as ITracingService;
            // IPluginExecutionContext
            IPluginExecutionContext context = serviceProvider.GetService(typeof(IPluginExecutionContext)) as IPluginExecutionContext;
            // IOrganizationService
            IOrganizationServiceFactory serviceFactory = serviceProvider.GetService(typeof(IOrganizationServiceFactory)) as IOrganizationServiceFactory;
            IOrganizationService service = serviceFactory.CreateOrganizationService(context.UserId);
            
            tracingService.Trace($"Plugin fired for {context.MessageName} on {context.PrimaryEntityName}");
            
            if (context.InputParameters.Contains("Target") &&
                context.InputParameters["Target"] is Entity entity)
            {
                tracingService.Trace($"Target entity: {entity.LogicalName}, ID: {entity.Id}");
            }
        }
    }
}
```
As you can see we have if condition to check if context.InputParameters has Target entity, this is because Target entity isn’t always there. It exists for Create/Update but the shape differs for other messages. This target entity is the record from which we trigger the Plugin, so it contains the Id and the triggered attributes. We can use this Target entity to modify the value of other attributes for that record if the Plugin runs on the PreOperation stage, so we don’t have to call service.Update() separately, which saves a database round-trip and avoids triggering another plugin chain.

If you’ve yet to get a really good grip on what we’ve talked so far, you probably will have a better understanding once we write our first D365 Plugin. Although what we wrote here is technically a working plugin, it doesn’t do much yet, it just traces. In the next article, we’ll register it to an entity in CRM, see it actually fire on real events, and start making it do useful work.