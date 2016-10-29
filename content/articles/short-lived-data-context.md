Title: [C#] Why it’s better to have short-lived DataContext
Date: 2014-08-20 10:20
Category: C#
Tags: c#, datacontext
Authors: Rok Povšič


This is the content of my super blog post.
rk with SQL databases in your C# application, one way is to use LINQ to SQL framework. The way to use LINQ to SQL is to create an instance of DataContext for your specific database and use it to retrieve, insert, update and delete data.

If the project is not too large, you could have all your dealings with database abstracted in one class. That puts all your database logic in one place. You also can easily mock this class (as opposed to mocking DataContext). Let’s call this DatabaseOperations.

When having a class which contains methods that do work the database, two ways of dealing with DataContext come to mind.

```csharp
public class DatabaseOperations : IDatabaseOperations
{
    private readonly MyDatabaseDataContext _context;

    public DatabaseOperations(MyDatabaseDataContext context)
    {
        _context = context;
    }

    public List<User> GetUsers()
    {
        // Retrieve users by using _context.
    }

    public List<Role> GetRoles()
    {
        // Retrieve roles by using _context.
    }

    public List<Group> GetGroups()
    {
        // Retrieve groups by using _context.
    }
}
```

Another way would be without the context instance as a field. Here each method creates and closes its own context. Sample code:

```csharp
public class DatabaseOperations : IDatabaseOperations
{
    private readonly string _connectionString = "myConnStr";

    public List<User> GetUsers()
    {
        using (var context = new MyDatabaseDataContext(_connectionString))
        {
            // Retrieve users by using context.
        }
    }

    public List<Role> GetRoles()
    {
        using (var context = new MyDatabaseDataContext(_connectionString))
        {
            // Retrieve roles by using context.
        }
    }

    public List<Group> GetGroups()
    {
        using (var context = new MyDatabaseDataContext(_connectionString))
        {
            // Retrieve groups by using context.
        }
    }
}
```

At first, the second approach may seem to be more wasteful as each function has to create the context. That creates some amount of duplicated code. However, there are two reasons why this second approach is preferred.

The first reason is that in the first example the instance of a class DatabaseOperations can live a long time. You probably do not create new instance of the class each time you call function inside. Long lived DatabaseOperations instance means also that the injected DataContext lives long time. The DataContext, however, is supposed to be used on only small units of work. The reason is that in the first example, one instance of DataContext has to track the changes that happen in returned objects.

More info in the [official documentation](http://msdn.microsoft.com/en-us/library/system.data.linq.datacontext(v=vs.110).aspx):

> In general, a DataContext instance is designed to last for one “unit of work” however your application defines that term. A DataContext is lightweight and is not expensive to create. A typical LINQ to SQL application creates DataContext instances at method scope or as a member of short-lived classes that represent a logical set of related database operations.

The second reason, which is important from the design point of view, is that in first example, DataContext has to be passed in via constructor. However, the DatabaseOperations class behaves like a Service Object and in order to use dependency injection, Service Objects should take as constructor parameters only other Service Objects. DataContext is more of a Value Object which does not belong in the parameter list. The tree of Service Objects cannot be created at the start of the program.

For more info see [this blog article](http://misko.hevery.com/2008/09/30/to-new-or-not-to-new/) by Miško Hevery (who is the author of JavaScript framework AngularJS).

You could, of course, also have DataContext as a parameter in every function. That would allow your class to be a Service Object which has no Value Objects in the constructor parameter list. However, the first reason would still be violated if that DataContext is long-lived or, as the documentation says, used for more than one “unit of work”.

In order to somehow mitigate the duplication of code by creating a new DataContext in every method, you might be able to use the trick from [this StackOverflow answer](http://stackoverflow.com/a/23367569/365837).

That might or might not be useful for you, depending on where you store and how you obtain the connection string. For example, if you have it stored as a static class field, then it is appropriate. If you have to get the connection string from a file or another database, then it might get a bit complicated (in my last project, I decided against it and just used the simple approach shown in the second example).